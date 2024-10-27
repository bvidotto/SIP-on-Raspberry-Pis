# -*- coding: utf-8 -*-
"""
File: Utilities.py
Author: Benoît Vidotto
Date: Q2/Q3 2021
"""


"""
This script, in conjunction with the python script Wizard.py, allows the menu in the Wizard file 
Wizard file to “talk” with the Raspberry. When requested 
this script retrieves information from the Raspberry and sends it back to the Wizard script.
To work, this script must be placed in the Twinkle installation folder.
In the “Wizard.py” and “Utilities.py” duo, Wizard is to be used on a Windows PC
and Utilities is to be placed in the Raspberries.
"""
import sys
import os

path = os.path.dirname(os.path.abspath(__file__)) + '/'

# if sys.version_info[0] < 3:
#     os.system('python3 ' + path +  __file__)
#     exit()


if sys.argv[1] =="getInfo":

    f = open(path + "user.cfg", "r")

    # Transform file content into a dictionnary
    dct = {}
    for x in f:
        if '=' in x:
            y = x.split('=')
            dct[y[0]]=y[1].replace('\n', '')
        else:
            dct[x] = ""
    print(dct['user_name'] + '\n' + dct['user_domain'] + '\n' + dct['auth_pass'])

elif sys.argv[1] =="EditSIPuser":
    f = open(path + "user.cfg", "r")

    # Transform file content into a dictionnary
    dct = {}
    for x in f:
        if '=' in x:
            y = x.split('=')
            dct[y[0]]=y[1]
        else:
            dct[x] = ""

    username_new = str(sys.argv[2])
    password_new = str(sys.argv[3])
    userdomain_new = str(sys.argv[4])
    #print('\n' + username_new + '\n' + password_new + '\n' + userdomain_new)

    #Edit the variables into the dictionnary
    dct['user_name']=username_new + '\n'
    dct['auth_name']=username_new + '\n'
    dct['user_display']=username_new + '\n'

    dct['user_domain']=userdomain_new + '\n'
    dct['outbound_proxy']=userdomain_new + '\n'
    dct['registrar']=userdomain_new + '\n'

    dct['auth_pass']=password_new + '\n'

    # Write back the dictionnary into a string
    l = ''
    for key, value in dct.items():
        if '# ' in key or key == '\n':
            l = l + '\n' + key
        else:
            l = l + key + '=' + value

    f.close()
    #Save the new string with the new settings in the file
    f = open(path + "user.cfg", "w")
    f.write(l)
    f.close()
    print('User settings edited successfully')

elif sys.argv[1] =="HDMI":
    f=open(path + 'HDMI.sh', 'rt')

    HDMI = f.read()
    #print(HDMI)
    f.close()

    f = open(path + 'HDMI.sh', 'wt')
    if HDMI == '':
        f.write('/usr/bin/tvservice -o')
        print('HDMI is disabled')
    else:
        f.write('')
        print('HDMI will be enabled on next boot')
    f.close()

elif sys.argv[1] == "HDMIinfo":
    f=open(path + 'HDMI.sh', 'rt')

    HDMI = f.read()
    #print(HDMI)
    f.close()

    print('1' if HDMI=='' else '0')
else:
    print('Error: Unknown argument. Available arguments are "getInfo", "EditSIPuser" and "HDMI".')
