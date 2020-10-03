# python version : 3.8.5
# modify the UDPClient(python3).py from the lecture

from datetime import datetime
from socket import *
import sys

# Define connection (socket) parameters
# Address + Port no
# Server would be running on the same host as Client
serverName = sys.argv[1]

# change this port number if required
serverPort = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_DGRAM)
# This line creates the client's socket. The first parameter indicates the address family; in particular,
# AF_INET indicates that the underlying network is using IPv4.The second parameter indicates that the socket is of
# type SOCK_DGRAM,which means it is a UDP socket (rather than a TCP socket, where we use SOCK_STREAM).

time_rtts = []
i = 3331
while i <= 3345:
    time_send = datetime.now()
    message = 'PING ' + str(i) + ' ' + str(time_send) + '\r\n'

    clientSocket.sendto(message.encode('utf-8'), (serverName, serverPort))
    # Note the difference between UDP sendto() and TCP send() calls. In TCP we do not need to attach the destination
    # address to the packet, while in UDP we explicilty specify the destination address + Port No for each message

    try:
        clientSocket.settimeout(0.6)
        modifiedMessage, serverAddess = clientSocket.recvfrom(1024)
        # Note the difference between UDP recvfrom() and TCP recv() calls.
        time_receive = datetime.now()
        rtt = round((time_receive - time_send).total_seconds() * 1000)
        time_rtts.append(rtt)
        print(f'ping to {serverName}, seq = {i}, rtt = {rtt} ms')
        clientSocket.settimeout(None)

    except timeout:
        print(f'ping to {serverName}, seq = {i}, rtt = time out')

    i += 1

print(
    f'min RTT = {min(time_rtts)} ms, max RTT = {max(time_rtts)} ms, average RTT = {sum(time_rtts) / len(time_rtts)} ms')

clientSocket.close()
# Close the socket
