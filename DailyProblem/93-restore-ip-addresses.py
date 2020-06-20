from typing import List


# 小心一个bug是，每个整数除非就是0，否则不能以0开头
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        n = len(s)

        def solve(path, i):
            if len(path) == 4:
                if i >= n:
                    ans.append('.'.join(path))
                    # print(ans[-1])
                return
            if i >= n:
                return

            if i + 1 <= n:
                solve(path + [s[i:i + 1]], i + 1)
            if i + 2 <= n and s[i] != '0':
                solve(path + [s[i:i + 2]], i + 2)
            if i + 3 <= n and s[i] != '0' and int(s[i:i + 3]) <= 255:
                solve(path + [s[i:i + 3]], i + 3)

        solve([], 0)
        return ans
