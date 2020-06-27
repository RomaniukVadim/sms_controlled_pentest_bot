#!/usr/bin/python


from Hologram.HologramCloud import HologramCloud
import PrivateData
import time
from PortScanner import ScanMe


def ProcessCommand(command) :

    if command.lower().find('nmap') != -1 :
        
        try :
            _,ip,ports = command.split()

            print "\nInitiating Scan: %s %s" %(ip, ports)

            result = ScanMe(ip,ports)

            print result
        except Exception as ex:
            result = ex.message
            raise

        return result


credentials = PrivateData.settings['credentials']
phonehome = PrivateData.settings['mothership']


while 1: 

    try:

        hg = HologramCloud(credentials, network='cellular', authentication_type='csrpsk')
        hg.enableSMS()


        print 'Starting Pentest Bot v1.0! ...\nMessaging mothership'
        smsSend = hg.sendSMS(phonehome, "Pentest Bot v1.0 reporting on Duty!")
        print hg.getResultString(smsSend)


        # Let us wait for command to act on

        print "Waiting for Mothership's message ..."
      
        while 1: 
            recvCommand = hg.popReceivedSMS()

            command = ''
            if recvCommand is not None: 
                print recvCommand
                command = recvCommand.message

                hg.sendSMS(phonehome, 'On it Boss! please be patient...')
                time.sleep(3)
                commandResult = ProcessCommand(command) 

                smsSend = hg.sendSMS(phonehome, commandResult.replace('\n', ' ')[:155])
                print hg.getResultString(smsSend)



            time.sleep(10)


    except Exception as ex:
        print ex.message, ex.args
        pass 



