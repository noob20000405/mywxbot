import config
import functions as f

def do_command(master, msg, dict_qs, dict_msg):
    if 'qs' == msg.text:
        print("Questions : ")
        config.SHOW_QS = True
        master.send(f.dict_to_msg(dict_qs))

    if msg.isdigit() and config.SHOW_QS:
        id = msg
        master.send(f.show_next_msgs(dict_msg, id))