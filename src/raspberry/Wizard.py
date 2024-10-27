# -*- coding: utf-8 -*-
"""
File: Wizard.py
Author: Benoît Vidotto
Date: Q2/Q3 2021
"""


"""
This script, in conjunction with the python script Utilities.py, enables you to use 
Raspberrys remotely, without using PuTTY or any other software, and limiting access to the 
functionality available on the Raspberry for this use case.
This script is actually a menu that allows anyone who wishes and has the right
(username and password settings online 34) to modify the SIP phone's settings.
of the SIP phone.
In the “Wizard.py” and “Utilities.py” duo, Wizard is to be used on a Windows PC
and Utilities is to be placed in the Raspberries.
"""
import paramiko
from getpass import getpass
import os

"""si une erreur apparait, la dizaine de lignes suivantes permet de voir l'erreur 
dans le fichier .exe sans qu'il quitte prématurément."""
def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    end = input("Do you wish to restart the script ? [y/n]")
    if end == "y" or end == "Y":
        os.execv(sys.argv[0], sys.argv)    
    else:
        sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit


realUsername = 'pi'
realPassword = 'raspberry'
while True:
    username = input('Login as: ')
    password = getpass('Password: ')
    if password != realPassword or username != realUsername:
        print('Access Denied')
        continue
    else:
        break
    
username= 'pi'
password='raspberry'
# server = '10.128.100.103'

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(server, username=username, password=password)

def SSHconnect(server):
    print('\nConnecting to ' + server + ' ...')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, username=username, password=password)
    except TimeoutError:
        print('    ' + "Timeout expired: Can't find server at address " + server + "\n")
        ssh = 'timeout'
    return ssh

def SSHcmd(cmd):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('python /home/pi/.twinkle/Utilities.py ' + cmd)
    stdout = ssh_stdout.readlines() #this line is necessary as the variable is emptied after one use
    if len(stdout)==0:
        print("Error: " + ssh_stderr.readlines()[0])
    else:
        print('\n' + stdout[0])
    return

def inputAction(nbrActions):
    while True:
        try:
            choice = int(input('\nSelect action: '))
            if 1 <= choice <= nbrActions:
                break
        except ValueError:
            pass
    return choice
    

while True:
    print('\n=== Raspberry SIPphone Utility ===\n\nSelect action by number: \n\n    1. Get current SIP settings of multiple Raspberries\n    2. Edit Raspberry settings\n    3. Enable/disable HDMI\n    4. Reboot Rapsberry\n    5. Exit')
    
    choice = inputAction(5)
        
    if choice == 1:
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
        cmd_to_execute='python /home/pi/.twinkle/Utilities.py getInfo'
        print('\n')
        for server in raspberries:
            ssh = SSHconnect(server)
            
            if ssh == 'timeout':
                continue
            
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
            
            stdout = ssh_stdout.readlines() #this line is necessary as the variable is emptied after one use
            if len(stdout)==0:
                display= "Error: " + ssh_stderr.readlines()[0]
            else:
                display = '    SIP address : ' + stdout[0].replace('\n', '') + '@' + stdout[1].replace('\n', '')
            print(display) 
            ssh.close()
    
    elif choice == 2:
        server = input('Enter the IP address of the selected Raspberry: ')
        #server = '10.128.100.103'
        #if ssh.get_transport().getpeername()[0] != server:
        ssh = SSHconnect(server)
        # ssh = paramiko.SSHClient()
        # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.connect(server, username=username, password=password)
        
        if ssh == 'timeout':
            continue
        
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('python /home/pi/.twinkle/Utilities.py getInfo')
        stdout = ssh_stdout.readlines()
        
        username_old = stdout[0].replace('\n', '')
        userdomain_old = stdout[1].replace('\n', '')
        password_old = stdout[2].replace('\n', '')
        
        while True:
            print('\n=== EDIT USER/SIP SETTINGS ===\n\nCurrent settings: \n\n    Username: ' + username_old + '\n    User domain: ' + userdomain_old + '\n\nSelect action by number: \n\n    1. Edit username\n    2. Edit user domain\n    3. Exit and save changes\n    4. Exit and discard changes')

            subchoice = inputAction(4)            
        
            if subchoice == 1:
                print('\nCurrent user_name: ' +  username_old)
                username_new=input('\nEnter new user_name: ')
                if (username_new == ''):
                    username_new = username_old
                    continue
                username_old = username_new
        
                #password_new = input('Enter new password: ')
                password_new = ''
                while(password_new == ''):
                    password_new = getpass('Enter new password: ')
        
            elif subchoice == 2:
                print('\nCurrent user_domain: ' + userdomain_old)
                userdomain_new=input('\nEnter new user_domain: ')
                if userdomain_new == '':
                    userdomain_new = userdomain_old
                    continue
                else:
                    userdomain_old = userdomain_new
                    
            elif subchoice == 3:
                username_new = username_new if 'username_new' in globals() else username_old
                userdomain_new = userdomain_new if 'userdomain_new' in globals() else userdomain_old
                password_new = password_new if 'password_new' in globals()else password_old
                print("\nNew settings: \n\n    Username: " + username_new + "\n    User domain: " + userdomain_new)
                break
            elif subchoice == 4:
                stop=input('Exit and discard changes ? [y/n]')
                if stop == "y" or stop == "Y":
                    break
                
        if subchoice==4:
            pass
        else:
            SSHcmd('EditSIPuser ' + username_new + ' ' + password_new  + ' ' + userdomain_new)
            print('\nFor the changes to be applied, the board needs to be rebooted.')
            reboot = input('Do you want to reboot now ? [y/n]')
            if reboot == 'y' or reboot == 'Y':
                ssh.exec_command('sudo reboot')
            
            # ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('python /home/pi/.twinkle/Utilities.py EditSIPuser ' + username_new + ' ' + password_new  + ' ' + userdomain_new)
            # stdout = ssh_stdout.readlines() #this line is necessary as the variable is emptied after one use
            # if len(stdout)==0:
            #     print("Error: " + ssh_stderr.readlines()[0])
            # else:
            #     print('\n' + stdout[0])
                
    elif choice == 3:
        server = input('Enter the IP address of the selected Raspberry: ')
        #server = '10.128.100.103'
        #if ssh.get_transport().getpeername()[0] != server:
        ssh = SSHconnect(server)
        
        if ssh == 'timeout':
            continue
        
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('python /home/pi/.twinkle/Utilities.py HDMIinfo')

        if ssh_stdout.readlines()[0].replace('\n', '') == '0':
            print('\nThe HDMI port is disabled.')
            subchoice = input('Do you want to enable it ?[y/n]')
        else:
            print('\nThe HDMI port is enabled.')
            subchoice = input('Do you want to disable it ? [y/n]')

       	if subchoice == 'y' or subchoice == 'Y':
            SSHcmd('HDMI')
               
    elif choice == 4:
        server = input('Enter the IP address of the selected Raspberry: ')
        ssh = SSHconnect(server)
        if ssh == 'timeout':
            continue
        reboot = input('Do you want to reboot now ? [y/n]')
        if reboot == 'y' or reboot == 'Y':
            ssh.exec_command('sudo reboot')
        
    elif choice == 5:
        break