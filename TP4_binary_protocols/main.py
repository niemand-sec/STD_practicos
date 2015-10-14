__author__ = 'BlackSwan'


import struct
import easygui
import socket
import serial
import sys
import re
import bitstring

while(True):
    while(True) :

        packet = ""

        sys.stdout = open('output', 'w')
        msg = "Binary Protocols"
        title = "Binary Protocols "
        fieldNames = ["ID1","Function","Address","Variables", "ID2", "Timestamp", "Grades", "Amper", "Volts" ]
        fieldValues = ["299","19","65535", "499", "1000", "99-12-31 23:59", "50", "10", "220"]  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames,fieldValues)
        if fieldValues == None :
            break


        id = int(fieldValues[0])
        function = int(fieldValues[1])
        address = int(fieldValues[2])
        variables = int(fieldValues[3])

        id2 = int(fieldValues[4])
        timestamp = fieldValues[5]
        grades = int(fieldValues[6])
        amperes = int(fieldValues[7])
        volts = int(fieldValues[8])

        errors = 0
        if not 0 <= id < 300 :
            easygui.msgbox("ID1 out of range")
            break
        if not 0 <= function < 20 :
            easygui.msgbox("Invalid function")
            break
        if not 0 <= address < 65536 :
            easygui.msgbox("Address out of range")
            break
        if not 0 <= variables < 500 :
            easygui.msgbox("Invalid amount of variables")
            break
        if not 0 <= id2 <= 1000 :
            easygui.msgbox("ID2 out of range")
            break
        pattern = re.compile('[0-9]{2}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}')
        if not pattern.match(timestamp) :
            easygui.msgbox("Invalid timestamp format")
            break
        else :

            timestamp = timestamp.replace("-","").replace(":","").replace(" ","")
            anio = int(timestamp[:2])
            mes = int(timestamp[2:4])
            dia = int(timestamp[4:6])
            hora = int(timestamp[6:8])
            min = int(timestamp[8:10])

            if not 0 < mes <=12:
                easygui.msgbox("Invalid month")
                break
            if not 0 < dia <=31:
                easygui.msgbox("Invalid day")
                break
            if not 0 <= hora < 24 :
                easygui.msgbox("Invalid hour")
                break
            if not 0 <= min < 60 :
                easygui.msgbox("Invalid minute")
                break

        if not 0 <= grades <= 50 :
            easygui.msgbox("Grades out of range")
            break
        if not 0 <= amperes <= 10 :
            easygui.msgbox("Invalid Amper")
            break
        if not 0 <= volts <= 220 :
            easygui.msgbox("Invalid Volts")
            break

        packet =   '{0:09b}'.format(id) + " " + '{0:05b}'.format(function) + " " + '{0:16b}'.format(address) + " " + '{0:09b}'.format(variables)


        packet2 = '{0:10b}'.format(id2)
        packet2 = packet2 + " " + '{0:08b}'.format(anio) + " " + '{0:04b}'.format(mes) + " " + '{0:05b}'.format(dia) + " " + '{0:05b}'.format(hora) + " " + '{0:06b}'.format(min)
        packet2 = packet2 + " " + '{0:06b}'.format(grades) + " " + '{0:04b}'.format(amperes) + " " + '{0:04b}'.format(volts)

        print "FIRST BIT ARRAY \n\t%s" %packet
        print "SECOND BIT ARRAY \n\t%s" %packet2


        #paquete = struct.pack("5B" , "11asd")

        #print paquete


        ser = serial.Serial()
        ser.port = 1
        ser.open()
        s = bitstring.Bits('0b11111010000110001111001111110111111011110010101011011100')
        ser.write(s.tobytes())
        #print s
        ser.close()
        sys.stdout = open ('output', 'r')
        easygui.codebox(msg, title, sys.stdout.readlines())