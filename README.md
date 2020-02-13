# Code Tricks For Python

> 记录我收集和使用的一些 **有趣**、**实用**、**优雅** 的 python 代码片段. 
>
> 主要目的是备忘与分享.



#### 目录结构

- [**命令行**](#命令行)
  - [非交互式执行代码](#非交互式执行代码)
  - [简易HTTPServer](#简易HTTPServer)

- [**一行代码**](#一行代码)
  - [最值](#最值)
  - [逆序](#逆序)
  - [碾平](#碾平)
  - [真假](#真假)
  - [去重](#去重)
  - [时间戳](#时间戳)
  - [彩蛋攻击](#彩蛋攻击)
  - [执行代码](#执行代码)
  - [join连接](#join连接)
  - [简易判断](#简易判断)
  - [条件过滤](#条件过滤)
  - [排序技巧](#排序技巧)
  - [字典合并](#字典合并)
  - [列表推导式](#列表推导式)
  - [zip分配生成dict](#zip分配生成dict)
  - [switch-case写法](#switch-case写法)
  - [Format自动解包](#Format自动解包)

- [**代码片段**](#代码片段)
  - [从右向左替换字符串](#从右向左替换字符串)

- [**相关内容**](#相关内容)
  - [PyTricks](https://github.com/brennerm/PyTricks)
  - [wtfpython](https://github.com/satwikkansal/wtfpython)
  - [code-snippets-python](https://github.com/binderclip/code-snippets-python)
  - [writing_solid_python_code](https://l1nwatch.gitbooks.io/writing_solid_python_code_gitbook/)



## 命令行

#### 非交互式执行代码

```python
# code-1
python -c "import os;os.popen('calc')"

# note-1
打开计算器(Windows 操作系统)


# code-2
python -m timeit -n 1 -r 1 -s "import os" "import platform" "print(platform.system())" "os.popen('calc')"

# output-2
Windows
1 loops, best of 1: 401 msec per loop

# note-2
最后会打开计算器(Windows 操作系统)
-m 运行Python内置模块，-n -r -s 都是timeit的命令行
timeit是一个计时运行代码的模块，可以用来测试算法速度
-n 设定每组运行轮数，-r 设定定时器重复组数，-s 后面的第一个字符串是初始化代码，只运行一遍
以上代码会运行1组，在组内的1次运行中求平均值，取这1组的最好成绩
参考：https://www.cnblogs.com/hengyumo/p/10617018.html
```



#### 简易HTTPServer

```python
# code
python2 -m SimpleHTTPServer 53
python3 -m http.server 53

# note
监听的默认地址是 0.0.0.0, 对外开放, 可目录浏览
```



## 一行代码

#### 最值

```python
# code heapq.nsmallest/heapq.nlargest
import heapq
print(heapq.nlargest(2, [{'S': 5, 'H': 3}, {'S': 7, 'H': 1}, {'S': 0, 'H': 2}], key=lambda x: x['S']))

# output
[{'H': 1, 'S': 7}, {'H': 3, 'S': 5}]

# note
取最大/最小的 N 个值
```



#### 逆序

```python
# code-1 reversed 逆序
print(list(reversed(['L', 'G', 'PK'])))

# output-1
['PK', 'G', 'L']


# code-2 Slice 逆序
print(['L', 'G', 'PK'][::-1])

# output-2
['PK', 'G', 'L']
```



#### 碾平

```python
# code
s = [1, [2, [3, [4, [5, 6], 7], 8], (9, 0)]]
f = lambda x: [y for _x in x for y in f(_x)] if isinstance(x, (list, tuple)) else [x]
print(f(s))

# output
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# note
for _x in x 对于x这个list/tuple中的每个元素
y for y in f(_x) 对以上每个元素获取碾平后的列表并去掉括号拼接起来
```



#### 真假

```python
# code for python2
True -= 1
print(True)
print(True == False)

# output
0
True

# note
python 2.x 中, True 和 False 都是变量, 可以被改变
```



#### 去重

```python
# code
array = ['c', 'a', 'c', 'd', 'b', 'b', 'a', 'a', 'f']

print(list(set(array)))

uniq = []
[uniq.append(x) for x in array if x not in uniq]
print(uniq)

print([x for y, x in enumerate(array) if array.index(x) == y])

# output
['a', 'c', 'b', 'd', 'f']
['c', 'a', 'd', 'b', 'f']
['c', 'a', 'd', 'b', 'f']

# note
依次对应:
去重但不保序
去重且保序
去重且保序
```



#### 时间戳

```python
# code
import time
print(time.strftime("%Y%m%d-%H:%M:%S", time.localtime(time.time())))

# output
20190101-17:12:14

# note
strftime 就是string_format_time的意思
```



#### 彩蛋攻击

```python
# code for python2
[reload(__import__("YW50aWdyYXZpdHk=".decode("base64"))) for x in range(666)]

# code for python3
[__import__("imp").reload(__import__("antigravity")) for x in range(666)]

# note
一个内置彩蛋模块的"拒绝服务攻击", 谨慎运行!
```



#### 执行代码

```python
# code
exec("print('love ' + s)", {'s': 'peace'})

# output
love peace
```



#### join连接

```python
# code
print("+".join(['L', 'G', '007']))

# output
L+G+007
```



#### 简易判断

```python
# code-1
print('bingo' if 1 > 2 else 'miss')

# output-1
miss


# code-2
print("\n".join([(str(x) + ' bingo') if not x % 2 else str(x) + ' miss' for x in range(10)]))

# output-2
0 bingo
1 miss
2 bingo
3 miss
4 bingo
5 miss
6 bingo
7 miss
8 bingo
9 miss
```



#### 条件过滤

```python
# code
print(filter(lambda x: "T" in x, ["TIT", "YoY"]))

# output
['TIT']
```



#### 排序技巧

```python
# code-1
import heapq
k = [2, 6, 1, 5, 3, 4]
print(heapq.nsmallest(len(k), k))

# output-1
[1, 2, 3, 4, 5, 6]

# note-1
从小到大排序


# code-2
print(sorted(['LG', 'cdn', 'dll', 'BBQ', 'afun'], key=lambda x: (len(x), x)))

# output-2
['LG', 'BBQ', 'cdn', 'dll', 'afun']

# note-2
先按长度、再按 ascii 值从小到大依次排序


# code-3
from collections import OrderedDict
d = {'apple': 1, 'orange': 3, 'banana': 4, 'tomato': 2}
print(OrderedDict((x, y) for x, y in sorted(d.items(), key=lambda x: x[1])))

# output-3
OrderedDict([('apple', 1), ('tomato', 2), ('orange', 3), ('banana', 4)])

# note-3
无序字典变有序字典 (按 value 排序)
```



#### 字典合并

```python
# code-1
d = {'a': 1}
d.update({'b': 2})
print(d)

# output-1
{'a': 1, 'b': 2}


# code-2
d1 = {'a': 1}
d2 = {'b': 2}
print(dict(d1, **d2))

# output-2
{'a': 1, 'b': 2}

# note-2
这种方法要求d1与d2的key的数据类型必须相同！


# code-3
d = {'a': 1}
d['b'] = 2
print(d)

# output-3
{'a': 1, 'b': 2}
```



#### 列表推导式

```python
# code
print([x for x in 'LandGrey' if ord(x) > ord('d')])

# output
['n', 'r', 'e', 'y']
```



#### zip分配生成dict

```python
# code
print(dict(zip('AABCD', xrange(5))))

# output
{'A': 1, 'C': 3, 'B': 2, 'D': 4}

# note
本质 dict(list([(k1, v1), (k2, v2)]), ...)
```



#### switch-case写法

```python
# code
def switch(case):
    return {
        0: ">",
        1: "<",
        2: "="
    }.get(case, "?")


print(switch(1))

# output
<
```



#### Format自动解包

```python
# code
t = [{'protocol': 'https'}, 'landgrey.me', '443']
print("{0[0][protocol]}://{0[1]}:{0[2]}".format(t))

# output
https://landgrey.me:443
```



#### Counter统计词频
```python
# code-1
from collections import Counter
import re
print(Counter(filter(lambda x: x, re.split(r" |,|\.|!|\?",
	"Have you ever hello world? hello world! Yes, hey hey."))).most_common(3))

# output-1
[('hey', 2), ('world', 2), ('hello', 2)]

# note-1
re.split('<pattern>', '<string>') 可以通过正则表达式使用多个字符分割
Counter(<Iterator>) 可以统计列表元素出现的频率


# code-2
from collections import Counter
print(Counter(i.strip(".?!") for i in "Have you ever hello world? hello world! Yes, hey hey.".split()))

# output-2
Counter({'world': 2, 'hello': 2, 'hey': 2, 'Yes,': 1, 'ever': 1, 'Have': 1, 'you': 1})

# note-2
可以使用strip达到去除标点的目的，与1中效果相同
```


## 代码片段

#### 从右向左替换字符串

```python
# code 
def rreplace(self, old, new, *max):
    count = len(self)
    if max and str(max[0]).isdigit():
        count = max[0]
    return new.join(self.rsplit(old, count))

print rreplace("lemon tree", "e", "3")
print rreplace("lemon tree", "e", "3", 1)

# output
l3mon tr33
lemon tre3
```



## 相关内容

- [**PyTricks**](https://github.com/brennerm/PyTricks)
- [**wtfpython**](https://github.com/satwikkansal/wtfpython)

- [**code-snippets-python**](https://github.com/binderclip/code-snippets-python)
- [**writing_solid_python_code**](https://l1nwatch.gitbooks.io/writing_solid_python_code_gitbook/)

