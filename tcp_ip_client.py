__author__ = 'VictorNahuel'

import socket

s = socket.socket()
s.connect(("localhost", 3333))

while True:
      mensaje = raw_input("> ")
      s.send(mensaje)
      if mensaje == "quit":
         break

print "adios"

s.close()