#! /usr/bin/env python3
import time

from smartcard.CardRequest import CardRequest
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString, PACK

request = CardRequest(timeout=5)
listeningCards = True

def pollingCards(observer):
    while listeningCards:
        try:
            connection = request.waitforcard().connection
        except CardRequestTimeoutException:
            continue
        connection.connect()
        data, sw1, sw2 = connection.transmit([0xFF, 0xCA, 0x00, 0x00, 0x00])
        if sw1 == 144 and sw2 == 0:
            observer.on_next(toHexString(data, PACK))
        while not not request.waitforcardevent():
            time.sleep(1 / 10)