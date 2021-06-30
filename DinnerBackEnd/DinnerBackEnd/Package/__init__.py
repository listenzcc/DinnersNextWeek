'''
FileName: __init__.py
Author: Chuncheng
Version: V0.0
Purpose: Dinner Arrangement Package
'''


# %%
import os
import logging
import configparser

# %%
DateFmt = '%Y-%m-%d'
Encoding = 'utf-8'
Folders = dict(
    root=os.path.join(os.path.dirname(__file__)),
    cook=os.path.join(os.path.dirname(__file__), '..', 'Cook'),
    schedule=os.path.join(os.path.dirname(__file__), '..', 'Schedule')
)

Constants = dict(
    dateFmt=DateFmt,
    encoding=Encoding,
    folders=Folders,
    cfg=configparser.ConfigParser()
)

# %%


def mk_logger(name, level, fmt):
    '''
    Method:mk_logger

    Make Logger Object as the name, level and fmt.

    Args:
    - @name: The name of the logger;
    - @level: The logging level;
    - @fmt: The fmt of the logger entry.

    Outputs:
    - The logger object.

    '''

    logger = logging.getLogger(name)
    logger.setLevel(level=level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


kwargs = dict(
    name='DNW',
    level=logging.DEBUG,
    fmt='%(asctime)s - %(levelname)s - %(message)s - (%(filename)s %(lineno)d)'
)

logger = mk_logger(**kwargs)
logger.info('Package Initialized')
