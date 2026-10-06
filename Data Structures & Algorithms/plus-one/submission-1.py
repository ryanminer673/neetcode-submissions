class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        #base case 
        if not digits:
            return [1]

        #work done
        # if number at end is not 9 then add 1 to it and return teh list
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        # else call the fnction on the list without teh last number and add a 0 to the end of teh list
        else:
            return self.plusOne(digits[0:-1]) + [0] 

        
                
            

       