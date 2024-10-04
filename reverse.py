class Solution:
    def reverse(self, x):
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        
        x = abs(x)
        reversed_x = 0
        
        while x != 0:
            pop = x % 10  
            x //= 10      
            if (reversed_x > INT_MAX // 10) or (reversed_x == INT_MAX // 10 and pop > 7):
                return 0  # It will overflow
            if (reversed_x < INT_MIN // 10) or (reversed_x == INT_MIN // 10 and pop > 8):
                return 0 
           
            reversed_x = reversed_x * 10 + pop
        
        
        return sign * reversed_x


sol = Solution()
print(sol.reverse(123))  
print(sol.reverse(-123)) 
print(sol.reverse(120))  
