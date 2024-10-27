"""
File: getSIPusers.py
Author: Benoît Vidotto
Date: Q2/Q3 2021
"""


import paramiko
import os
nbr = int(input('How many raspberries ? '))

badress=''
if nbr > 1:
    badress = input('Enter base IP adress (e.g. "192.168.0."): ')
    
raspberries = []
for i in range(nbr):
    tmp = input("Enter IP address of Raspberry: " + badress) 
    raspberries.append(badress + tmp)

username= 'pi'
password='raspberry'
cmd_to_execute='python /home/pi/.twinkle/getSIPuser.py'
print('\n')
for server in raspberries:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, username=username, password=password)
    except TimeoutError:
        print(server + '\n    ' + "Timeout expired: Can't find server at address " + server + "\n")
        continue
    
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
    
    stdout = ssh_stdout.readlines() #this line is necessary as the variable is emptied after one use
    if len(stdout)==0:
        display= "Error: " + ssh_stderr.readlines()[0]
    else:
        display = stdout[0]
    print(server + '\n    ' + display)

os.system('pause')