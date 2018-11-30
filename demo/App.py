from rx import Observable

from demo import Nfc, WalmooService, log


def _on_card_read(uid):
    log.info(uid)
    WalmooService.process_new_activity(uid)


cardListener = Observable.create(Nfc.pollingCards).publish()
cardListener.subscribe(_on_card_read)
try:
    cardListener.connect()
except KeyboardInterrupt:
    log.info("closing app")
    Nfc.listeningCards = False
