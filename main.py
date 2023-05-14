import paramiko

host = "HOST"
puerto = 22
usuario = "USUARIO"
password = "PASSWORD"

comando = "ls"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, puerto, usuario, password)

stdin, stdout, stderr = ssh.exec_command(comando)
lineas = stdout.readlines()

print(lineas)
