class Solution:
    def __init__(self) -> list[str]:
        """
        一次性生成所有
        """
        self.ans = ['1']
        for i in range(1, 30):
            s = str()
            len_prev = len(self.ans[i - 1])
            j = 0
            while j < len_prev:
                prev = self.ans[i - 1][j]
                j += 1
                cnt = 1

                while j < len_prev and self.ans[i - 1][j] == prev:
                    j += 1
                    cnt += 1
                s += str(cnt) + prev
            self.ans.append(s)

    def countAndSay(self, n: int) -> str:
        return self.ans[n - 1]
