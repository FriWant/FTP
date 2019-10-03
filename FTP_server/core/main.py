import optparse
import socketserver
from conf import settings
from core import server

class ArgvHandler():

    def __init__(self):
        self.opt = optparse.OptionParser()

        self.opt.add_option("-s", "--server", dest="server")
        self.opt.add_option("-P", "--port", dest="port")

        options, args = self.opt.parse_args()
        
        self.verify_args(options, args)

    def verify_args(self, options, args):
        cmd = args[0]

        if hasattr(self, cmd):
            func = getattr(self, cmd)
            func()

    def start(self):
        print("working...")
        s = socketserver.ThreadingTCPServer((settings.IP, settings.PORT), server.ServerHandler)    
        s.serve_forever()

    def help(self):
        pass

