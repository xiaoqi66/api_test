# coding=utf-8
import os
import logbook
from logbook import Logger,StreamHandler,FileHandler,TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler
from functools import wraps


check_path=os.path.dirname(os.path.dirname(__file__)).replace('/','\\')
LOG_DIR = os.path.join(check_path,'log')
# print LOG_DIR
file_stream = False
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True


def get_logger(name='interface',file_log=file_stream,level=''):
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False,level=level).push_thread()
    logbook.TimedRotatingFileHandler(
            os.path.join(LOG_DIR,'%s.log' % name),
            date_format='%Y-%m-%d-%H',
            bubble=True,
            encoding='utf-8').push_thread()
    return logbook.Logger(name)
LOG = get_logger(file_log=file_stream,level='INFO')


def logger(param):
    def wrap(function):
        """logger wrapper"""
        @wraps(function)
        def _wrap(*args,**kwargs):
            LOG.info("运行位置:{}".format(param))
            return function(*args,**kwargs)
        return _wrap
    return wrap