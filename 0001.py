"""
做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
"""
#文件读写、JSON
import random,string
"""
list1 = ["hello", "world", "error"]
str = "sword"
print(random.choice(str))#r;sword中的一个字母
print(random.choice(list1))#world；list1中的一个元素
"""
def toStr():
    chars = string.ascii_letters + string.digits#string模块下有数字和字母
    #print(chars)
    str = ""
    for i in range(8):
        str = str + random.choice(chars)
    return str

if __name__ == '__main__':
    """
    fp = open("F:\wallPaper\\forTest\\ans.txt", "r")#"wb"模式是读写二进制文件，需要对字符串进行编码，暂时没会
    
    for i in range(200):
        charstr = toStr()
        #print(charstr)
        fp.write(charstr+'\n')
    """
    """
    print(fp.tell())
    fp.seek(10)#下一行
    print(fp.readline())
    """
    """
    #for i in range(3):
    i = 0
    for line in fp:
        print(fp.readline(), end="")
        i = i+1
    print(i)
    
    fp.close()
    """
    #用with关键字处理文件，这样发生异常也没关系，会自动关闭文件
    #with open("F:\wallPaper\\forTest\\ans.txt", "r") as fp:
    #    read_data = fp.readline()
    #print(read_data)

"""
#JSON
import json
#dumps可以格式化所有的基本数据类型为字符串

#dump和dumps
data1 = json.dumps([]) #列表
print(data1, type(data1))
data2 = json.dumps(2) #数字
print(data2, type(data2))
data3 = json.dumps('3') #字符串
print(data3 ,type(data3))
dict = {"name": "Tom", "age": 23} #字典
data4 = json.dumps(dict)
print(data4, type(data4))

with open("F:\wallPaper\\forTest\\testJSON.txt", "w", encoding="utf-8") as f:
    #indent,格式化保存字典，默认为None，小于0为零个空格
    #f.write(json.dumps(dict, indent=4))
    json.dump(dict, f, indent=4) #传入文件描述符，和dumps一样的结果

dict = '{"name": "Tom", "age": 23}' #json输入必须是str,byte,bytearray
#dict2 = {"name": "Tom", "age": 23}
data1 = json.loads(dict)
#print(dict2, type(dict2))
print(data1, type(data1))

with open("F:\wallPaper\\forTest\\testJSON.txt", "r") as f:
    data2 = json.loads(f.read())
    print(data2, type(data2))
    f.seek(0)#f.seek(0)
    data3 = json.load(f)
    print(data3, type(data3))
    print(data3['name'])
"""
import json
#因为json只能读取一个文档对象，有两个解决办法
#1、单行读取文件,一次读取一行文件。
#2、保存数据源的时候，格式写为一个对象。
with open("F:\wallPaper\\forTest\\testJSON.txt", "r") as f:
    json_data = json.loads(f.read())
    print(json_data)
    print(json_data['dict'])
    print(json_data['dict'][0])
    print(json_data['dict'][1])
#    for line in f:
#        line = line.strip()
#        if len(line) != 0:
#            print('line:' + line)
#            json_data = json.loads(line)
#            print(json_data)
