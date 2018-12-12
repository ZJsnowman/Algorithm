__author__ = 'ZJsnowman'
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
import time
import functools


def diff_time(start_time, end_time):
    """
    计算时间差
    :param start_time:
    :param end_time:
    :return:
    """
    start_time = start_time
    end_time = end_time
    try:
        start_time_obj = datetime.strptime(start_time.strip(), "%Y-%m-%d %H:%M:%S:%f")
        end_time_obj = datetime.strptime(end_time.strip(), "%Y-%m-%d %H:%M:%S:%f")
        start_time_int = int(time.mktime(start_time_obj.timetuple()) * 1000.0 + start_time_obj.microsecond / 1000.0)
        end_time_int = int(time.mktime(end_time_obj.timetuple()) * 1000.0 + end_time_obj.microsecond / 1000.0)
        return end_time_int - start_time_int
    except Exception  as e:
        print('except:', e)
        return -1;


def clock(func):
    """
    计算函数耗时
    :param func:
    :return:
    """

    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elasped = time.time() - t0
        name = func.__name__
        print('执行 [%s] 耗时 :%0.8fs ' % (name, elasped))
        return result

    return clocked


def get_yesterday():
    """
    获取昨天的日期
    :return:  两种格式, bar 表示2018-08-12,dot 表示2018.08.12
    """
    yesterday = datetime.today() + timedelta(-1)
    yesterday_format_bar = yesterday.strftime('%Y-%m-%d')
    yesterday_format_dot = yesterday.strftime('%Y.%m.%d')
    return {'bar': yesterday_format_bar, 'dot': yesterday_format_dot}
