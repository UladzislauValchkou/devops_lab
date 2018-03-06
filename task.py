#!/bin/python
# pylint:disable=invalid-name
""" task """
import time
from datetime import datetime
import json
import psutil
import cfg


class util_var():
    """ class """
    def var(self):
        ''' func '''
        self.a = psutil.cpu_percent(interval=1)
        self.b = psutil.swap_memory()
        self.c = psutil.virtual_memory()
        self.d = psutil.disk_io_counters()
        self.e = psutil.net_if_addrs()


cl = util_var()


def to_txt():
    ''' func '''
    txt = open("snapshot.txt", "w")
    txt.close
    counter = 1
    while True:
        cl.var()
        list = [cl.a, cl.b, cl.c, cl.d, cl.e]
        s_list = "Snapshot" + str(counter) + ":" + str(datetime.now()) + str(list) + "\n"
        txt = open("snapshot.txt", "a")
        txt.write(s_list)
        txt.close
        counter += 1
        time.sleep(cfg.interval)


def to_json():
    ''' func '''
    json_out = open("out.json", "w")
    json_out.close
    counter = 1
    while True:
        cl.var()
        snap = "Snapshot" + str(counter) + ":"
        keys = {'Snapshot': snap, 'time': str(datetime.now()), 'cpu': cl.a, 'swap': cl.b, 'memory': cl.c, 'io': cl.d, 'net': cl.e}
        json_out = open("out.json", "a")
        json.dump(keys, json_out, sort_keys=True, indent=4, ensure_ascii=False)
        json_out.close
        counter += 1
        time.sleep(cfg.interval)


if cfg.out_format == "txt":
    to_txt()
else:
    to_json()
