# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2012-2016, Ryan P. Wilson
#
#     Authority FX, Inc.
#     www.authorityfx.com

#!/usr/bin/env python

import platform
import subprocess
import re

def print_header():
    print '________________________\n'
    print 'Authority FX, Inc. (c)\n'
    print 'Mac Address Utility'
    print '________________________\n'
    print 'Finding mac address...\n'

if platform.system() == 'Windows':

    from Tkinter import Tk

    print_header()

    getmac_call = subprocess.Popen('getmac', shell=True, stdout=subprocess.PIPE)
    output, err = getmac_call.communicate()

    output = output.lower().replace('-', '').split('\n')

    mac_list = []

    for line in output:
        if re.search('^[a-z0-9]{12}', line) and line.find('media disconnected') < 0:
            mac_list.append((line[:12],line[13:]))

    if len(mac_list) > 0:
        print 'id#  Mac Address    Identifier'
        for i in range(len(mac_list)):
            print str(i+1) + ') ' + mac_list[i][0] + mac_list[i][1]

        print ''

        while True:
            select_raw = raw_input('Enter a mac id# to copy to clipboard: ')

            try:
                select = int(select_raw)
                if select >= 1 and select <= len(mac_list):
                    break
                else:
                    print 'Invalid selection'
            except:
                print 'You must enter a number'

        cb = Tk()
        cb.withdraw()
        cb.clipboard_clear()
        cb.clipboard_append(str(mac_list[select-1][0]))

        print '\n' + str(mac_list[select-1][0]) + ' copied to clipboard.'
    else:
        print 'No Mac addresses found'


    raw_input('Press any key to close...')

else:
    print platform.system() + ' is not currently supported by Authority FX.'

