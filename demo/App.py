import logging
import sys

from rx import Observable

from demo import Nfc, WalmooService

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(threadName)s %(message)s')

if len(sys.argv) < 1:
    raise Exception('params: walmooLink')
walmoo_link = sys.argv[1]


def _on_card_read(uid):
    logging.info(uid)
    WalmooService.process_new_activity(walmoo_link, uid)


cardListener = Observable.create(Nfc.pollingCards).publish()
cardListener.subscribe(_on_card_read)
try:
    cardListener.connect()
except KeyboardInterrupt:
    logging.info("closing app")
    Nfc.listeningCards = False
