class Solution:
    def __init__(self):
        self.to19 = 'Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.unit = ["", "Thousand", "Million", "Billion"]

    def words(self, n):
        if n == 0:
            return []
        if n < 20:
            return [self.to19[n]]
        elif n < 100:
            return [self.tens[n // 10]] + self.words(n % 10)
        else:
            return [self.to19[n // 100]] + ["Hundred"] + self.words(n % 100)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        count = 0
        result = []
        while num > 0:
            n = num % 1000
            if n != 0:
                temp = self.words(n)
                if count > 0:
                    temp = temp + [self.unit[count]]
                result = temp + result
            num = num // 1000
            count += 1
        return ' '.join(result)


s = Solution()
print(s.numberToWords(123))
print(s.numberToWords(922343))
print(s.numberToWords(435399922343))
