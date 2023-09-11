import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fh = logging.FileHandler('./notification_bot_sender.log', mode='w')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

logger.info('logger inited')