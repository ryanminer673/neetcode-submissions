class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for string in strs:
            sorted_string_l = sorted(string)
            sorted_string = "".join(sorted_string_l)

            if sorted_string in groups:
                groups[sorted_string].append(string)
            else:
                groups[sorted_string] = [string]
        
        result = []
        for group in groups.values():
            result.append(group)


        return result


