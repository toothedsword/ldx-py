#!/bin/python3

import time as tm
import re
import datetime

def time2str(t,ss, num=1): # {{{
    st = datetime.datetime.utcfromtimestamp(t)
    st = str(st)
    time = re.search(r'(\d\d\d\d)-(\d\d)-(\d\d) (\d\d)\:(\d\d)\:(\d\d)',st)
    year = time.group(1)
    year2 = re.search('\d\d(\d\d)',year)
    year2 = year2.group(1)
    month = time.group(2)
    dom = time.group(3)
    hour = time.group(4)
    minute = time.group(5)
    sec = time.group(6)
    st = ss
    for i in range(0, num):
        st = re.sub('yyyy',year,st);
        st = re.sub('mm',month,st);
        st = re.sub('dd',dom,st);
        st = re.sub('HH',hour,st);
        st = re.sub('MM',minute,st);
        st = re.sub('SS',sec,st);
    return st # }}}


def time2vec(t): # {{{
    st = datetime.datetime.utcfromtimestamp(t)
    st = str(st)
    time = re.search(r'(\d\d\d\d)-(\d\d)-(\d\d) (\d\d)\:(\d\d)\:(\d\d)',st)
    year = int(time.group(1))
    month = int(time.group(2))
    dom = int(time.group(3))
    hour = int(time.group(4))
    minute = int(time.group(5))
    sec = int(time.group(6))
    return year,month,dom,hour,minute,sec # }}}


def str2time(s, rs='yyyymmddHHMMSS'):  # {{{
    if rs == 'yyyymmddHHMMSS':
        rt = re.search(
            r'(\d\d\d\d)[^\d]*(\d\d)[^\d]*(\d\d)[^\d]*' +
            r'(\d\d)[^\d]*(\d\d)[^\d]*(\d\d)', s)
        year = rt.group(1)
        month = rt.group(2)
        dom = rt.group(3)
        hour = rt.group(4)
        minute = rt.group(5)
        sec = rt.group(6)
    else:
        t = re.search(r'yyyy', rs)
        year = s[t.span(0)[0]:t.span(0)[1]]
        t = re.search(r'mm', rs)
        month = s[t.span(0)[0]:t.span(0)[1]]
        t = re.search(r'dd', rs)
        dom = s[t.span(0)[0]:t.span(0)[1]]
        t = re.search(r'HH', rs)
        hour = s[t.span(0)[0]:t.span(0)[1]]
        t = re.search(r'MM', rs)
        minute = s[t.span(0)[0]:t.span(0)[1]]
        t = re.search(r'SS', rs)
        sec = s[t.span(0)[0]:t.span(0)[1]]
    ts = tm.mktime((int(year), int(month), int(dom),
                    int(hour), int(minute), int(sec), 0, 0, 0)) - \
        tm.mktime((1970, 1, 1, 0, 0, 0, 0, 0, 0))
    return ts  # }}}


def vec2time(year, month, dom, hour, minute, sec):
    ts = tm.mktime((int(year), int(month), int(dom), int(hour), int(minute), int(sec), 0, 0, 0)) - \
    tm.mktime((1970, 1, 1, 0, 0, 0, 0, 0, 0))
    return ts  # }}}


