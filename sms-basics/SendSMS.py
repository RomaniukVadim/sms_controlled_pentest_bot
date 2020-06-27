#!/usr/bin/python

from Hologram.HologramCloud import HologramCloud
import PrivateData

credentials = PrivateData.settings['credentials']
phonehome = PrivateData.settings['mothership']


hg = HologramCloud(credentials, network='cellular', authentication_type='csrpsk')

print 'Starting Pentest Bot v1.0! ...\nMessaging mothership'

smsSend = hg.sendSMS(phonehome, "Pentest Bot v1.0 reporting on Duty!")

print hg.getResultString(smsSend)

