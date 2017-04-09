#!/usr/bin/python
from datetime import time
from tasklib import Task, local_zone

DEFAULT_TIME = time(22,0,0)  # Your wanted default time

def is_local_midnight(timestamp):
    return timestamp.astimezone(local_zone).time() == time(0,0,0)

def set_default_time(timestamp):
    return timestamp.astimezone(local_zone).replace(
        hour=DEFAULT_TIME.hour,
        minute=DEFAULT_TIME.minute,
        second=DEFAULT_TIME.second,
        )

def hook_default_time(task):
    if task['due'] and is_local_midnight(task['due']):
        task['due'] = set_default_time(task['due'])
        print("Default due time has been set.")
