import logging

import requests
from rx import Observable


def processNewActivity(link, token, serialKey, uid, callback):
    def callApi(observer):
        params = {'imei': serialKey, 'uid': uid}
        url = link + '/wal-program/activities/new'
        headers = {'Content-type': 'application/json', 'wtoken': token}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code >= 300:
            observer.on_error(response.text)
        observer.on_next(response.text)

    def onError(error):
        logging.error(error)

    Observable.create(callApi).subscribe(on_next=callback, on_error=onError)