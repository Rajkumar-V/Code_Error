

import paramiko

ip='192.168.0.8'
port=22
username='rajkumar'
password='4122'
 

#Connect linux machine
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip, port, username, password)


#Get_files
sftp_client = ssh.open_sftp()

#sftp_client.chdir("/var/log/")  #get directory servermachine to localmachine
#print(sftp_client.getcwd())
#sftp_client.get('syslog','syslog.txt')  

sftp_client.put("get_logfiles.py", '/home/rajkumar/get_logfiles.py') #Transfer file to localmachine to servermachine

sftp_client.close()
ssh.close()



    

    

