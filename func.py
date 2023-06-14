import re
import random

s = ""

with open("bee_movie.txt",'r') as script:
    speech = script.read().splitlines()
for line in speech:
    if line != "" and line != "  ":
        s += line

l = re.findall('.*?[.!\?]', s)
print(random.choice(l))
