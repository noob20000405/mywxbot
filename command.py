import config
import functions as f

def do_command(msg, dict_qs, dict_msg):
    if 'qs' == msg.text:
        print("Questions : ")
        config.SHOW_QS = True
        for key, content in dict_qs.items():
            print("ID: ", key)
            for value in content.values():
                print(value)

    if 'next' == msg and config.SHOW_QS:
        id = msg
        f.show_next_msgs(dict_msg, id)