class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        
        for st in strs:
            key = "".join(sorted(st))
            
            if key in s:
                s[key].append(st)
            else:
                s[key] = [st]

        return list(s.values())