#Regular expression----------
#match() = match.start(),match.end(),match.span()

import re
pattern = r"colour"
text = "My favourite colour is red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

#Regular expression----------
#match() = match.start(),match.end(),match.span()

import re
pattern = r"colour"
text = "My favourite colour is red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

#Regular expression----------
#match() = match.start(),match.end(),match.span()

import re
word = r"word"
text = "Bangldsh is our country . It is a word"
match = re.search(word,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

#Regular expression----------
#match() = match.start(),match.end(),match.span()

import re
word = r"word"
text = "Bangldsh is our country . It is a word"
same = re.search(word,text)
if same:
    print(same.start())
    print(same.end())
    print(same.span())




