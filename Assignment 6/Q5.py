words=input('Input hyphenated list:')
words=words.split('-')

words.sort()

a='-'.join(i for i in words)
print(a)