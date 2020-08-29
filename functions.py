import time

def add_item(dict, id, name, time, text):
    dict[id] = {}
    dict[id]["name"] = name
    dict[id]["time"] = time
    dict[id]["text"] = text
    id += 1

def get_localtime():
    return time.strftime("%H:%M:%S", time.localtime())

def clear_dict(localtime, time, dict):
    if time == localtime:
        dict.clear()