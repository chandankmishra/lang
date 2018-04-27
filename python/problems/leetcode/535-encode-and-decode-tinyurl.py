import string
import random


class Codec:
    alphabet = string.ascii_letters + string.digits

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            print (code)
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]


# Your Codec object will be instantiated and called as such:
codec = Codec()
url1 = "https://leetcode.com/problems/design-tinyurl"
c1 = codec.encode(url1)
print (c1)
print (codec.decode(c1))

for i in range(6):
    print (i)

print (Codec.alphabet)
print (random.choice(Codec.alphabet))
