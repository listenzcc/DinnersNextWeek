'''
FileName: scheduler.py
Author: Chuncheng
Version: V0.0
Purpose: Dinner Scheduler
'''


# %%
import datetime
from . import Constants, logger, cooks

# %%


def strftime(day):
    return day.strftime(Constants['dateFmt'])


class Scheduler(object):
    ''' Dinner Scheduler Class '''

    def __init__(self):
        '''
        Method: __init__

        Initialization of the Scheduler

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
