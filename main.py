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

def print_hex( str ):
    return ':'.join(x.encode('hex') for x in str)


def send_value( str ) :
    print "Writing value 0x%s in address 0x%s" %(reg_value, start_addr)
    respond = ""
    count = ser.timeout -1
    while (count >= 0  and sys.getsizeof(respond) == 21  ) :
        print "Sending: " + print_hex(str)
        ser.write(str)
        respond = ser.read(8)
        count -= 1

    print "Received : " + print_hex(respond)
    if str == respond:
        print "The value was assigned successfully"
    else:
        print "The value wasnt assigned"

# def recv_value( str ) :
#     print "Asking value of %d register(s) from address 0x%s" %(reg_quantity, start_addr)
#     print "Sending: " + print_hex(str)
#     ser.write(str)
#     respond = ser.read(7)
#     print "Received : " + print_hex(respond)
#     print "The value received is %s" %print_hex(respond[3:5])

def recv_multiple_values ( str ):
    print "Asking value of %s register(s) from address 0x%s" %(reg_quantity, start_addr)
    respond = ""
    count = ser.timeout - 1
    while (count >= 0  and sys.getsizeof(respond) == 21  ) :
        print "Sending: " + print_hex(str)
        ser.write(str)
        respond = ser.read(5 + int(reg_quantity)*2 )
        count -= 1
    print sys.getsizeof(respond)
    print "Received : " + print_hex(respond)
    if sys.getsizeof(respond) > 26 :
        for i in range(0,int(reg_quantity)):
            print i
            print "The value received is %s" %print_hex(respond[3+i*2:5+i*2])

def write_multiple_values ( str ) :
    print "write_Multiple_values"
    print "Writing 0x%s registers in address from 0x%s" %(int(reg_quantity), start_addr)
    respond = ""
    count = ser.timeout - 1
    while (count >= 0  and sys.getsizeof(respond) == 21  ) :
        print "Sending: " + print_hex(str)
        ser.write(str)
        respond = ser.read(8)
        count -= 1

    print "Received : " + print_hex(respond)
    if str == respond:
        print "The value was assigned successfully"
    else:
        print "The value wasnt assigned"


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
F_03 = "\x03"
F_06 = "\x06"
F_16 = "\x10"


ser = serial.Serial()

msg = "Select the port to use"
title = "Selecting Serial Port"
choices = ["COM1", "COM2"]
choice = easygui.choicebox(msg, title, choices)

if choice == "COM1":
    ser.port = 0
elif choice == "COM2":
    ser.port = 1




msg = "Setting the port"
title = "Setting the port "
fieldNames = ["Timeout","Attempts"]
fieldValues_port = []  # we start with blanks for the values
fieldValues_port = easygui.multenterbox(msg,title, fieldNames)

ser.timeout = int(fieldValues_port[0])
attempts = int(fieldValues_port[1])

ser.open()


print ser


print "Initiating..."


title = "Sistema de Transmision de Datos"
msg = "MODBUS"
choices = ["Read Holding Register","Write Single Register", "Write Multiple Register"]
reply = easygui.buttonbox(msg,title, choices=choices)

if reply == "Read Holding Register":
    fieldNames = ["ID","Starting address","Quantity of Registers"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multenterbox(msg,title, fieldNames)

    id = int(fieldValues[0])
    start_addr = fieldValues[1]
    reg_quantity = int(fieldValues[2])


    recv = struct.pack("B", id) + F_03 + start_addr.decode("hex") + struct.pack("!h", reg_quantity)
    recv = recv  + struct.pack("H", calculate_crc16(recv))
    recv_multiple_values(recv)



elif reply == "Write Single Register":
    fieldNames = ["ID","Register Address","Register Value"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multenterbox(msg,title, fieldNames)

    id = int(fieldValues[0])
    start_addr = fieldValues[1]
    reg_value = int(fieldValues[2])


    send = struct.pack("B", id) + F_06 + start_addr.decode("hex") + struct.pack("!h", reg_value)
    #send = id.decode("hex") + F_06 + start_addr.decode("hex") + reg_value.decode("hex")
    send = send + struct.pack("H", calculate_crc16(send))
    send_value(send)




elif reply == "Write Multiple Register":
    fieldNames = ["ID","Starting Address","Quantity of Registers", "Byte count", "Registers Value"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = easygui.multenterbox(msg,title, fieldNames)

    id = int(fieldValues[0])
    start_addr = fieldValues[1]
    reg_quantity = int(fieldValues[2])
    byte_count = int(fieldValues[3])
    reg_value = fieldValues[4].split(' ')

    print reg_value


    send_multiple = struct.pack("B", id) + "\x10" + start_addr.decode("hex") + struct.pack("!h", reg_quantity) + struct.pack("B", byte_count)

    for value in range(0, reg_quantity):
        send_multiple = send_multiple + struct.pack("!h", int(reg_value[value]))
    send_multiple = send_multiple + struct.pack("H", calculate_crc16(send_multiple))
    write_multiple_values(send_multiple)


ser.close()
