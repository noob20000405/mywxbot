import time
import config

def add_item(dict, id, name, time, text):
    id += 1
    dict[id] = {}
    dict[id]["name"] = name
    dict[id]["time"] = time
    dict[id]["text"] = text
    return dict, id

def get_localtime():
    return time.strftime("%H:%M:%S", time.localtime())

def clear_dict(localtime, time, dict1, dict2):
    if time == localtime:
        dict1.clear()
        dict2.clear()
    return dict1, dict2

def add_question(dict, id, name, time, text):
    dict[id] = {}
    dict[id]["name"] = name
    dict[id]["time"] = time
    dict[id]["text"] = text
    return dict

def show_next_msgs(dict, id):
    for i in range(config.NUMBER_MSGS):
        index = str(int(id) + i)
        print(dict[index]['name'], ' : ', dict[index]['text'])