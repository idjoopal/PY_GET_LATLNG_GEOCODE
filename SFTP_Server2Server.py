# Require packages
import os
import scp
import paramiko

target-server-ip-address = '10.xx.xx.xxx'
target-server-windows-username = 'username'
target-server-windows-password = 'password'

# If Your server on linux(Ubuntu, CentOS etc, something), file location will be looked like this
source-server-file-location = os.getcwd()+'/' + 'YOUR_FILE.csv'

# If Your server on Windows, file location will be looked like this
target-server-file-location = '/C:/Users/YOU/' + 'YOUR_FILE.csv'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('target-server-ip-address', username='target-server-windows-username', password='target-server-windows-password')

ftp_client=ssh_client.open_sftp()
ftp_client.put(source-server-file-location, target-server-file-location)
ftp_client.close()
ssh_client.close()
