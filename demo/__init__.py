import logging

log = logging
log.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(threadName)s %(message)s')
