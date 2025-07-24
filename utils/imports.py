from PIL import Image
import numpy as np
import logging, colorlog

# Configuração do handler e do formatter colorido
log_format = (
    "%(log_color)s[%(asctime)s] %(levelname)s: %(message)s (%(filename)s:%(lineno)d)"
)

log_colors = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

formatter = colorlog.ColoredFormatter(log_format, log_colors=log_colors)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)
