class Solution:
    def addBinary(self, a: str, b: str) -> str: 
        a_int = int(a,2) 
        b_int = int(b,2)

        while b_int:
            carry = (a_int & b_int) << 1

            a_int = a_int ^ b_int
            b_int = carry

        return bin(a_int)[2:]