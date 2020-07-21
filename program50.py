#Regular expression----------
#match()----------

import re
pattern = r"colour"
if re.match(pattern,"colour is colour , I love red colour"):
    print("Match")
else:
    print("Not Match")

#search()------------------
import re
pattern = r"colour"
if re.search(pattern,"colour is colour , I love red colour"):
    print("Match")
else:
    print("Not Match")


#findall()----------------
import re
pattern = r"colour"
print(re.findall(pattern,"red is colour , I love red colour"))

