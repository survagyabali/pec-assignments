print('you can enter only 10 words in the list')

userlist = []  #taking an empty list


for i in range(11):
    word = input('enter', str(i),' word: ')
    userlist.append(word)  #filling my list
    

print("list entered by user is: ", userlist)

for word in userlist:
    print( userlist.count(word),' times') 