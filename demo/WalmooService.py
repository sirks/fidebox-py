import json

import requests

from demo import log
from demo.setup import login_hash, username, terminalsid, url, web_pass


def process_new_activity(uid):
    get_consumer_req = [('data', json.dumps({
        'login_hash': login_hash,
        'username': username,
        'operation': '14',
        'instance': '1',
        'uid': uid,
        'terminalsid': terminalsid,
        'imei': ''
    }))]
    consumer_data = requests.post(url + 'web_output.php', params=get_consumer_req)
    consumer_json = json.loads(consumer_data.text)
    if consumer_json['status'] != 0:
        log.info('no uid {}'.format(uid))
        return
    consumer_id = consumer_json['data']['id']
    reg_transaction_req = [
        ('data', json.dumps({
            'amount': '1',
            'consumersid': consumer_id,
            'instance': '13',
            'login_hash': login_hash,
            'mode': 'POINTS',
            'operation': '1',
            'terminalsid': terminalsid,
            'unit': 'pts',
            'username': username,
            "paswd": web_pass
        }))
    ]
    transaction_data = requests.post(url + 'web_input.php', params=reg_transaction_req)


if __name__ == '__main__':
    process_new_activity('04CD280A8C2A80')
