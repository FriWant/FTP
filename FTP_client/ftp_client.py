import socket
import optparse

STATUS_CODE = {
    200: "Authentication passed",
    400: "Authentication failed"
}


class ClientHandler():

    def __init__(self):

        self.opt = optparse.OptionParser()

        self.opt.add_option("-s", "--server", dest="server")
        self.opt.add_option("-P", "--port", dest="port")
        self.opt.add_option("-u", "--username", dest="username")
        self.opt.add_option("-p", "--password", dest="password")

        self.options, self.args = self.opt.parse_args()
        self.verify_args(self.options, self.args)
        self.make_connection()

    def response(self):
        data = self.sock.recv(1024).decode("utf-8")
        data = json.loads(data)
        return data

    def verify_args(self, options, args):
        server=options.server
        port=int(options.port)
        username=options.username
        password=options.password
        if int(port)>0 and int(port)<65536:
            return True

    def make_connection(self):
        self.sock=socket.socket()
        self.sock.connect((self.options.server, int(self.options.port)))

    def interactive(self):
        self.authenticate()

    def authenticate(self):
        if self.options.username is None or self.options.password is None:
            username = input("username: ")
            password = input("password: ")
            return self.get_auth_result(username, password)
        return get_auth_result(self.options.username, self.options.password)

    def get_auth_result(self, username, pwd):
        
        data={
                "action": "auth",
                "username": username,
                "password": pwd
                }

        self.sock.send(json.dumps(data).encode("utf-8"))
        response=self.response()
        print("response: ", response["status_code"])
ch = ClientHandler()
ch.interactive()
