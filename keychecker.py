import os

# assign directory
directory = 'keys'

#create dictionary
d = dict()

#open list of file extensions
text = open('keyfolder.txt', 'r')

#categorize extensions
for extension in text:
    if extension.strip() in d:
        d[extension.strip()] += 1
    else:
        d[extension.strip()] = 1

#write dictionaries
with open("listextensions.txt", 'w') as f: 
    for key, value in d.items(): 
        f.write('%s:%s\n' % (key, value))


