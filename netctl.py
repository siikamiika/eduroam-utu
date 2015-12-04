#!/usr/bin/env python3

from getpass import getpass
import os

PATH = '/etc/netctl/eduroam'
TEMPLATE = \
"""Description='eduroam'
Interface={interface}
Connection=wireless
Security=wpa-configsection
IP=dhcp
TimeoutWPA=10
WPAConfigSection=(
    'ssid="eduroam"'
    'scan_ssid=0'
    'priority=0'
    'mode=0'
    'proto=RSN'
    'key_mgmt=WPA-EAP'
    'auth_alg=OPEN'
    'pairwise=CCMP'
    'group=CCMP'
    'eap=PEAP'
    'identity="{id}"'
    'anonymous_identity="@utu.fi"'
    'password="{password}"'
    'ca_cert="/usr/share/ca-certificates/trust-source/mozilla.trust.crt"'
    'phase2="auth=MSCHAPv2"'
)
"""

def main():

    print('Creating a netctl profile called "eduroam" for eduroam at University of Turku')

    interface = input('network interface: ')
    id = input('UTU email: ')
    password = getpass('UTU password: ')

    config = TEMPLATE.format(**locals())

    with open(PATH, 'w') as f:
        f.write(config)

    os.chmod(PATH, 0o600)

    print('Success! You may need to install pptpclient to connect to eduroam.')

if __name__ == '__main__':
    main()
