class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort each str to get a key that i can use to group anagrams
        # loop through each 
        # sort it 
        # add it as a key to a dict
        # add the original value as the value to a list
        # move onto the next

        ana_map = {}

        for string in strs:

            sorted_string = sorted(string)

            sorted_string = "".join(sorted_string)

            if sorted_string in ana_map:
                ana_map[sorted_string].append(string)
            else:
                ana_map[sorted_string] = [string]

        result = []

        for key, value in ana_map.items():
            result.append(value)

        return result


