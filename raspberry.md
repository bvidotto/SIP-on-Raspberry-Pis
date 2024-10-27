# Raspberry Pi Installation steps 


## Configure SD Card

#### Raspberry imager

Follow this
[<u>tutorial</u>](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2).

#### Enable ssh

Once the card is activated, 2 partitions will be created on the card. In
the partition called `boot,` you need to create a file called `ssh.`
This file must not have an extension.

## Controlling the Raspberry

#### Connectivity

The Raspberry will be controlled using an SSH client, for example PuTTY.
To do this, connect the Raspberry to a power supply via its port
microUSB/USB Type C, and an Ethernet cable to the corresponding port.
The Ethernet cable can be connected either to a network on which the PC
required for control, either directly to the said PC.

#### Software

If the Raspberry is connected directly to the PC via Ethernet cable: On
the PC that will control the Raspberry, open PuTTY. In PuTTY, the Host
name should be `raspberrypi.local` and port `22`. The connection can
then be opened.

If the Raspberry is connected via network: use an IPScanner to find the
address of the Raspberry card. Then enter this address in Putty.

## Getting rid of the repeating audio message

When there is no connection to the HDMI connector, the Raspberry
broadcasts a message at regular intervals to activate the screen reader.
To disable it, run this command: `sudo mv /usr/share/piwiz/srprompt.wav
/usr/share/piwiz/srprompt.wav.bak.`

## Install Twinkle

sudo apt-get install twinkle

An internet connection is required to run this command. folder where
Twinkle configuration files are located is `/home/pi/.twinkle`

### Configure the .cfg file

The file name is the \*\*user\*\* name that will be set in the GUI
Twinkle. For simplicity, the file name will therefore be the same as the
name username (user_name) in the configuration file. Write to the
\*\*user\*\*.cfg file which is in the box below. Do not are required as
user_name and user_domain for creating a very basic user (not our case
here). To work with the Company Asterisk server, UiD must be 500X or
600X and the sip.foo.bar should be 10.128.100.61 (local Asterisk server
address). The command to access the \*\*user\*\*.cfg file is *sudo nano
/.twinkle/\*\*user\*\*.cfg*

    user_name=**UiD**
    user_domain=**sip.foo.bar**
    user_display=**Your Name**
    user_organization=
    auth_realm=
    auth_name=**UiD**
    auth_pass=**Password**

    # SIP SERVER
    outbound_proxy=**sip.foo.bar**
    all_requests_to_proxy=no
    registrar=**sip.foo.bar**
    register_at_startup=yes
    registration_time=3600

    #RTP AUDIO
    codecs=g711a,g711u,gsm
    ptime=20
    dtmf_payload_type=101
    dtmf_duration=100
    dtmf_pause=40
    dtmf_volume=10

    # SIP PROTOCOL
    hold_variant=rfc3264
    check_max_forwards=no
    allow_missing_contact_reg=yes
    registration_time_in_contact=yes
    compact_headers=no
    use_domain_in_contact=yes
    allow_redirection=no
    ask_user_to_redirect=yes
    max_redirections=5
    ext_100rel=supported
    referee_hold=no
    referrer_hold=yes
    allow_refer=yes
    ask_user_to_refer=yes
    auto_refresh_refer_sub=no

    # NAT
    nat_public_ip=
    #stun_server=**sip.foo.bar**:10000

    # TIMERS
    timer_noanswer=30
    timer_nat_keepalive=30

    # ADDRESS FORMAT
    display_useronly_phone=yes
    numerical_user_is_phone=no

    #RING TONES
    ringtone_file=
    ringback_file=

    # SCRIPTS
    script_incoming_call=

### Allow auto-answer

For twinkle to automatically pick up the call it receives, you must
launch twinkle via the command line using `twinkle -c`, then run the
command `auto_answer -a` on to enable auto-answer for the active user.
To choose the user, run the command twinkle -c -f \*\*user\*\*.cfg
replacing \*\*user\*\* with the user desired.

### Start Twinkle when turning on the Raspberry

#### Set default user when starting twinkle

Edit the twinkle.sys file using the `sudo nano command
/home/pi/.twinkle/twinkle.sys`. In this file, below the line `\#
Startup`, add `start_user_profile=` followed by the user name defined in
the previous step according to the name of the corresponding file. For
example, if the file created in the previous step is 6005.cfg, the line
to add in twinkle.sys will then be `start_user_profile=6005`.

#### Create the startup.py file in /home/pi/.twinkle

Use the command `sudo nano /home/pi/.twinkle/startup.py` to access
startup.py:

The content to put in it is as follows:

    import os
    os.system(`twinkle')

#### Enable autostart and create the twinkle.desktop file

Below are the commands to use to access the twinkle.desktop file.

    mkdir /home/pi/.config/autostart
    nano /home/pi/.config/autostart/twinkle.desktop

The contents of the twinkle.desktop file are as follows:

    [Desktop Entry]
    Type=Application
    Name=Twinkle
    Exec=/usr/bin/python3 /home/pi/.twinkle/startup.py

#### Enable desktop autologin in raspi-config

sudo raspi-config

In raspi-config, navigate to `1 System Options \> S5 Boot/Auto Login \>
B4 Desktop Autologin`, enable auto-login according to what is displayed
on the screen, press finish in the main menu and accept the reboot.

Twinkle does not accept to be used via command line in the background
(auto deregistering of the SIPphone). Thus, among the possibilities of
Starting a program when the Raspberry Autostart starts is the most
appropriate because it allows you to launch the Twinkle GUI after the
raspberry desktop graphical environment is launched, which explains why
it is necessary to enable autologin on the desktop.

#### Disable HDMI port (optional)

The Raspberry desktop being in autologin, the entirety of the Raspberry
is accessible by anyone who connects a display to the HDMI port. So,
from a security point of view, it may be necessary to Disable the HDMI
port. Disabling the HDMI port also helps prevent inefficient use of
energy.

The command to disable the HDMI port is `/usr/bin/tvservice -o`. For To
re-enable the HDMI port, the command is `/usr/bin/tvservice -p`. For the
HDMI port is always disabled every time the card is turned on, it just
add the line `/usr/bin/tvservice -o` in rc.local using from `sudo nano
/etc/rc.local`.

HDMI.py and HDMI.sh can also be used, by putting bash
`/home/pi/.twinkle/HDMI.sh` in the rc.local file (Command: `sudo nano
/etc/rc.local`).

### Menu to modify user settings

Copy the files ‘UserEditor.py’ and ‘UserEditor.sh’ into
`/home/pi/.twinkle`. For the UserEditor to be displayed at the cmd login
of the map, add the line bash `/home/pi/.twinkle/UserEditor.sh` in `sudo
nano /etc/bash.bashrc`.

# Creating commands to facilitate access to UserEditor/HDMI menus

Follow the instructions in this
[<u>tutorial</u>](https://www.raspberrypi.org/forums/viewtopic.php?t=44362).

In bash.bashrc, the instructions to add are `printf
’\\n=======================\\n Instructions \\n\\nType \\"HDMI\\" to
enable/disable the HDMI port\\nType \\"UserEditor\\" to change user/SIP
settings\\n\\n=======================\\n’`.

# pjsip.conf

This appendix explains the different options for creating a user on
Asterisk using explanations provided in the pjsip.conf file in the
<a href="#tab:pjsip" data-reference-type="ref"
data-reference="tab:pjsip">following table</a>.

<div class="longtable">

 
| pjsip.conf         | Comments                                             |
|---------------------------|------------------------------------------------------|
| ;===TRANSPORT             |                                                      |
| {[}transport-udp{]}       |                                                      |
| type=transport            |                                                      |
| protocol=udp              |                                                      |
| bind=0.0.0.0              | Defines an IPV4 address                              |
| ;===SOFTPHONE TEMPLATE    | Simple comment for readibility                       |
|                           |                                                      |
| {[}ipfone{]}(!)           | Declaration of the template ipfone                   |
| type=endpoint             | All ipfone are endpoints from a                      |
|                           | architecture (proxy). An endpoint is                 |
|                           | essentially a profile for the configuration of a SIP |
|                           | endpoint such as a phone or remote server.           |
| allow=!all,ulaw           | Audio/telephony codecs to allow (here G.711 µ-law)   |
|                           | Allow= !all is the equivalent of disallow=all.       |
| context=from-internal     | Dialplan context for inbound sessions                |
| transport=transport-udp   | Definition of the protocol defined                   |
|                           | in the associated section above                      |
| direct\_media=no          | Determines whether media may flow directly           |
|                           | between endpoints.                                   |
| send\_pai=yes             | Send the P-Asserted-Identity header                  |
| refer\_blind\_progress=no | Whether to notify all the progress details           |
|                           | on blind transfer                                    |
| rtp\_timeout=2            | Delay without RTP to consider channel as dead        |
|                           |                                                      |
| {[}auth{]}(!)             | Holds the options and credentials related to         |
|                           | inbound or outbound authentication                   |
| type=auth                 |                                                      |
| auth\_type=userpass       | Set to userpass to read password. Other option is    |
|                           | md5                                                  |
| {[}aor{]}(!)              | Tells Asterisk where an endpoint can be contacted.   |
|                           | Without it, the endpoint can't be contacted          |
| type=aor                  |                                                      |
| max\_contacts=3           | Max number of contacts that can bind to an AoR       |
| remove\_existing=yes      | New contacts replace existing ones.                  |
| ;===EXTENSION 6001        |                                                      |
|                           |                                                      |
| {[}6001{]}(ipfone)        | Declaration of the user 6001 based                   |
|                           | on the ipfone template                               |
| outbound\_auth=6001       | Authentication object used for outbound requests     |
| auth=6001                 | Refers to auth section below                         |
| aors=6001                 | AoR(s) to be used with the endpoint (refers to       |
|                           | section below)                                       |
| allow\_transfer=yes       | Determines whether SIP REFER transfers               |
|                           | are allowed for this endpoint                        |
| context = from-internal   |                                                      |
| {[}6001{]}(aor)           |                                                      |
| {[}6001{]} (auth)         |                                                      |
| type=auth                 |                                                      |
| auth\_type=userpass       |                                                      |
| password=6001             |                                                      |
| username=6001             |                                                      |
| ;nat=yes                  |                                                      |

  

</div>
