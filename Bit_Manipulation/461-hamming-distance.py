class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        s = self.convert2bin(ans)
        return sum([int(x) for x in s])

    def convert2bin(self, x):
        s = str()
        while x:
            s += str(x % 2)
            x = x >> 1
        return s[::-1]
