#00:00 Intro

#00:36 capitalize()


str = 'HeLlOś'
print(str.capitalize()) #Helloś
#00:56 casefold()

print(str.casefold()) #helloś

#01:36 center()
print(str.center(20)) #       HeLlOś
#02:02 count()
print(str.count('O')) #1 (ważna jest wielkość liter)
#02:25 encode()
print(str.encode(encoding='UTF-8', errors='strict')) #b'HeLlO\xc5\x9b'
#02:55 endswith()
print(str.endswith('ś')) #True
#03:34 expandtabs()
str = 'text\ttext2\ttext3'
print(str.expandtabs(20)) #text                text2               text3
#03:56 find()
str = 'Remember to comment and subscribe!'
int = str.find('subscribe')
print(int) #24
print(str[int:])
#04:45 format()
str = '{subject} is doing: {action}.'
print(str.format(subject='Cat', action='meow'))# Cat is doing: meow.

#alternative:
str = '{} id doing: {}.'
print(str.format('Cat', 'meow'))

#05:20 format_map()
#05:26 index()
#06:17 isalnum()
#06:49 isalpha()
#07:04 isascci()
#07:24 isdecimal() / isdigit() / isnumeric()
#09:35 isidentifier()
#10:06 islower() 
#10:26 isprintable()
#10:49 isspace()
#11:05 istitle()
#11:30 isupper()
#11:52 join()
#12:35 ljust()
#12:58 lower()
#13:16 lstrip. 
#13:42 maketrans() / translate()
#14:57 partition()
#15:27 removeprefix() 
#15:43 removesuffix()
#15:59 replace()
#16:47 rfind()
#17:21 rindex()
#17:44 rjust()
#18:02 rpartition()
#18:34 rsplit() / split()
#19:59 rstrip()
#20:17 splitlines()
#20:56 startswith()
#21:15 strip()
#21:40 swapcase()
#21:54 title()
#22:16 upper()
#22:17 zfill()
#22:48 Wrapping it up""