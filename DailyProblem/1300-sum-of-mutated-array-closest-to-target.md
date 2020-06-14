### 解题思路
P.S. 代码写麻烦了……其实代码第二步和第三步可以合并的hhh，直接一次顺序遍历就好了

自己在解题的时候并没有想到二分法。虽然代码长了点，但是基本的思路很容易理解！算法能够AC，如果有漏洞欢迎指出。

对于这种求和更接近的要求，首先想到的肯定是要排序（**代码第一步**）（可能与前几天做了2/3/4数之和的题目有关，直接想到了类似的方法）。对于从小到大排序后的数组，肯定从某个下标开始，左边的数不变，右边的数全部更改为答案。那么关键就在于找到这个下标、进而找到答案。

怎么找到这个下标id呢？首先从0~id的子数组和肯定不会超过target。那么先找到这样的临界下标，我们命名为k（**代码第二步**）。

这里有一些关于k的特殊情况，在代码里面详细说明了。

值得讨论的是k的一般情况（**代码第三步**），即``sum[0...k] <= target``而``sum[0...k+1] > target``. 既然分割点下标肯定在0\~k，那么就对这部分进行反向遍历（即``i = k, k - 1, ..., 0``），遍历的过程中我们利用子数组和s（s不用重新求，直接从**代码第一步**所得s中依次减去``arr[i+1]``就好）与``target``，求出当全数组和最接近``target``时，理论上i+1\~n-1部分应该取什么值(即``(target - s) / (n- 1 - i)``的上下取整``upper``与``lower``)。但这只是理论上的值，为了使得其符合题目规则，我们需要考虑到这两个数与``arr[i]``、``arr[i+1]``的大小关系。我们选择的条件是（以``upper``为例）：当且仅当``arr[i] <= upper``时，才考虑它可能是答案（因为分割的下标在本次遍历中不可变）；其次，``upper``最终更新为``upper``和``arr[i+1]``中较小的那个数（因为如果``upper`` > ``arr[i+1]``会导致``arr[i+1]``不能更新为``upper``的数值）（P.S. ``upper = min(upper, arr[i+1])``后依然满足``upper >= arr[i]``，因为``arr[i+1]>=arr[i]``）

成功了吗？我们是不是还漏掉了什么呢？上面的遍历依次将数组分割为``arr[0...i]``与``arr[i+1...n-1]``且$i\in[0,k]$，也就是说左边的数组长度最短为1。实际上左边的数组可能长度为0。一种解决的方法是在做题之前就在List中添加一个0做首位哨兵（因为``arr[i]>=1``），另一种解决的方法是再人为增加一次“循环”。

### 代码

```python3
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # 第一步：排序
        arr.sort()
        s, n = 0, len(arr)
        # 如果arr只有一个数，特判解决
        # 以免后面对数组的处理会越界
        if n == 1:
            if arr[0] > target:
                return target
            else:
                return arr[0]
        # 第二步：找到这样的k，使得sum[0...k] <= target而sum[0...k+1] > target
        k = -1
        for i in range(0, n):
            s += arr[i]
            if s <= target:
                k = i
            else:
                break
        # 如果整个数组的和不超过target
        # 直接返回数组最后一个元素即可
        if s <= target:
            return arr[-1]
        # 如果整个数组的和超过target
        else:
            # 如果第一个数就大于了target（表现为k = -1无法更新）
            # 那么直接在target / n的上下取整里找答案
            if k == -1:
                quotient = target / n
                if target - n * math.floor(quotient) > n * math.ceil(quotient) - target:
                    return int(math.ceil(quotient))
                else:
                    return int(math.floor(quotient))
            # 否则从0~k这一段中找到分割点id，和答案ans
            # 代码第三步
            else:
                diff, ans = float('inf'), float('inf')
                for i in range(k, -1, -1):
                    s -= arr[i+1]
                    quotient = (target - s) / (n - 1 - i)
                    lower = math.floor(quotient)
                    upper = math.ceil(quotient)
                    if arr[i] <= lower:
                        lower = min(lower, arr[i+1])
                        # 更新答案的规则
                        # 只有当diff_小于当前diff时才更新diff和ans
                        # 当diff_等于当前diff时，ans更新为ans和lower中较小的数
                        diff_ = abs(target - s - lower * (n - i - 1))
                        if diff_ < diff:
                            diff = diff_
                            ans = lower
                        elif diff_ == diff:
                            ans = min(ans, lower)
                    
                    if arr[i] <= upper:
                        upper = min(upper, arr[i+1])
                        # 更新答案的规则同上
                        diff_ = abs(s + upper * (n - i - 1) - target)
                        if diff_ < diff:
                            diff = diff_
                            ans = upper
                        elif diff_ == diff:
                            ans = min(ans, upper)
                # 人为增加一次循环
                s -= arr[0]     # assert: s == 0
                quotient = target / n
                lower = math.floor(quotient)
                upper = math.ceil(quotient)
                
                lower = min(lower, arr[0])
                diff_ = abs(target - s - lower * n)
                if diff_ < diff:
                    diff = diff_
                    ans = lower
                elif diff_ == diff:
                    ans = min(ans, lower)
                
                upper = min(upper, arr[0])
                diff_ = abs(s + upper * n - target)
                if diff_ < diff:
                    diff = diff_
                    ans = upper
                elif diff_ == diff:
                    ans = min(ans, upper)
                return ans
```
![image.png](https://pic.leetcode-cn.com/480547945ba49e0b3c0afa993d78bf2e68577d419a5f02c56ad78065a22348ec-image.png)
