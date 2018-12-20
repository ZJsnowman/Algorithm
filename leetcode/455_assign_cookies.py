class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort(reverse=True)
        si = 0  # 指向当前最大的饼干
        gi = 0  # 指向当前最贪婪的小朋友
        result = 0  # 记录当前满足的的小朋友
        while (si < len(s) and gi < len(g)):
            if s[si] >= g[gi]:
                si += 1
                gi += 1
                result += 1
            else:
                gi += 1

        return result


if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    sol = Solution()
    print(sol.findContentChildren(g, s))
