class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(ch.lower() for ch in s if ch.isalnum())
        return a == a[::-1]