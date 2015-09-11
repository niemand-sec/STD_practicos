__author__ = 'BlackSwan'

import serial
import easygui
import crc16
import struct
import sys
import serial.tools.list_ports
import socket

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

def manage_error_tcp( packet ):
    print "The value wasnt assigned"
    if packet[8] == "\x01" :
        print "ILLEGAL FUNCTION CODE"
    elif packet[8] == "\x02":
        print "ILLEGAL DATA ADDRESS"
    elif packet[8] == "\x03":
        print "ILLEGAL DATA VALUE"
    elif packet[8] == "\x04":
        print "SERVER FAILURE"
    elif packet[8] == "\x05":
        print "ACKNOWLEDGE"
    elif packet[8] == "\x06" :
        print "SERVER BUSY"
    elif packet[8] == "\x0A" :
        print "GATEWAY PROBLEM"
    elif packet[8] == "\x0B" :
        print "GATEWAY PROBLEM"
    else :
        print "Other error"



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

def send_value_tcp( pckt ) :
    print "Writing value 0x%s in address 0x%s" %(reg_value, start_addr)
    respond = ""
    print "Sending: " + print_hex(pckt)
    s.send(pckt)
    try :
        respond = s.recv(21)
    except :
        print "Time out"

    if sys.getsizeof(respond) == 21:
        return

    print "Received : " + print_hex(respond)

    if "\x86" == respond[7]:
        manage_error_tcp(respond)
    elif "\x06" == respond[7]:
        print "The value was assigned successfully"

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
                print "[%s]\t=>\t%s\t=>\t" %(value_print * 125 + i + index_reg , print_hex_without_colon(respond[3+i*2:5+i*2])),
                print "%s\t=>\t" %struct.unpack('!H', respond[3+i*2:5+i*2]),
                print ' '.join('{0:08b}'.format(ord(x), 'b') for x in respond[3+i*2:5+i*2])
        else :
            print "Transmission error"
    elif sys.getsizeof(respond) == 26 :
        manage_error(respond)
    elif sys.getsizeof(respond) == 21 :
        print "No response"

def recv_multiple_values_tcp ( str):
    print "Asking value of %s register(s) from address 0x%s" %(quantity, start_addr)
    respond = ""
    count = ser.timeout - 1
    while (count >= 0  and sys.getsizeof(respond) == 21  ) :
        print "Sending: " + print_hex(str)
        ser.write(str)   #cambiar para tcp
        respond = ser.read(5 + int(quantity)*2 )  #cambiar para tcp
        count -= 1
    print "Received : " + print_hex(respond)
    if sys.getsizeof(respond) > 26 :   #cambiar para tcp
        if respond[len(respond)-2:] == struct.pack("H", calculate_crc16(respond[:len(respond)-2])):   #no usar mas crc
            for i in range(0,int(quantity)):
                print "[%s]\t=>\t%s\t=>\t" %(value_print * 125 + i + index_reg , print_hex_without_colon(respond[3+i*2:5+i*2])),
                print "%s\t=>\t" %struct.unpack('!H', respond[3+i*2:5+i*2]),
                print ' '.join('{0:08b}'.format(ord(x), 'b') for x in respond[3+i*2:5+i*2])
        else :
            print "Transmission error"
    elif sys.getsizeof(respond) == 26 :  #cambiar para tcp
        manage_error(respond)
    elif sys.getsizeof(respond) == 21 :   #cambiar para tcp
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

def write_multiple_values_tcp ( str ) :
    print "Writing 0x%s registers in address from 0x%s" %(int(reg_quantity), start_addr)
    respond = ""
    print "Sending: " + print_hex(str)
    s.send(str)
    try :
        respond = s.recv(12)
    except :
        print "Time out"

    if sys.getsizeof(respond) == 30:
        print "TIME OUT"
        return

    print "Received : " + print_hex(respond)

    if "\x90" == respond[7]:
            manage_error_tcp(respond)
    elif "\x10" == respond[7]:
            print "The values were assigned successfully"
    else :
        print "Transmission error"

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
global tx_id

while (True) :

    title = "Sistema de Transmision de Datos"
    msg = "MODBUS"
    choices = ["TCP/IP","Serial Port"]
    reply = easygui.buttonbox(msg,title, choices=choices)
    sys.stdout = open('output', 'w')

    if reply == "TCP/IP" :

        msg = "Setting TCP/IP"
        title = "Setting TCP/IP "
        fieldNames = ["IP","Port", "Timeout", "Attempts"]
        fieldValues = ["localhost", "502", "3", "3"]  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames, fieldValues)
        if fieldValues == None:
            break
        tx_id = 0
        ip = fieldValues[0]
        port = int(fieldValues[1])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(int(fieldValues[2]))
        attempts = int(fieldValues[3])
        while (attempts > 0) :
            print attempts
            try :
                if not s.connect((ip, port)) :
                    break
                else :
                    pass
            except :
                attempts -= 1
                print "Attempt %d failed" %attempts

        # EJEMPLO DE COMUNICACION TCP
        #mensaje = "\x01\x00\x00\x00\x00\x06\x01\x03\x00\x00\x00\x02"
        #s.send(mensaje)
        #print print_hex(s.recv(12))
        if attempts != 0 :
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
                    if fieldValues == None:
                        break
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
                        recv = struct.pack("B", id) + F_03 + struct.pack("!h",start_addr) + struct.pack("!h", quantity) #corregir paquete
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
                    if fieldValues == None:
                        break
                    id = int(fieldValues[0])
                    start_addr = int(fieldValues[1])
                    reg_value = int(fieldValues[2])
                    send = struct.pack("!h", tx_id) + "\x00\x00" + "\x00\x06"  + struct.pack("B", id) + F_06 + struct.pack("!h",start_addr) + struct.pack("!H", reg_value)
                    send_value_tcp(send)


                elif reply == "Write Multiple Register":
                    fieldNames = ["ID","Starting Address","Quantity of Registers", "Byte count", "Registers Value"]
                    fieldValues = []  # we start with blanks for the values
                    fieldValues = easygui.multenterbox(msg,title, fieldNames)
                    if fieldValues == None:
                        break
                    id = int(fieldValues[0])
                    start_addr = int(fieldValues[1])
                    reg_quantity = int(fieldValues[2])
                    byte_count = int(fieldValues[3])
                    reg_value = fieldValues[4].split(' ')
                    length = 7 + 2 * reg_quantity
                    send_multiple = struct.pack("!h", tx_id) + "\x00\x00" + struct.pack("!h", length)  + struct.pack("B", id) + "\x10" + struct.pack("!h",start_addr) + struct.pack("!h", reg_quantity) + struct.pack("B", byte_count) #corrregit estructura pquete

                    for value in range(0, reg_quantity):
                        send_multiple = send_multiple + struct.pack("!H", int(reg_value[value]))
                    write_multiple_values_tcp(send_multiple)

                tx_id += 1
                sys.stdout = open ('output', 'r')
                easygui.codebox(msg, title, sys.stdout.readlines())
        else :
            print "Connection TIMEOUT"
            sys.stdout = open ('output', 'r')
            easygui.codebox(msg, title, sys.stdout.readlines())

    elif reply == "Serial Port":

        ser = serial.Serial()
        sys.stdout = open('output', 'w')
        ports = list(serial.tools.list_ports.comports())

        msg = "Select the port to use"
        title = "Selecting Serial Port"
        choices = []
        for port in ports:
            choices.append(port[0])
        choice = easygui.choicebox(msg, title, choices)
        if choice == None:
            break

        ser.port = int(choice[len(choice)-1:]) - 1


        msg = "Setting the port"
        title = "Setting the port "
        fieldNames = ["Timeout","Attempts","Baudrate","ByteSize","Parity", ]
        fieldValues_port = []  # we start with blanks for the values
        fieldValues_port = easygui.multenterbox(msg,title, fieldNames)
        if fieldValues_port == None:
            break
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

            title = "Sistema de Transmision de Datos"
            msg = "MODBUS"
            choices = ["Read Holding Register","Write Single Register", "Write Multiple Register"]
            reply = easygui.buttonbox(msg,title, choices=choices)

            if reply == "Read Holding Register":
                fieldNames = ["ID","Starting address","Quantity of Registers"]
                fieldValues = []  # we start with blanks for the values
                fieldValues = easygui.multenterbox(msg,title, fieldNames)
                if fieldValues_port == None:
                    break
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
                if fieldValues == None:
                    break
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
                if fieldValues == None:
                    break
                id = int(fieldValues[0])
                start_addr = int(fieldValues[1])
                reg_quantity = int(fieldValues[2])
                byte_count = int(fieldValues[3])
                reg_value = fieldValues[4].split(' ')

                send_multiple = struct.pack("B", id) + "\x10" + struct.pack("!h",start_addr) + struct.pack("!h", reg_quantity) + struct.pack("B", byte_count)

                for value in range(0, reg_quantity):
                    send_multiple = send_multiple + struct.pack("!H", int(reg_value[value]))
                send_multiple = send_multiple + struct.pack("H", calculate_crc16(send_multiple))
                write_multiple_values(send_multiple)

            sys.stdout = open ('output', 'r')
            easygui.codebox(msg, title, sys.stdout.readlines())
            #sys.stdout.close()

        ser.close()
    else :
        print "Incorrect option"

exit()
