#任一个英文的纯文本文件，统计其中的单词出现的个数
#python的内建模块collections

import collections
"""
#namedtuple:自定义的tuple对象
Point = collections.namedtuple('Point', ['x', 'y'])
Circle = collections.namedtuple('Circle',['x', 'y', 'r'])

p = Point(1, 2)
c = Circle(1, 1, 4)
print(p.x, p.y)
print(c.r)

#deque:双向列表,appendleft,popleft,通list比较
q = collections.deque([1, 2, 3])
q.append(4)
q.appendleft(5)
print(q)
print(q[0])

#defaultdict:通dict字典相比较
dd = collections.defaultdict(lambda: 'N/A')
dd['name'] = 'Jhon'
dd['age'] = 23
print(dd['name'], dd['age'])#Jhon
print(dd['sex'])#N/A

di = dict({'name': 'Jhon', 'age': 23})
print(di['name'], di['age'])
try:
    print(di['sex'])
except Exception as e:
    print("except!")

#OrderedDict:按key的插入顺序排列
od = collections.OrderedDict([('x',1),('z', 3),('y', 2)])
print(od)
print(od['z'])

#ChainMap,argparse:
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431953239820157155d21c494e5786fce303f3018c86000

#Counter:简单的计数器
#c = collections.Counter()
string = 'hello world!'
c = collections.Counter(string)#输出：Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})
#for ch in string:
#    c[ch] = c[ch] +1
print(c) #输出：Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})
"""
#0004
with open('F:\wallPaper\\forTest\eng.txt', 'r') as fp:
    #一行一行的读
    ans = fp.read().split('\n')#split得到的是一个list
    #print(ans)
    #一行一行的处理
    answer = 0
    res = []
    #res.extend('cat')#['c', 'a', 't']
    for i in ans:
        ans_list = i.split(' ')
        #print(ans_list)
        answer = answer +len(ans_list)
        res.extend(ans_list)
    print(answer)#正确答案是17；输出：17
    print(res) #标点符号没有处理？！？！？！
    c = collections.Counter(res)
    print(c)