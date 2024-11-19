class Solution:
    def getSum(self, a: int, b: int) -> int:

        #Porte hobe ei context ta
        # Mask to keep results within 32 bits
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            # XOR for sum without carry, AND and shift for carry
            temp = (a ^ b) & MASK
            b = ((a & b) << 1) & MASK
            a = temp
        
        # If result is greater than MAX_INT, it's a negative number in 32-bit
        return a if a <= MAX_INT else ~(a ^ MASK)