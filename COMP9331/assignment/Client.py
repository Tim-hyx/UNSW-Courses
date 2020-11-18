import socket, threading, sys
from enum import Enum


class Client:
    serverIp, username, needToSendFilename, needToSendThreadtitle = '', '', '', ''
    serverPort, returnCode, currentStage = 0, 0, 1
    clientSocket, exit = None, False
    states = Enum('states', ('start0', 'wait0', 'start1', 'wait1', 'exit'))
    state = states.start0

    def __init__(self, ip, port):
        self.serverIp, self.serverPort = ip, port
        try:
            self.clientSocket = socket.socket()
            self.clientSocket.connect((self.serverIp, self.serverPort))
        except:
            exit()

    def recv(self):
        while True:
            try:
                res = eval(self.clientSocket.recv(999999).decode())
                self.returnCode = res['returncode']
            except ConnectionError as e:
                return
            else:
                if res['id'] == 'ATE':
                    if res['stage'] == 2:
                        self.currentStage = 1
                        if res['returncode'] == 0:
                            print('Welcome to the forum')
                            self.state = self.states.start1
                        elif res['returncode'] == 2:
                            print('Invalid password')
                            self.state = self.states.start0
                        elif res['returncode'] == 1:
                            print(f"{res['username']} has already logged in")
                            self.state = self.states.start0
                    elif res['stage'] == 1:
                        if res['returncode'] != 2:
                            self.state, self.currentStage = self.states.start0, 2
                        else:
                            print('This user has already logged in')
                            self.state = self.states.start0
                elif res['id'] == 'MSG':
                    if res['returncode'] != 0:
                        print(f"Thread {res['threadtitle']} not exists")
                    else:
                        print(f"Message posted to {res['threadtitle']} thread")
                    self.state = self.states.start1
                elif res['id'] == 'CRT':
                    if res['returncode'] != 0:
                        print(f"Thread {res['threadtitle']} exists")
                    else:
                        print(f"Thread {res['threadtitle']} created")
                    self.state = self.states.start1
                elif res['id'] == 'EDT':
                    if res['returncode'] == 0:
                        print('The message has been edited')
                    elif res['returncode'] == 2:
                        print('Message number not exist.')
                    elif res['returncode'] == 1:
                        print("The message belongs to another user and cannot be edited")
                    self.state = self.states.start1
                elif res['id'] == 'DLT':
                    if res['returncode'] == 0:
                        print('The message has been deleted')
                    elif res['returncode'] == 2:
                        print('Message number not exist.')
                    elif res['returncode'] == 3:
                        print(f"Thread {res['threadtitle']} not exists")
                    elif res['returncode'] == 1:
                        print("The message belongs to another user and cannot be edited")
                    self.state = self.states.start1
                elif res['id'] == 'LST':
                    if res['content'] != '':
                        print('The list of active threads:')
                        print(res['content'])
                    else:
                        print('No threads to list')
                    self.state = self.states.start1
                elif res['id'] == 'RDT':
                    if res['returncode'] != 0:
                        print(f"Thread {res['threadtitle']} does not exist")
                    else:
                        if res['content'] != '':
                            print(res['content'])
                        else:
                            print(f"Thread {res['threadtitle']} is empty")
                    self.state = self.states.start1
                elif res['id'] == 'DWN':
                    if res['returncode'] == 0:
                        with open(res['filename'], 'wb') as fp:
                            fp.write(res['filedata'])
                        print(f"{res['filename']} successfully downloaded")
                    elif res['returncode'] == 2:
                        print(f"Thread {res['threadtitle']} not exists")
                    elif res['returncode'] == 1:
                        print(f"File does not exist in Thread {res['threadtitle']}")
                    self.state = self.states.start1
                elif res['id'] == 'UPD':
                    if self.currentStage == 2:
                        self.currentStage = 1
                        print(f"{res['filename']} uploaded to {res['threadtitle']} thread")
                    elif self.currentStage == 1:
                        if res['returncode'] == 1:
                            self.currentStage = 1
                            print('File exist.')
                        elif res['returncode'] == 0:
                            self.currentStage, self.needToSendFilename, self.needToSendThreadtitle = 2, res['filename'], \
                                                                                                     res['threadtitle']
                        else:
                            self.currentStage = 1
                            print('Thread not exist.')
                    self.state = self.states.start1
                elif res['id'] == 'RMV':
                    if res['returncode'] == 0:
                        print(f"Thread {res['threadtitle']} removed")
                    elif res['returncode'] == 2:
                        print('The thread was created by another user and cannot be removed')
                    elif res['returncode'] == 1:
                        print(f"Thread {res['threadtitle']} not exist")
                    self.state = self.states.start1
                elif res['id'] == 'XIT':
                    if res['returncode'] == 0:
                        print('Goodbye.')
                        self.exit = True
                        self.state = self.states.exit
                    elif res['returncode'] == 2:
                        print(f"User {res['username']} not exist")
                        self.state = self.states.start1
                    elif res['returncode'] == 1:
                        print(f"User {res['username']} repeat logout")
                        self.state = self.states.start1
                elif res['id'] == 'SHT':
                    if res['returncode'] != 0:
                        print('Incorrect password')
                        self.state = self.states.start1
                    else:
                        print('Goodbye. Server shutting down')
                        self.exit = True
                        self.state = self.states.exit

    def send(self):
        tip_tmp = 'Enter one of the following commands: CRT, MSG, DLT, EDT, LST, RDT, UPD, DWN, RMV, XIT, SHT: '
        while True:
            try:
                req = dict()
                if self.state == self.states.wait0 or self.state == self.states.wait1:
                    pass
                elif self.state == self.states.start1:
                    req['username'], command = self.username, []
                    if self.currentStage != 1:
                        if self.needToSendFilename != '':
                            command.append('UPD')
                    else:
                        input_str = input(tip_tmp)
                        commandIdList = ['ATE', 'CRT', 'MSG', 'DLT', 'EDT', 'LST', 'RDT', 'UPD', 'DWN', 'RMV', 'XIT',
                                         'SHT']
                        split_rst = input_str.split()
                        rst = [split_rst[0]]
                        if rst[0] not in commandIdList:
                            if self.state != self.states.start0:
                                raise Exception()
                            else:
                                rst[0] = 'ATE'
                                rst += split_rst
                        elif rst[0] in ['MSG', 'EDT']:
                            rst.append(split_rst[1])
                            if rst[0] != 'MSG':
                                rst.append(split_rst[2])
                                rst.append(input_str.replace('EDT ' + split_rst[1] + ' ' + split_rst[2] + ' ', ''))
                            else:
                                rst.append(input_str.replace('MSG ' + split_rst[1] + ' ', ''))
                        else:
                            rst += split_rst[1:]
                        command = rst
                    if command[0] == 'CRT':
                        req['id'], req['stage'], req['threadtitle'] = 'CRT', 1, command[1]
                    elif command[0] == 'DLT':
                        req['id'], req['stage'], req['threadtitle'], req['messagenumber'] = 'DLT', 1, command[1], int(
                            command[2])
                    elif command[0] == 'EDT':
                        req['id'], req['stage'], req['threadtitle'], req['messagenumber'], req['message'] = 'EDT', 1, \
                                                                                                            command[
                                                                                                                1], int(
                            command[2]), command[3]
                    elif command[0] == 'MSG':
                        req['id'], req['stage'], req['threadtitle'], req['message'] = 'MSG', 1, command[1], command[2]
                    elif command[0] == 'LST' and len(command) == 1:
                        req['id'], req['stage'] = 'LST', 1
                    elif command[0] == 'LST' and len(command) != 1:
                        print('Incorrect syntax for LST')
                        continue
                    elif command[0] == 'RDT' and len(command) != 1:
                        req['id'], req['stage'], req['threadtitle'] = 'RDT', 1, command[1]
                    elif command[0] == 'RDT' and len(command) == 1:
                        print('Incorrect syntax for RDT')
                        continue
                    elif command[0] == 'DWN':
                        req['id'], req['stage'], req['threadtitle'], req['filename'] = 'DWN', 1, command[1], command[2]
                    elif command[0] == 'RMV':
                        req['id'], req['stage'], req['threadtitle'] = 'RMV', 1, command[1]
                    elif command[0] == 'UPD':
                        req['id'] = 'UPD'
                        if self.currentStage != 1:
                            req['stage'], req['threadtitle'], req[
                                'filename'] = 2, self.needToSendThreadtitle, self.needToSendFilename
                            with open(self.needToSendFilename, 'rb') as fp:
                                req['filedata'] = fp.read()
                            self.needToSendFilename, self.needToSendThreadtitle = '', ''
                        else:
                            req['stage'], req['threadtitle'], req['filename'] = 1, command[1], command[2]
                    elif command[0] == 'XIT':
                        req['id'], req['stage'] = 'XIT', 1
                    elif command[0] == 'SHT' and len(command) != 1:
                        req['id'], req['stage'], req['password'] = 'SHT', 1, command[1]
                    elif command[0] == 'SHT' and len(command) == 1:
                        print('Incorrect syntax for SHT')
                        continue
                    self.clientSocket.send(str(req).encode())
                    self.state = self.states.wait1
                elif self.state == self.states.start0:
                    req['id'] = 'ATE'
                    if self.currentStage == 1:
                        input_str = input('Enter username: ')
                        req['stage'], req['username'], self.username = 1, input_str, input_str
                    elif self.currentStage == 2:
                        req['username'] = self.username
                        if self.returnCode != 0:
                            input_str = input(f"Enter new password for {req['username']}: ")
                            req['stage'], req['newpassword'] = 2, input_str
                        else:
                            input_str = input('Enter password: ')
                            req['stage'], req['password'] = 2, input_str
                    self.clientSocket.send(str(req).encode())
                    self.state = self.states.wait0
                elif self.state == self.states.exit:
                    return
            except Exception as e:
                print('Invalid command')
                continue

    def start(self):
        recv_thread = threading.Thread(target=self.recv)
        recv_thread.setDaemon(True)
        recv_thread.start()
        send_thread = threading.Thread(target=self.send)
        send_thread.setDaemon(True)
        send_thread.start()
        while True:
            if self.exit:
                return


if __name__ == '__main__':
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client = Client(server_ip, server_port)
    client.start()
