import paramiko

class SSHConnect:

    def __init__(self,ip,port,username,password):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, self.port, self.username, self.password )

    def get_files(self,a):
        sftp_client = self.ssh.open_sftp()
        sftp_client.chdir("/var/log/")  #get logfiles servermachine to localmachine
        print(sftp_client.getcwd())
        sftp_client.get('syslog', f'./log/{a}.txt')
        sftp_client.close()
        self.ssh.close()
    
if __name__ == '__main__':
    connection = SSHConnect("192.168.12.156", 22, "rajkumar", "4122")
    connection.connect()
    connection.get_files('sample')

