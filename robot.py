from wxpy import *
import MySQLdb
import config
import command
import globvar
import functions as f
import regex

bot = Bot(cache_path=True)

bot.file_helper.send('hello !!')

listen_group = ensure_one(bot.groups().search('索邦大学校友总群'))
# listen_friend = bot.friends().search('')[0]

myFriend = bot.friends()
myGroup = bot.groups()
master = ensure_one(bot.friends().search(config.MASTER))

if config.SYNC_MSG:
    sync_groups = bot.groups().search(config.SYNC_GROUP_NAME)
    sync_groups[0].update_group(members_details=True)
    sync_groups[1].update_group(members_details=True)
else:
    sync_groups = bot.file_helper

"""
if listen_group:
    print('succeed !')
    sex_dict = {'male': 0, 'female': 0, 'unknown': 0}
    for member in listen_group.members:
        print(member, '\n')
        if member.sex == 1:
            sex_dict['male'] += 1
        elif member.sex == 2:
            sex_dict['female'] += 1
        else:
            sex_dict['unknown'] += 1
    print(sex_dict)
"""
@bot.register(myFriend) # for test
def friends_msg(msg):
    if config.LISTEN_FRIENDS:
        print("From a friend : ")
        name = msg.sender.name
        time = msg.receive_time
        text = msg.text
        # print(msg.sender.name)
        # print(msg.receive_time)
        message = msg.sender.name + ' : ' + msg.text
        print(message)

        globvar.dict_msg, globvar.msg_id = f.add_item(globvar.dict_msg, globvar.msg_id, name, time, text)
        print('id : ', globvar.msg_id)

        if regex.is_question(text):
            globvar.dict_qs = f.add_question(globvar.dict_qs, globvar.msg_id, name, time, text)

        localtime = f.get_localtime()
        globvar.dict_msg, globvar.dict_qs = f.clear_dict(localtime, config.INITIALIZE_TIME, globvar.dict_msg, globvar.dict_qs)

@bot.register(myGroup)
def group_msg(msg):
    if config.LISTEN_GROUPS:
        print("From the group : ")
        name = msg.member.name
        time = msg.receive_time
        text = msg.text
        # print(msg.member.name)
        # print(msg.receive_time)
        message = msg.member.name + ' : ' + msg.text
        print(message)

        globvar.dict_msg, globvar.msg_id = f.add_item(globvar.dict_msg, globvar.msg_id, name, time, text)
        print('id : ', globvar.msg_id)

        if regex.is_question(text):
            globvar.dict_qs = f.add_question(globvar.dict_qs, globvar.msg_id, name, time, text)

        localtime = f.get_localtime()
        globvar.dict_msg, globvar.dict_qs = f.clear_dict(localtime, config.INITIALIZE_TIME, globvar.dict_msg,
                                                         globvar.dict_qs)

        # test
        print(globvar.dict_msg)

@bot.register(sync_groups, except_self=False)
def sync_my_groups(msg):
    if config.SYNC_MSG:
        sync_message_in_groups(msg, sync_groups)

@bot.register(chats=master)
def do_command(msg):
    command.do_command(master, msg, globvar.dict_qs, globvar.dict_msg)

embed()
