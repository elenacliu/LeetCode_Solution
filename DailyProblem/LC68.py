from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        word_length = [len(word) for word in words]     # 直接计算出所有单词的长度
        i = 0
        n = len(words)
        ans = []
        while i < n:
            width = 0       # 本行的宽度
            level = []      # 本行的单词列表
            s = str()       # 本行的答案
            # Part1: 获得本行的所有单词
            while i < n:    # 即便在主循环内，也要当心越界哦
                _width = width + word_length[i] + 1
                # 如果还没有超过maxWidth，更新width，并添加单词到level中
                if _width <= maxWidth or _width - 1 == maxWidth:
                    width = _width
                    level.append(words[i])
                    i += 1
                # 否则，跳出循环
                else:
                    break
            # i < n，因此不是最后一行
            if i < n:
                # 需要添加额外的空格
                if width <= maxWidth:
                    # 如果只能容纳1个单词，单词后面全部填充space
                    if len(level) == 1:
                        s += level[0]
                        s += (maxWidth - len(s)) * ' '
                    # 否则，平均分配空格
                    else:
                        # 额外的空格数
                        sp_num = maxWidth - width + 1
                        # 右侧的空格数（注意，最右边的单词的右侧可以没有空格，因此间隔数为len(level)-1）
                        sp_right = sp_num // (len(level) - 1)
                        # 余数，实为左侧[0, remain)个间隔可以再多一个空格
                        remain = sp_num - sp_right * (len(level) - 1)
                        j = 0
                        while j < len(level) - 1:
                            if j < remain:
                                s += level[j] + ' ' + (sp_right + 1) * ' '
                            else:
                                s += level[j] + ' ' + sp_right * ' '
                            j += 1
                        # 最后一个单词右侧不加空格
                        s += level[-1]
                # 不需要添加额外的空格
                elif width - 1 == maxWidth:
                    j = 0
                    while j < len(level) - 1:
                        s += level[j] + ' '
                        j += 1
                    # 最后一个单词右侧不加空格
                    s += level[-1]
            # i == n，是最后一行，左对齐，不加额外的空格，最右边不足的用空格补齐
            else:
                j = 0
                while j < len(level) - 1:
                    s += level[j] + ' '
                    j += 1
                s += level[-1]
                s += (maxWidth - len(s)) * ' '
            ans.append(s)
        return ans