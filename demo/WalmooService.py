import requests


def process_new_activity(link, uid):
    params = {'imei': serialKey, 'uid': uid}
    url = link + '/wal-program/activities/new'
    headers = {'Content-type': 'application/json', 'wtoken': token}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code >= 300:
        observer.on_error(response.text)
    observer.on_next(response.text)
