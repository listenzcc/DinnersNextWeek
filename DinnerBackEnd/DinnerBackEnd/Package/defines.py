'''
FileName: defines.py
Author: Chuncheng
Version: V0.0
Purpose: Definition of the Classes in Backend
'''


# %%
import os
import datetime
import pandas as pd
from . import Constants, logger
from .utils import convert_df2cfg, convert_cfg2df, save_cfg

# %%

encoding = Constants['encoding']


class FoodSets(object):
    ''' Object of Foods and Sets'''

    def __init__(self):
        '''
        Method: __init__

        Initialization of the FoodSets object

        Args:
        - @self

        '''

        fpath = os.path.join(Constants['folders']['cook'],
                             'cooks.ini')

        cfg = Constants['cfg']
        cfg.read(fpath, encoding=encoding)

        df = convert_cfg2df(cfg)
        print(df)

        _cfg = convert_df2cfg(df)
        save_cfg(_cfg, fpath)

        pass

# %%


def strftime(day):
    return day.strftime(Constants['dateFmt'])


class Scheduler(object):
    ''' Dinner Scheduler Class '''

    def __init__(self):
        '''
        Method: __init__

        Initialization of the Scheduler Object

        Args:
        - @self

        Outputs:
        - @

        '''

        self.reset_today()

        logger.info('Initialized Scheduler')

        pass

    def reset_today(self):
        '''
        Method: reset_today

        Reset Attribute of Today

        Args:
        - @self

        Outputs:
        - @

        '''

        self.today = datetime.date.today()

        logger.debug('Resetted Today as {}'.format(strftime(self.today)))

        pass


# %%
scheduler = Scheduler()
