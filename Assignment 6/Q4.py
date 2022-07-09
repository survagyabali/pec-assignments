input=input("Check:")

def is_panagram(sentence):

  alp='abcdefghijklmnopqrstuvwxyz' # define a alp with all alphabets(alp)
  for letter in alp:             # checking every letter is present in alp.
      if letter in sentence.lower(): # string.lower to avoid case difference
          return True           # return only if all alp is present in   
  return False   
print(is_panagram(input))