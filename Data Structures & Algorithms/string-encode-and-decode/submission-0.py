class Solution:

    def encode(self, strs: List[str]) -> str:
        empty = []
        for str in strs:
            empty.append(f"{len(str)}#{str}")
        return ''.join(empty)

    def decode(self, s: str) -> List[str]:
        empty = []
        i = 0
        while i < len(s):
            j = s.find("#",i)
            length = int(s[i:j])
            i = j + 1
            empty.append(s[i: i+length])
            i += length
        return empty

