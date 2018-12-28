class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        x = 0
        for i in range(len(t)):
            if t[i] == s[x]:
                x += 1
                if x == len(s):
                    return True
        return False


if __name__ == '__main__':
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    print(sol.isSubsequence(s, t))
