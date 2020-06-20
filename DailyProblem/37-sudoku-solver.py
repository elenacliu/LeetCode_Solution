# -*- coding: utf-8 -*-


class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [0b0] * 9
        col = [0b0] * 9
        grid = [0b0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():   # 如果(i, j)是数字
                    mask = 1 << int(board[i][j])    # 那么mask就将这一位置为1
                    row[i] |= mask
                    col[j] |= mask
                    grid[(i//3)*3+j//3] |= mask

        for r in row:
            print(bin(r))
        for c in col:
            print(bin(c))
        for g in grid:
            print(bin(g))

        def solve(s):
            if s < 81:  # 问题，你这样只能求一次的值啊
                i = s // 9
                j = s % 9
                if board[i][j] == '.':
                    occ = row[i] | col[j] | grid[(i//3)*3+j//3]   # 求并集
                    print("occ", bin(occ))
                    if occ == 0b1111111110:     # 这一位没有数字可以填写，返回False
                        return False
                    occ = occ >> 1      # 求哪些位为1
                    bit = 0             # 第bit位
                    flag = False
                    while bit < 9:     # 原循环条件occ is not 0不对
                        if occ & 1 == 0:    # 如果某一位为0
                            bit += 1
                            occ = occ >> 1
                            print(bit)
                            board[i][j] = str(bit)
                            mask = 1 << bit
                            row_c = row[i]
                            col_c = col[j]
                            grid_c = grid[(i//3)*3+j//3]
                            row[i] |= mask
                            col[j] |= mask
                            grid[(i//3)*3+j//3] |= mask
                            if solve(i * 9 + j + 1):
                                flag = True
                                break
                            else:
                                # 本次尝试失败
                                board[i][j] = '.'
                                row[i], col[j], grid[(i//3)*3+j//3] = row_c, col_c, grid_c
                                continue
                        else:
                            occ = occ >> 1
                            bit += 1
                    if flag:
                        return True
                    else:
                        return False
                else:
                    return solve(s+1)
            else: return True
        solve(0)
