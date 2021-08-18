import paramiko
import sys

class SSHConnect:


    def __init__(self,ip,port,username,password):
        self.ip = ip   #192.168.0.8
        self.port = port  #22
        self.username = username  #rajkumar
        self.password = password  #4122

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, self.port, self.username, self.password )

    def runCommand(self):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        outlines = stdout.readlines()
        resp = ''.join(outlines)
        return resp
        

if __name__ == "__main__":

    connection = SSHConnect("192.168.12.156", 22, "rajkumar", "4122")
    connection.connect()

    while True:
        cmd = input("Enter Command or Terminal Quit['Q']:")
        if cmd == "Q":
            sys.exit()

        print(connection.runCommand())


