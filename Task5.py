class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ int((len(bin(num)) - 2) * '1', 2)
