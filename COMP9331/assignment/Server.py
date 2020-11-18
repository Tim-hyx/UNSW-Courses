import threading, socket, sys, os


class File:
    type = 'file'
    fileName, fileUploader = '', ''

    def __init__(self, uploader, filename):
        self.fileName, self.fileUploader = filename, uploader

    def toString(self):
        return self.fileUploader + ' uploaded ' + self.fileName


class Message:
    type = 'message'
    messageAuthor, messageContent = '', ''

    def __init__(self, message_author, message_content):
        self.messageAuthor, self.messageContent = message_author, message_content

    def toString(self):
        return self.messageAuthor + ': ' + self.messageContent


class Thread:
    threadAuthor, threadTitle = '', ''

    def __init__(self, thread_title, thread_author):
        self.threadTitle, self.threadAuthor = thread_title, thread_author
        self.threadMessageList, self.threadFileList, self.threadContent = [], [], []
        with open(self.threadTitle, 'w') as fp:
            fp.write(self.threadAuthor)
            fp.write('\n')

    def postMessage(self, message, username):
        msg = Message(username, message)
        self.threadMessageList.append(msg)
        self.threadContent.append(msg)
        self.writeToFile()
        return 0

    def readThread(self, username):
        content = ''
        i = 1
        for line in self.threadContent:
            if line.type == 'message':
                content += str(i) + ' '
                i += 1
            content += line.toString() + '\n'
        return 0, content

    def deleteMessage(self, message_number, username):
        if message_number > len(self.threadMessageList) or message_number < 1:
            return 2
        else:
            if self.threadMessageList[message_number - 1].messageAuthor != username:
                return 1
            else:
                self.threadContent.remove(self.threadMessageList[message_number - 1])
                self.threadMessageList.remove(self.threadMessageList[message_number - 1])
                self.writeToFile()
                return 0

    def editMessage(self, message_number, message, username):
        if message_number > len(self.threadMessageList) or message_number < 1:
            return 2
        else:
            if self.threadMessageList[message_number - 1].messageAuthor != username:
                return 1
            else:
                self.threadMessageList[message_number - 1].messageContent = message
                self.writeToFile()
                return 0

    def uploadFile_send(self, username, thread_title, file_name, file_data):
        file = File(username, file_name)
        self.threadFileList.append(file)
        self.threadContent.append(file)
        self.writeToFile()
        with open(thread_title + '-' + file_name, 'wb') as fp:
            fp.write(file_data)
        return 0

    def uploadFile_confirm(self, username, filename):
        for file in self.threadFileList:
            if file.fileName == filename:
                return 1
        return 0

    def downloadFile(self, username, thread_title, filename):
        for file in self.threadFileList:
            if file.fileName == filename:
                with open(thread_title + '-' + filename, 'rb') as fp:
                    return 0, fp.read()
        return 1, None

    def writeToFile(self):
        with open(self.threadTitle, 'w') as fp:
            fp.write(self.threadAuthor)
            fp.write('\n')
            i = 1
            for line in self.threadContent:
                if line.type != 'message':
                    fp.write(line.toString())
                    fp.write('\n')
                else:
                    fp.write(str(i) + ' ')
                    fp.write(line.toString())
                    fp.write('\n')
                    i += 1
        return


class ThreadManager:
    threadList = True

    def __init__(self):
        self.threadList = dict()

    def createThread(self, thread_title, thread_author):
        if thread_title in self.threadList:
            return 1
        else:
            self.threadList[thread_title] = Thread(thread_title, thread_author)
            return 0

    def listThreads(self, username):
        thread_titles = self.threadList.keys()
        str = ''
        for thread in thread_titles:
            str += thread + '\n'
        return 0, str

    def removeThread(self, thread_title, username):
        if thread_title not in self.threadList:
            return 1
        else:
            if self.threadList[thread_title].threadAuthor != username:
                return 2
            else:
                del self.threadList[thread_title]
                os.remove(thread_title)
                return 0

    def deleteMessage(self, thread_title, message_number, username):
        if thread_title not in self.threadList:
            return 3
        else:
            return self.threadList[thread_title].deleteMessage(message_number, username)

    def postMessage(self, thread_title, message, username):
        if thread_title not in self.threadList:
            return 1
        else:
            return self.threadList[thread_title].postMessage(message, username)

    def readThread(self, thread_title, username):
        if thread_title not in self.threadList:
            return 1, ''
        else:
            return self.threadList[thread_title].readThread(username)

    def editMessage(self, thread_title, message_number, message, username):
        if thread_title not in self.threadList:
            return 3
        else:
            return self.threadList[thread_title].editMessage(message_number, message, username)

    def uploadFile_confirm(self, thread_title, username, filename):
        if thread_title not in self.threadList:
            return 2
        else:
            return self.threadList[thread_title].uploadFile_confirm(username, filename)

    def downloadFile(self, username, thread_title, file_name):
        if thread_title not in self.threadList:
            return 2, None
        else:
            return self.threadList[thread_title].downloadFile(username, thread_title, file_name)

    def uploadFile_send(self, username, thread_title, file_name, file_data):
        if thread_title not in self.threadList:
            return 2
        else:
            return self.threadList[thread_title].uploadFile_send(username, thread_title, file_name, file_data)

    def writeToFile(self):
        for thread in self.threadList:
            thread.writeToFile()


class User:
    username, password = '', ''

    def __init__(self, username, password):
        self.username, self.password = username, password
        self.login, self.client = False, None

    def toString(self):
        return self.username + ' ' + self.password


class UserManger:
    userFileName = ''
    userList = dict()

    def __init__(self, file_name):
        self.userList = dict()
        self.userFileName = file_name
        if not os.path.isfile(self.userFileName):
            pass
        else:
            with open(self.userFileName, 'r') as fp:
                for line in fp.readlines():
                    line = line.split('\n')
                    split_rst = line[0].split(' ')
                    if len(split_rst) != 2:
                        exit()
                    else:
                        username, password = split_rst[0], split_rst[1]
                        self.userList[username] = User(username, password)

    def createNewUser(self, username, password, client):
        self.userList[username] = User(username, password)
        self.userLogin(username, password, client)
        with open(self.userFileName, 'a') as fp:
            fp.write('\n')
            fp.write(self.userList[username].toString())
        return 0

    def userLogin(self, username, password, client):
        if username in self.userList:
            user = self.userList[username]
            if not user.login:
                if user.password != password:
                    return 2
                else:
                    user.login, user.client = True, client
                    return 0
            else:
                return 1
        return 3

    def findUserByClient(self, client):
        for user in self.userList:
            if self.userList[user].client == client:
                return self.userList[user]
        return None

    def userLogout(self, username):
        if username in self.userList:
            user = self.userList[username]
            if not user.login:
                return 1
            else:
                user.login = False
                return 0
        return 2

    def userClientClose(self, client):
        user = self.findUserByClient(client)
        if user is not None:
            self.userLogout(user.username)


class Server:
    serverPort, serverAddress, serverAdminPassword = 0, '127.0.0.1', ''
    serverSocket, userManger, threadManger, exit = None, None, None, False
    clientPool, threadPool = [], []

    def __init__(self, serverPort, adminPassword):
        self.exit, self.serverPort, self.serverAdminPassword = False, serverPort, adminPassword
        try:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSocket.bind((self.serverAddress, self.serverPort))
        except:
            exit()
        self.userManger = UserManger('credentials.txt')
        self.threadManger = ThreadManager()

    def shutdown(self, password):
        if self.serverAdminPassword != password:
            return 1
        else:
            users = self.userManger.userList.values()
            for user in users:
                if user.login:
                    self.userManger.userLogout(user.username)
            return 0

    def sendToClient(self, msg, client):
        client.sendall(str(msg).encode())

    def recvFromClient(self, client):
        username = ''
        isContinue = True
        while isContinue:
            try:
                req = eval(client.recv(999999).decode())
            except ConnectionError as e:
                self.userManger.userClientClose(client)
                self.clientPool.remove(client)
                client.close()
                return
            else:
                res = dict()
                if req['id'] != 'ATE' and req['id'] != 'XIT':
                    print(f"{req['username']} issued {req['id']} command")
                # login or create new user
                if req['id'] == 'ATE':
                    res['id'] = 'ATE'
                    if req['stage'] == 1:
                        res['stage'], username = 1, req['username']
                        if username not in self.userManger.userList:
                            res['returncode'] = 1
                        else:
                            res['returncode'] = 0
                            if self.userManger.userList[username].login:
                                res['returncode'] = 2
                                print(f"{req['username']} has already logged in")
                    elif req['stage'] == 2:
                        res['stage'], username = 2, req['username']
                        if 'newpassword' not in req:
                            password = req['password']
                            return_code = self.userManger.userLogin(username, password, client)
                            if return_code != 0:
                                print('Incorrect password')
                            else:
                                print(f"{req['username']} successful login")
                            res['returncode'] = return_code
                        else:
                            newpassword = req['newpassword']
                            self.userManger.createNewUser(username, newpassword, client)
                            res['returncode'] = 0
                            print('New user')
                            print(f"{req['username']} successfully logged in")
                # create thread
                elif req['id'] == 'CRT':
                    res['id'], res['stage'], username, thread_title = 'CRT', 1, req['username'], req['threadtitle']
                    return_code = self.threadManger.createThread(thread_title, username)
                    res['returncode'], res['threadtitle'] = return_code, thread_title
                    if return_code != 0:
                        print(f'Thread {thread_title} exists')
                    else:
                        print(f'Thread {thread_title} created')
                # post message
                elif req['id'] == 'MSG':
                    res['id'], res['stage'], username, thread_title, message = 'MSG', 1, req['username'], req[
                        'threadtitle'], req['message']
                    return_code = self.threadManger.postMessage(thread_title, message, username)
                    res['returncode'], res['threadtitle'] = return_code, thread_title
                    if return_code != 0:
                        print(f'Thread {thread_title} not existed')
                    else:
                        print(f'Message posted to {thread_title} thread')
                # read thread
                elif req['id'] == 'RDT':
                    res['id'], res['stage'], username, thread_title = 'RDT', 1, req['username'], req['threadtitle']
                    res['threadtitle'] = thread_title
                    res['returncode'], res['content'] = self.threadManger.readThread(thread_title, username)
                    if res['returncode'] != 0:
                        print('Incorrect thread specified')
                    else:
                        print(f"Thread {res['threadtitle']} read")
                # Delete message
                elif req['id'] == 'DLT':
                    res['id'], res['stage'], username, thread_title, message_number = 'DLT', 1, req['username'], req[
                        'threadtitle'], req['messagenumber']
                    return_code = self.threadManger.deleteMessage(thread_title, message_number, username)
                    res['returncode'], res['threadtitle'] = return_code, thread_title
                    if res['returncode'] == 0:
                        print('Message has been deleted.')
                    elif res['returncode'] == 3:
                        print(f"Thread {res['threadtitle']} not exists")
                    elif res['returncode'] == 2:
                        print('Message number not exist')
                    elif res['returncode'] == 1:
                        print('Message cannot be deleted')
                # list threads
                elif req['id'] == 'LST':
                    res['id'], res['stage'], username = 'LST', 1, req['username']
                    res['returncode'], res['content'] = self.threadManger.listThreads(username)
                # edit message
                elif req['id'] == 'EDT':
                    res['id'], res['stage'], res[
                        'threadtitle'], username, thread_title, message_number, message = 'EDT', 1, req['threadtitle'], \
                                                                                          req['username'], req[
                                                                                              'threadtitle'], req[
                                                                                              'messagenumber'], req[
                                                                                              'message']
                    res['returncode'] = self.threadManger.editMessage(thread_title, message_number, message, username)
                    if res['returncode'] == 0:
                        print('Message has been edited')
                    elif res['returncode'] == 2:
                        print('Message number not exist')
                    elif res['returncode'] == 1:
                        print('Message cannot be edited')
                # remove thread
                elif req['id'] == 'RMV':
                    res['id'], res['stage'], username, thread_title, res['threadtitle'] = 'RMV', 1, req['username'], \
                                                                                          req['threadtitle'], req[
                                                                                              'threadtitle']
                    res['returncode'] = self.threadManger.removeThread(thread_title, username)
                    if res['returncode'] == 0:
                        print(f"Thread {res['threadtitle']} removed")
                    elif res['returncode'] == 2:
                        print(f"Thread {res['threadtitle']} cannot be removed")
                    elif res['returncode'] == 1:
                        print(f"Thread {res['threadtitle']} not exists")
                # upload file
                elif req['id'] == 'UPD':
                    res['id'], username, thread_title, file_name = 'UPD', req['username'], req['threadtitle'], req[
                        'filename']
                    res['username'], res['filename'], res['threadtitle'] = username, file_name, thread_title
                    if req['stage'] == 1:
                        res['stage'], res['threadtitle'], res['filename'] = 1, req['threadtitle'], req['filename']
                        res['returncode'] = self.threadManger.uploadFile_confirm(thread_title, username, file_name)
                        if res['filename'] == 1:
                            print('File exist.')
                        else:
                            print('Thread not exist.')
                    elif req['stage'] == 2:
                        res['stage'], file_data = 2, req['filedata']
                        res['returncode'] = self.threadManger.uploadFile_send(username, thread_title, file_name,
                                                                              file_data)
                        print(f"{res['username']} uploaded file {res['filename']} to {res['threadtitle']} thread")
                # download file
                elif req['id'] == 'DWN':
                    res['id'], username, thread_title, file_name = 'DWN', req['username'], req['threadtitle'], req[
                        'filename']
                    res['threadtitle'], res['filename'] = thread_title, file_name
                    res['returncode'], res['filedata'] = self.threadManger.downloadFile(username, thread_title,
                                                                                        file_name)
                    if res['returncode'] == 0:
                        print(f"{res['filename']} downloaded from Thread {res['threadtitle']}")
                    elif res['returncode'] == 2:
                        print(f"Thread {res['threadtitle']} not exists")
                    elif res['returncode'] == 1:
                        print(f"{res['filename']} does not exist in Thread {res['threadtitle']}")
                # exit
                elif req['id'] == 'XIT':
                    res['id'], username = 'XIT', req['username']
                    res['returncode'] = self.userManger.userLogout(username)
                    res['username'] = username
                    self.clientPool.remove(client)
                    isContinue = False
                    if res['returncode'] == 0:
                        print(f"{res['username']} exited")
                        print('Waiting for clients')
                    elif res['returncode'] == 2:
                        print(f"User {res['username']} not exists")
                    elif res['returncode'] == 1:
                        print(f"User {res['username']} repeat logout")
                # shut down
                elif req['id'] == 'SHT':
                    res['id'], password = 'SHT', req['password']
                    res['returncode'] = self.shutdown(password)
                    if res['returncode'] != 0:
                        print('Incorrect password')
                    else:
                        print('Server shutting down')
                        for c in self.clientPool:
                            if c != client:
                                c.sendall(str(res).encode())
                        self.exit = True
                self.sendToClient(res, client)

    def acceptLoop(self):
        self.serverSocket.listen(20)
        print('Waiting for clients')
        while True:
            client, _ = self.serverSocket.accept()
            print('Client connected.')
            self.clientPool.append(client)
            thread = threading.Thread(target=self.recvFromClient, args=(client,))
            thread.setDaemon(True)
            thread.start()

    def start(self):
        thread = threading.Thread(target=self.acceptLoop)
        thread.setDaemon(True)
        thread.start()
        while True:
            if self.exit:
                return


if __name__ == '__main__':
    server_port = int(sys.argv[1])
    admin_password = sys.argv[2]
    server = Server(server_port, admin_password)
    server.start()
