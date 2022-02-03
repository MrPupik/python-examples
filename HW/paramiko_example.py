import paramiko
from secret import my_secret_password

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("0.0.0.0", username="itay", password=my_secret_password)
stdin, stdout, stderr = ssh.exec_command("docker ps")
print(stdout.readlines())
