# 动态规划

DP的复健之路实在是太辛苦了！不得不说DP几乎承包了LeetCode上大多数难题，而且一直是”看得懂但想不到“的那类难题……:sob:

两场面试都考的是动态规划，面试官这是有多么喜欢动态规划啊:wink:

在算法方面不算很有经验，也就是今年断断续续做了几个月题目而已，下面的都是些经验之谈。我认为DP和两种思想有联系：一种是递归，一种是自动机。目前还没找到两种联系之间的关系。

从递归的角度讲，递归树的节点都代表了一个具体的状态（想想给递归函数传了哪些参数:smile:），而递归树中偏偏重合的状态又很多（因为许多问题的子问题序列是重叠的），因此不如以空间换时间，把这些状态对应的结果存下来，这是自顶而下的做法，好理解但是代码、过程总显得不那么优美，因为第一次遇到某个子问题的情况不太有规律，说赋值就赋值了，不在写代码的人的掌控内啊！于是就有了利用递推自底而上的写法，这下从规模较小的情况出发，得到规模较大的问题的答案，每种状态都在这种状态遍历到的时候得到答案，本本分分易debug。但问题又来了，怎么从前面的情况推到后面的情况呢？这下又渗透了自动机的思想。

从自动机的角度讲，dp数组和状态转移方程充当的就是状态转移图——dp数组相当于节点，状态转移方程相当于边。边实际上代表的是”选“或”不选“的关系。

动态规划的代码实现要注意4点：

1. ``dp``数组的含义（也就是自动机每个节点的含义）
2. 状态转移方程
3. 边界条件&遍历顺序
4. 答案（与dp数组的含义有关，有些答案就是数组元素，有些答案却要对数组元素进行处理）

说了这么多，还是需要做题练手，下面直接上题。

## 区间dp（这类dp多半和字符串有关）

### LC647. 回文子串

[题目链接](https://leetcode-cn.com/problems/palindromic-substrings/)

#### 方法1：中心扩展算法$O(n^2)$

#### 方法2：马拉车算法$O(n)$

### LC87. 扰乱字符串

[题目链接](https://leetcode-cn.com/problems/scramble-string/)

这题给我的启示就是，不要被形式所迷惑。题目是否用动态规划解决，一是靠做题感觉，二是靠逻辑推理（比方说从递归的记忆化搜索推导出来）。我认为这题就属于靠推理所得的。因为相比动态规划，递归方法比较容易想到。

#### 方法1：暴力递归

如果考虑字符串T是否是字符串S的扰乱字符串，可以将S分成两半S1,S2，T分成两半T1,T2。

以下两种情况中有一种成立，那么T就是S的扰乱字符串。

+ T1是S1的扰乱字符串 且 T2是S2的扰乱字符串
+ T2是S1的扰乱字符串 且 T1是S2的扰乱字符串

很明显是理论上可以这样解决的。

但问题在于，递归过程中的很多结果是可以储存下来的（memoization)，因为递归树中有很多**相同的状态**。记忆化搜索/动态规划不就是用数组的不同维表示不同的状态吗？很自然想到动态规划。

```python
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        l = len(s1)
        for k in range(1, l):
            if self.isScramble(s1[:k],s2[:k]) and self.isScramble(s1[k:],s2[k:]):
                return True
            if self.isScramble(s1[:k],s2[l-k:]) and self.isScramble(s1[k:],s2[:l-k]):
                return True
        return False
    
```

但很奇怪的是python中这种剪枝+递归还比动态规划快，不知道为什么。

#### 方法2：动态规划

1. ``dp``数组的含义

   我们首先想到利用``dp[i][j][m][n]``代表S[i...j]和T[m...n]是否是扰乱字符串。但是因为互为扰乱字符串的前提是j - i == m - n，因此降为3维``dp[i][j][len]``，表示S[i...i+len-1]和T[m...m+len-1]是否是扰乱字符串。

2. 状态转移方程

   最重要的一环！
   $$
   dp[i][j][k]=OR_{1\leq w\leq k-1} \{dp[i][j][w]\space\space and \space\space dp[i+w][j+w][k-w]\}\space\space \\or \space\space OR_{1\leq w\leq k-1} \{dp[i][j+k-w][w]\space\space and\space\space  dp[i+w][j][k-w]\}
   $$

3. 初始条件和遍历顺序

   初始条件是$k=1,i,j\in[0,n-1]$

   遍历顺序是从转移方程看出来的，得到$dp[i][j][k],i,j\le n-k$之前，$dp[i'][j'][w],i\le i'\le i+w,j\le j'\le j+w, 1\le w\le k-1$一定都要求出来。

   因此循环嵌套是

   ```pseudocode
   for k in range(1, n+1):
   	for i in range(0, n):
   		for j in range(0, n):
   			// do something
   ```

4. 答案是``dp[0][0][n]``

```python
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        n1 = len(s2)
        if n1 != n:
            return False
        # dp = [[[False] * (n+1)] * n] * n
        
        dp = [[[False] * (n+1) for _ in range(n)] for _ in range(n)] 
        for i in range(0, n):
            for j in range(0, n):
                dp[i][j][1] = (s1[i]==s2[j])
                # print(dp[i][j][1])

        for k in range(2, n+1):
            for i in range(0, n-k+1):
                for j in range(0, n-k+1):
                    for w in range(1, k):
                        if dp[i][j][w] and dp[i+w][j+w][k-w]:
                            dp[i][j][k] = True
                            break
                        if  dp[i][j+k-w][w] and dp[i+w][j][k-w]:
                            dp[i][j][k] = True
                            break
        return dp[0][0][n]
```

#### 最后：一个小问题

我在题解中有时使用的是S和T互为扰乱字符串。还是要在最后说明一下。

T为S的扰乱字符串，那么S是否为T的扰乱字符串？从扰乱字符串的定义来看应该是显然的。因为每个操作都是可逆的，直接逆向按照S->T的操作步骤就可以从T得到S。

## 子数组问题

#### LC523. 连续的子数组

[题目链接](https://leetcode-cn.com/problems/continuous-subarray-sum/)

#### 方法1：优化的暴力

用动态规划方法存储了前缀和，时间$O(n^2)$，空间$O(n)$

注意dp数组的下标从0~n，因为没有任何数时和为0

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]+nums[i-1]
        # print(dp)
        
        for i in range(1, n+1):
            for j in range(i + 1, n+1):
                sub = dp[j] - dp[i-1]
                if k == 0 and sub == 0:
                    return True
                elif k != 0 and sub % k == 0:
                    return True
        return False

```

#### 方法2：hashmap

如果前缀和``sum[0:i]``与前缀和``sum[0:j]``对数``k``的模相同，那么一定有``sum[i:j]``能够被``k``整除

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        hashmap = dict()
        hashmap[0] = -1
        s = 0
        for i in range(0, n):
            s += nums[i]
            if k != 0:
                s = s % k
            if s in hashmap.keys():
                if i - hashmap[s] > 1:
                    return True
            else:
                hashmap[s] = i;
        return False
```

### LC1147. 段氏回文

[题目链接](https://leetcode-cn.com/problems/longest-chunked-palindrome-decomposition/)

#### 方法1：双指针+贪心
双指针+贪心，算是比较巧妙吧，感觉这样解这题不算hard。

段氏回文本质还是回文，以ghabciabcgh=(ghh)(abc)(i)(abc)(ghh)为例，既然要分割得到的段数最多，那么就在发现了一段回文后就记录下来。确定首尾两端相同的算法是：i从前往后遍历，j固定不动，当text[i] == text[j]时，检查pre_i\~i这段子串与j-(i-pre_i)\~j这段子串是否相同，若相同则更新答案（由于是段数），同时要更新i, pre_i, j；若不相同，则i往后移动一位，继续找下一个满足text[i] == text[j]的i。

我们看看代码何时退出循环。

+ 一种坏情况是，直到i == j时才有text[i] == text[j]。当段数为奇数的时候从这里退出循环。比如(ghh)(abc)(i)(abc)(ghh), (merchant)
+ 另一种情况是，i > j，这种情况下双指针最后一次更新后交错。当段数为偶数的时候从这里退出循环。比如(abc)(abc)

做完这题的心得有两点：

+ 算法题说难也难，说容易也容易。归根到底是：如果是人来做，怎么解决这个问题？然后是，该怎么编程让计算机执行我的想法？
+ 不要被问题的难度和标签束缚，刷题后期尽可能跟着自己的感觉思考，毕竟面试时肯定要自己想出条明路的。

我的代码：

```python
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        i, pre_i = 0, -1
        ans = 0
        j = n - 1
        while i <= j:
            while text[i] != text[j]:                
                i += 1  
            if i == j:
                ans += 1
                break
            elif i < j:              
                l = i - pre_i
                flag = True
                for k in range(0, l):
                    if text[j - k] == text[i - k]:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    pre_i = i
                    i += 1
                    j = j - l
                    ans += 2
                else:
                    i += 1
            else:
                break
        return ans
```

![image.png](https://pic.leetcode-cn.com/fc8fcb4bbdc45a4cecefb0ab7b012337fb02c782b56ecc6e0d015452a26494a5-image.png)

看到的大佬的代码：

不得不说我虽然语言用的是python，可写码习惯还停留在C++的层面上……

```python
class Solution:
    def longestDecomposition(self, S):
        res, l, r = 0, "", ""
        for i, j in zip(S, S[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res
```

不过刷题是训练算法思维的，倒也能接受吧。

#### 方法2：动态规划

