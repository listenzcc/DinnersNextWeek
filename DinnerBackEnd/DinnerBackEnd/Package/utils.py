'''
FileName: utils.py
Author: Chuncheng
Version: V0.0
Purpose: Useful Functions
'''

# %%
import os
import configparser
import pandas as pd
import traceback
import time

from . import logger, Constants

# %%


def convert_cfg2df(cfg):
    '''
    Method: convert_cfg2df

    Convert Config [cfg] into DataFrame.

    Args:
    - @cfg

    Outputs:
    - The Converted DataFrame

    '''

    df = pd.DataFrame(columns=['name', 'foods'])

    for sec in cfg.sections():
        dct = dict(
            name=sec,
            foods=set()
        )

        for key in cfg[sec]:
            dct['foods'].add(cfg[sec][key])

        df = df.append(dct, ignore_index=True)

    logger.debug(
        'Converted Config into DataFrame, with {} entries'.format(len(df)))

    return df


def save_cfg(cfg, path):
    '''
    Method: save_cfg

    Save Config [cfg] to the Path [path]

    Args:
    - @cfg: The Config object;
    - @path: The path to be saved.

    '''

    encoding = Constants['encoding']
    if os.path.isfile(path):
        logger.warning(
            'Overwriting Warning: Saving Config into {}'.format(path))
        with open(path + '-{}.save.ini'.format(time.time()),
                  'w',
                  encoding=encoding) as f:
            f.write(open(path, encoding=encoding).read())

    try:
        cfg.write(open(path, 'w', encoding=encoding))
        logger.debug('Saved Config into {} with {}'.format(path, encoding))
    except:
        logger.error('Failed to save Config, error: {}'.format(
            traceback.format_exc()))

    pass


def convert_df2cfg(df):
    '''
    Method: convert_df2cfg

    Convert DataFrame [df] into Config

    Args:
    - @df

    Outputs:
    - The Converted Config

    '''

    cfg = configparser.ConfigParser()
    for j in range(len(df)):
        se = df.iloc[j]

        name = se['name']
        foods = se['foods']

        cfg.add_section(name)

        for i, f in enumerate(foods):
            cfg[name][chr(ord('A') + i)] = f

    logger.debug(
        'Converted DataFrame into Config, with {} entries'.format(len(df)))

    return cfg
