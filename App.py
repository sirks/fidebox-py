#!/usr/bin/python

import logging
import sys

from rx import Observable

import Nfc
import Serial
from services import FideService, WalmooService

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')

if len(sys.argv) < 3:
    raise Exception('params: fideLink walmooLink serialNumber')
fideLink = sys.argv[1]
walmooLink = sys.argv[2]
serialKey = sys.argv[3]

token = FideService.getToken(fideLink, serialKey)

Serial.open()

def onCardRead(uid):
    logging.info(uid)
    WalmooService.processNewActivity(walmooLink, token, serialKey, uid, sendSerial)


def sendSerial(data):
    if data:
        logging.info(data)
        Serial.write(data+';')


cardListener = Observable.create(Nfc.pollingCards).publish()
cardListener.subscribe(onCardRead)
try:
    cardListener.connect()
except KeyboardInterrupt:
    logging.info("closing app")
    Nfc.listeningCards = False
