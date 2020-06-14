# Parser

与表达式解析有关的题目多半要用栈或者递归来解决（我习惯用栈+迭代），也有直接用Python+正则表达式的。数据结构课程栈一章，中缀表达式求值算法可以供参考（核心在于两个栈，一个放操作数，一个放操作符）

[这里](https://leetcode-cn.com/problems/number-of-atoms/solution/python-di-gui-xia-jiang-fen-xi-by-mbinary/)列出了LC上关于解析的常见题目

## LC726. 原子的数量

[题目链接](https://leetcode-cn.com/problems/number-of-atoms/)

### 方法1：栈+迭代
如果没有听说过中缀表达式求值的算法，推荐一看，对于本题的理解很有帮助。

还是那句话，写代码的前提要知道是我们自己遇到这个问题怎么解决。

对于给定字符串``f``，我们无非要做以下三件事：

1. 提取元素名称``atom``
2. 提取紧跟着的元素个数``cnt``
3. **根据括号关系计算元素出现的总次数``num``**

对上述第三点，如果我知道**两个括号之间所有的元素和他们在括号内的个数**，再**乘以括号后紧跟着的数字**，不就能够解决了吗？

我们设置两个容器，一个是括号栈``parentheses_stack``，用来匹配括号，另一个是一个元素信息列表``element_info``，用来记录字符串``f``中出现的元素的名称、当前个数、当前被几个括号包围（之所以不像中缀表达式求值那样设计两个栈，是因为在表达式求值的场景中，操作符有目数的限制，因此对放置操作数的容器只有末尾的pop和push操作，而且最后一定只有一个``value``做结果，因此用只栈放置操作数是可以的）

可能有人会疑惑为什么这里要记录某元素当前被几个括号包围，实际上正是通过这个数和括号栈（只放置了``(``括号）的中的括号个数的大小关系，判断元素信息列表中的哪些元素的个数在本轮中需要乘以括号后的数字（这也是我认为最比较巧妙的一个点）。

以K4(ON(SO3)2)2为例，演示过程：

![726_1.png](https://i.loli.net/2020/06/15/8jdrpYJQZTFaLW6.png)

![726_2.png](https://i.loli.net/2020/06/15/xJpa5u7YNw2hoOv.png)

![726_3.png](https://i.loli.net/2020/06/15/q84lJBPszdLrfyG.png)

![726_4.png](https://i.loli.net/2020/06/15/eocvPaz7ndkwJHb.png)

### 代码

```python
class Solution:
    def countOfAtoms(self, f: str) -> str:
        i = 0
        n = len(f)
        element_info = list()   # list of [element_name, number_of_element, number_of_parentheses]
        parentheses_stack = list()
        # atom = str()
        distribution = dict()
        while i < n:
            # 如果遇到的是字母
            # 如果遇到的是大写字母
            atom = str()
            if f[i].isupper():
                atom = f[i]
                i += 1
            # 跟着小写字母
            while i < n and f[i].islower():
                atom += f[i]
                i += 1
            cnt = str()
            # 如果后面有数
            if i < n and f[i].isdigit():
                # 遍历所有的数
                while i < n and f[i].isdigit():
                    cnt += f[i]
                    i += 1
                element_info.append([atom, int(cnt), len(parentheses_stack)])
            # 如果后面没有数
            else:
                # 如果前面的if都执行过（即得到了某一个atom，而不是一开始就从(开头）
                # print("i, atom:", i, atom)
                if len(atom) and len(cnt) == 0:
                    element_info.append([atom, 1, len(parentheses_stack)])
                if i < n and f[i] == '(':
                    parentheses_stack.append('(')
                    i += 1
                elif i < n and f[i] == ')':
                    i += 1
                    cnt = str()
                    if i < n and f[i].isdigit():
                        # 遍历所有的数
                        while i < n and f[i].isdigit():
                            cnt += f[i]
                            i += 1
                        cnt = int(cnt)
                    else: cnt = 1
                    # parentheses_stack.pop()
                    for k in range(len(element_info)-1,-1,-1):
                        if element_info[k][2] == len(parentheses_stack):
                            element_info[k][1] *= cnt
                            element_info[k][2] -= 1
                        else:
                            break
                    parentheses_stack.pop()
        
        # print(element_info)
        for ele in element_info:
            if ele[0] in distribution:
                distribution[ele[0]] += ele[1]
            else:
                distribution[ele[0]] = ele[1]

        # print(distribution)
        lst = sorted(distribution.items(), key=lambda obj: obj[0])
        # print(lst)
        ans = str()
        for name, number in lst:
            if number == 1:
                ans += name
            else:
                ans += name + str(number)
        return ans
           
```
![image.png](https://pic.leetcode-cn.com/dc8aedcff9775125fa70ebe210f00fad401c474e02091289fad9c29dd1df552c-image.png)

### 方法2：递归（官方题解）
