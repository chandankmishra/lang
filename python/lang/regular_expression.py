import re
# pattern.match - first match at the begining
# pattern.search - first match in whole text
# pattern.findall - returns the string with match
# pattern.finditer - return the match object
# pattern.sub - replaces the string with pattern matched
# flag - re.compile(r'start', re.IGNORECASE) //re.IGNORECASE or re.I


text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
321-555-4321
123.555.1234
123*555*1234
0.100.100.1
1.100.100.1
100.100.100.1
100.100.100.356
100-100-100-356
abcdef  abcab
abc
aaaabbbbccc
coreyms.com
'''
pattern = re.compile(r'[0-2]?\d{1,2}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
# matches = pattern.finditer(text_to_search)
matches = pattern.findall(text_to_search)
for match in matches:
    print (match)

urls = '''
https://www.google.com
https://apple.com
http://www.facebook.com
https://www.yahoo.com
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.sub(r'\2\3', urls)
print (matches)
