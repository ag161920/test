import re
import random

def func1(N):
  """
  Returns random line from the script of Bee Movie.
  Inputs: Line number
  Outputs: Script line
  """
  s = ""

  with open("bee_movie.txt",'r') as script:
      speech = script.read().splitlines()
  for line in speech:
     if line != "" and line != "  ":
          s += line

  l = re.findall('.*?[.!\?]', s)
  if N > len(l):
    print("Error: Input script line number out of range!")
  else:
    return l[N-1]
