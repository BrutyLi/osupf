import paramiko,sys
# hostname='192.168.2.54'
# username='root'
# password='yixinkeji'
# paramiko.util.log_to_file('syslogin.log')
# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname=hostname,username=username,password=password)
# stdin,stdout,stderr=ssh.exec_command('free -m')
# print(stdout.readlines())
# ssh.close()

def cmdline(ip,user,password,cmd):
    '''cmdline('192.168.2.54','root','yixinkeji','ifconfig')'''
    outstr=''
    paramiko.util.log_to_file('syslogin.log')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=user, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    for line in stdout.readlines():
        outstr+=str(line) + '\n'
    ssh.close()
    return outstr
