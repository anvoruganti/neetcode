class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for string in strs:
            sorted_string=''.join(sorted(string))
            if sorted_string in hashmap:
                string_list =hashmap.get(sorted_string)
                string_list.append(string)
                hashmap[sorted_string]=string_list
            else:
               string_list=[]
               string_list.append(string)
               hashmap[sorted_string]=string_list

        result=[]

        for sorted_string in hashmap:
            val= hashmap.get(sorted_string)
            result.append(val)

        return result 
