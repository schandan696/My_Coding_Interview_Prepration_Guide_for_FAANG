# def LCS(s1, s2):
#     if len(s1) == 0 or len(s2) == 0:
#         return 0

#     if s1[0] == s2[0]:
#         return 1 + LCS(s1[1:], s2[1:])
#     else:
#         return max(LCS(s1, s2[1:]), LCS(s1[1:], s2))
def __LCS(s1, s2, i, j, dp):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    if dp[i][j] >= 0:
        return dp[i][j]
     
    if s1[0] == s2[0]:
        return 1 + __LCS(s1[1:], s2[1:], i+1, j+1, dp)
    else:
        ans = max(__LCS(s1, s2[1:], i, j+1, dp), __LCS(s1[1:], s2, i+1, j, dp))
        dp[i][j] = ans
        return ans

def LCS2(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[-1 for j in range(m)] for i in range(n)]
    return __LCS(s1, s2, 0, 0, dp)

s1 = "abcdefghijklm"
s2 = "acdef"
print(LCS2(s1, s2))



