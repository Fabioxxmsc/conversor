import re

inputText = '00.758.947/0001-66 2.386.505 -9'

strPattern = '00.758.947/0001-66'

math = re.search(strPattern, inputText)

if inputText[math.start(): math.end()] == strPattern:
    print('matched')
else:
    print('not matched')