import re

string = "The Sun is falling down, The Sun is Still Bright"
print(re.search("^.*Sun.*$", string))
print(re.findall("n", string))
print(re.split("\s", string))
print(re.split("\s", string, 1))
print(re.sub("Sun", "Moon", string, 1))