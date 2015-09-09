__author__ = 'VictorNahuel'

import socket

s = socket.socket()
s.bind(("localhost", 3333))
s.listen(10)

sc, addr = s.accept()

while True:
  recibido = sc.recv(1024)
  print "Recibido:", recibido
  sc.send(recibido)

print "adios"

sc.close()
s.close()
