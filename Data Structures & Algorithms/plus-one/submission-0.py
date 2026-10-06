class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1
        for n in range(len(digits)):
            if digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
                else:
                    i = i-1
                    continue
            else:
                digits[i] = digits[i] + 1
                i = i-1
                return digits

        return digits
                
            

       