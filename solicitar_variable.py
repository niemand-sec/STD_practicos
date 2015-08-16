__author__ = 'BlackSwan'

import serial
#from PyCRC.CRC16 import CRC16
import crc16
import binascii
import re
import struct
from ctypes import create_string_buffer

def print_hex( str ):
    return ':'.join(x.encode('hex') for x in str)


def send_value( str ) :
    print "Writing value 0x%s in address 0x%s" %(reg_value, start_addr)
    print "Sending: " + print_hex(str)
    ser.write(str)
    respond = ser.read(8)
    print "Received : " + print_hex(respond)
    if str == respond:
        print "The value was assigned successfully"
    else:
        print "The value wasnt assigned successfully"


def recv_value( str ) :
    print "Asking value of %d register(s) from address 0x%s" %(reg_quantity, start_addr)
    print "Sending: " + print_hex(str)
    ser.write(str)
    respond = ser.read(7)
    print "Received : " + print_hex(respond)
    print "The value received is %s" %print_hex(respond[3:5])

def recv_multiple_values ( str ):
    print "Asking value of %d register(s) from address 0x%s" %(reg_quantity, start_addr)
    print "Sending: " + print_hex(str)
    ser.write(str)
    respond = ser.read(5 + reg_quantity*2 )
    print "Received : " + print_hex(respond)
    for i in range(0,reg_quantity):
        print "The value received is %s" %print_hex(respond[3+i*2:5+i*2])

def write_multiple_values ( str ) :
    print "write_Multiple_values"
    #function 16


def calculate_crc16( str ) :
    crc = 0xFFFF
    for ch in str:
        crc = crc16.calcByte( ch, crc)
    return crc

global id
global start_addr
global reg_quantity
global reg_value
ser = serial.Serial()
ser.port = 1

print "Initiating..."

id = 1
start_addr = '0007'
reg_quantity = 1
reg_value = '0220'

print ser
ser.open()
print ser.name


send = struct.pack("B", id) + "\x06" + start_addr.decode("hex") + reg_value.decode("hex")
print type(calculate_crc16(send))
send = send + struct.pack("H", calculate_crc16(send))
send_value(send)






recv = struct.pack("B", id) + "\x03" + start_addr.decode("hex") + struct.pack("!h", reg_quantity)
recv = recv  + struct.pack("H", calculate_crc16(recv))

recv_multiple_values(recv)

ser.close()



# TODO: menu para elegir que hacer en el programa
# TODO: Ingreso de parametros
# TODO: funcion 16
