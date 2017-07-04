# -*- coding: UTF-8 -*-
from datetime import datetime

def str_parse_time(date_str):
    try:
        date = datetime.strptime(date_str, '%Y%m%d')
    except ValueError:
        date = datetime.today()
    return date
