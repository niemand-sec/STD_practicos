__author__ = 'BlackSwan'

import serial
import easygui
#from PyCRC.CRC16 import CRC16
import crc16
import binascii
import re
import struct
import sys
from ctypes import create_string_buffer
import base64
import serial.tools.list_ports


def print_hex( str ):
    return ':'.join(x.encode('hex') for x in str)

def print_hex_without_colon( str ):
    return ''.join(x.encode('hex') for x in str)

def manage_error( packet ):
    print "The value wasnt assigned"
    if packet[2] == "\x01" :
        print "ILLEGAL FUNCTION"
    elif packet[2] == "\x02":
        print "ILLEGAL DATA ADDRESS"
    elif packet[2] == "\x03":
        print "ILLEGAL DATA VALUE"
    elif packet[2] == "\x04":
        print "SLAVE DEVICE FAILURE"
    else:
        print "Transmission error"

def send_value( pckt ) :
    print "Writing value 0x%s in address 0x%s" %(reg_value, start_addr)
    respond = ""
    count = ser.timeout -1
    while (count >= 0  and sys.getsizeof(respond) == 21  ) :
        print "Sending: " + print_hex(pckt)
        ser.write(pckt)
        respond = ser.read(8)
        count -= 1
    print "Received : " + print_hex(respond)
    if sys.getsizeof(respond) > 21:
        if "\x86" == respond[1]:
            manage_error(respond)
        elif respond[len(respond)-2:] == struct.pack("H", calculate_crc16(respond[:len(respond)-2])):
            print "The value was assigned successfully"
    else:
            print "No response"



def recv_multiple_values ( str):
    print "Asking value of %s register(s) from address 0x%s" %(quantity, start_addr)
    respond = ""
    count = ser.timeout - 1
    while (count >= 0  and sys.getsizeof(respond) == 21  ) :
        print "Sending: " + print_hex(str)
        ser.write(str)
        respond = ser.read(5 + int(quantity)*2 )
        count -= 1
    print "Received : " + print_hex(respond)
    if sys.getsizeof(respond) > 26 :
        if respond[len(respond)-2:] == struct.pack("H", calculate_crc16(respond[:len(respond)-2])):
            for i in range(0,int(quantity)):
                print "[%s]\t=>\t%s\t=>\t" %(value_print * 125 + i + 1 + index_reg , print_hex_without_colon(respond[3+i*2:5+i*2])),
                print "%s\t=>\t" %struct.unpack('!H', respond[3+i*2:5+i*2]),
                print ' '.join('{0:08b}'.format(ord(x), 'b') for x in respond[3+i*2:5+i*2])
        else :
            print "Transmission error"
    elif sys.getsizeof(respond) == 26 :
        manage_error(respond)
    elif sys.getsizeof(respond) == 21 :
        print "No response"


def write_multiple_values ( str ) :
    print "Writing 0x%s registers in address from 0x%s" %(int(reg_quantity), start_addr)
    respond = ""
    count = ser.timeout - 1
    while (count >= 0  and sys.getsizeof(respond) == 21  ) :
        print "Sending: " + print_hex(str)
        ser.write(str)
        respond = ser.read(8)
        count -= 1

    print "Received : " + print_hex(respond)

    if sys.getsizeof(respond) >21:
        if respond[len(respond)-2:] == struct.pack("H", calculate_crc16(respond[:len(respond)-2])) :
            if "\x90" == respond[1]:
                manage_error(respond)
            else :
                print "The values were assigned successfully"
        else :
            print "Transmission error"
    else:
        print "No response"


def calculate_crc16( str ) :
    crc = 0xFFFF
    for ch in str:
        crc = crc16.calcByte( ch, crc)
    return crc

global id
global start_addr
global reg_quantity
global reg_value
global attempts
global byte_count
global value_printing
F_03 = "\x03"
F_06 = "\x06"
F_16 = "\x10"


ser = serial.Serial()

ports = list(serial.tools.list_ports.comports())


msg = "Select the port to use"
title = "Selecting Serial Port"
choices = []
for port in ports:
    choices.append(port[0])
choice = easygui.choicebox(msg, title, choices)

ser.port = int(choice[len(choice)-1:]) - 1


msg = "Setting the port"
title = "Setting the port "
fieldNames = ["Timeout","Attempts","Baudrate","ByteSize","Parity", ]
fieldValues_port = []  # we start with blanks for the values
fieldValues_port = easygui.multenterbox(msg,title, fieldNames)

ser.timeout = int(fieldValues_port[0])
attempts = int(fieldValues_port[1])
ser.baudrate = int(fieldValues_port[2])
ser.bytesize = int(fieldValues_port[3])
ser.parity = fieldValues_port[4]

#sys.stdout = open('output', 'w')
ser.open()

#print ser

#print "Initiating..."

while(True) :
    value_print = 0
    sys.stdout = open('output', 'w')
    title = "Sistema de Transmision de Datos"
    msg = "MODBUS"
    choices = ["Read Holding Register","Write Single Register", "Write Multiple Register"]
    reply = easygui.buttonbox(msg,title, choices=choices)

    if reply == "Read Holding Register":
        fieldNames = ["ID","Starting address","Quantity of Registers"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)

        id = int(fieldValues[0])
        start_addr = int(fieldValues[1])
        reg_quantity = float(fieldValues[2])
        times = int(reg_quantity) // 125
        if (reg_quantity/125 - times) > 0 and reg_quantity > 125 :
            times += 1
        elif reg_quantity < 125 :
            times = 1
        index_reg = start_addr
        reg_restantes = reg_quantity
        count = 1
        while (times > 0) :
            quantity = 0.0
            if reg_restantes < 125 :
                quantity = reg_restantes
            else :
                quantity = reg_restantes - (( (reg_quantity)/125 )  - count ) * 125
            recv = struct.pack("B", id) + F_03 + struct.pack("!h",start_addr) + struct.pack("!h", quantity)
            recv = recv  + struct.pack("H", calculate_crc16(recv))
            recv_multiple_values(recv)
            value_print +=1
            start_addr = start_addr +  125
            reg_restantes -= quantity
            times -= 1
            count += 1

    elif reply == "Write Single Register":
        fieldNames = ["ID","Register Address","Register Value"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)

        id = int(fieldValues[0])
        start_addr = int(fieldValues[1])
        reg_value = int(fieldValues[2])


        send = struct.pack("B", id) + F_06 + struct.pack("!h",start_addr) + struct.pack("!H", reg_value)
        #send = id.decode("hex") + F_06 + start_addr.decode("hex") + reg_value.decode("hex")
        send = send + struct.pack("H", calculate_crc16(send))
        send_value(send)


    elif reply == "Write Multiple Register":
        fieldNames = ["ID","Starting Address","Quantity of Registers", "Byte count", "Registers Value"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)

        id = int(fieldValues[0])
        start_addr = int(fieldValues[1])
        reg_quantity = int(fieldValues[2])
        byte_count = int(fieldValues[3])
        reg_value = fieldValues[4].split(' ')

        send_multiple = struct.pack("B", id) + "\x10" + struct.pack("!h",start_addr) + struct.pack("!h", reg_quantity) + struct.pack("B", byte_count)

        for value in range(0, reg_quantity):  # FUNCIONA CON 123 pero con 124 y 125 no
            send_multiple = send_multiple + struct.pack("!H", int(reg_value[value]))
        send_multiple = send_multiple + struct.pack("H", calculate_crc16(send_multiple))
        write_multiple_values(send_multiple)



    sys.stdout = open ('output', 'r')
    easygui.codebox(msg, title, sys.stdout.readlines())
    #sys.stdout.close()


ser.close()