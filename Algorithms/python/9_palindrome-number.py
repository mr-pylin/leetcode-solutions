# https://leetcode.com/problems/palindrome-number
# difficulty: easy

class Solution:
    # method 1:
    # def isPalindrome(self, x: int) -> bool:
    #     if x >= 0:  # negative number is not palindrome
    #         digits = []
    #         while x:  # split number into a list of digits
    #             digits.append(x % 10)
    #             x = x // 10
            
    #         # loop half of the list and compare it symmetrically
    #         is_palindrome = True
    #         for i in range(len(digits) // 2):
    #             if digits[i] != digits[-(i + 1)]:
    #                 is_palindrome = False
    #                 break
    #     else:
    #         is_palindrome = False
        
    #     return is_palindrome
    
    # method 2:
    # def isPalindrome(self, x: int) -> bool:
    #     if (x > 0 and x % 10) or x == 0:  # negative numbers and numbers ending with 0 are not palindrome
    #         n1 = x
    #         n2 = 0

    #         # reverse the number
    #         while x:
    #             n2 = n2 * 10 + (x % 10)
    #             x = x // 10

    #         if n1 == n2:
    #             return True
            
    #     return False

    # method 3: faster
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:  # negative number is not palindrome
            digits = str(x)
            
            # loop half of the str and compare it symmetrically
            is_palindrome = True
            for i in range(len(digits) // 2):
                if digits[i] != digits[-(i + 1)]:
                    is_palindrome = False
                    break
        else:
            is_palindrome = False
        
        return is_palindrome

        
if __name__ == '__main__':
    x = 123
    print(Solution().isPalindrome(x))