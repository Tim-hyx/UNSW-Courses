# python version: 3.85

from socket import *
import sys

#initialise the TCP socket
Server = socket(AF_INET, SOCK_STREAM)
Server.bind(('', int(sys.argv[1])))
Server.listen(5)

while True:
    Connection, address = Server.accept() # wait for the client link accept
    try:
        message = Connection.recv(1024).decode()
        #reads the filename
        fileName = message.split()[1]
        file = open(fileName[1:], 'rb')
        #opens the file
        content = file.read()
        response = 'HTTP/1.1 200 OK\r\n\r\n'
        # send data
        Connection.sendall(response.encode())
        Connection.sendall(content)
        Connection.close() # close
    except Exception:
        response = '404 File not found\r\n\r\n'
        Connection.sendall(response.encode())
        Connection.close()
