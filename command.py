def do_command(msg):
    print("history : ")
    if 's' == msg.text:
        for key, content in dict_messages.items():
            print("ID: ", key)
            for value in content.values():
                print(value)