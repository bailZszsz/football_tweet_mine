
# a quick file I made to test a potential feature - translating an emoji into their unicode codepoint.
# this feture was implemented into my project. 

emoji = '😍'

test1 = f'U+{ord(emoji):X}'

test2 = emoji.encode('unicode-escape').decode('ASCII')

print(test1)
print(test2)

##throw type error for weird emojis, skip them!
##throw missing element eror if unicode code not showm in sentiment data, skip it!

