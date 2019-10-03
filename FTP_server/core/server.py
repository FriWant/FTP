
import socketserver
import json
import configparser
from conf import settings


STATUS_CODE = {
    200: "Authentication passed",
    400: "Authentication failed"
}

class ServerHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("Ok")

        while 1:
            data = self.request.recv(1024).strip()
            data = json.loads(data.decode("utf-8"))

            if data.get("action"):
            
                if hasattr(self, data.get("action")):
                    func = getattr(self, data.get("action"))
                    func(**data)
                else:
                    print("Invalid cmd")
            else:
                print("Invalid cmd")

    

    def auth(self, **data):
        username=data["username"]
        password=data["password"]

        user=self.authenticate(username, password)
        if user:
            self.send_response(200)


        else:
            self.send_response(400)



    def send_response(self, state_code):
        response={"status_code": state_code}
        self.request.sendall(json.dumps(response).encode("utf-8"))
    def authenticate(self, user, pwd):
        cfg=configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)

        if user in cfg.sections():
            if cfg[user]["Password"] == pwd:
                self.user = user
                print("Passed authentication")
                return user
            else:
                return None
