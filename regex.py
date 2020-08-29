import re

def is_question(text):
    word_list = ['请问', '问', '吗', '么', '\?', '\？']
    for word in word_list:
        if re.search(word, text) != None:
            return True
    return False

"""
text = "我想你是逼"

if is_question(text):
    print("True")
else:
    print("False")
"""