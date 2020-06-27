#!/usr/bin/python

from Hologram.HologramCloud import HologramCloud
import time
import PrivateData

credentials = PrivateData.settings['credentials']
phonehome = PrivateData.settings['mothership']


try:

        hg = HologramCloud(credentials, network='cellular', authentication_type='csrpsk')

        print "Starting ... Will check every 10 seconds for SMS message\n"
        while 1: 
            recvCommand = hg.popReceivedSMS()

            command = ''
            if recvCommand is not None: 
                print recvCommand
                command = recvCommand.message

            time.sleep(10)


except Exception as ex:
        print ex.message, ex.args
        pass 



