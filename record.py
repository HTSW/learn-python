# -*- coding: utf-8 -*-
# split 按照指定的分隔符对字符串进行分割
str.split(str='',num=string.count(str))
#str -- 分隔符
#num -- 分割次数
a = ('/usr/lib/system/systemd')
a.split('/',1)
a.split('/',2)

# 循环判断
name = input('Please input your name:')
while True:
    s1 = input('Please input your score of last year:')
    if s1.isdigit():
        s1 = float(s1)
        while True:
            s2 = input('Please input score of this year:')
            if s2.isdigit():
                s2 = float(s2)
                p = (s2 - s1)/s2 * 100
                # format method have two
                print('Hi {0}, your score update {1:.1f}% in this year'.format(name,p))
                print ('Hi %s, your score update %.1f%% in this year' % (name,p))
                break
            else:
                print ('You must input number , Please try again')
        break
    else:
        print('Your input invalid,Please input number ,try again')

# 生成器
# 把一个列表生成式由[]变成()，就可以变成一个生成器
# 生成器保存算法，不马上运算，而是在调用时才运算，一般用next()来调用，或者使用for循环来迭代
# 如果一个函数中有yield ，这个函数就是个生成器

# 迭代器

# 可用于for循环的对象称之为可迭代对象
# 可用next()函数调用返回下一个值的对象为迭代器
# 生成器都是迭代器
# list，dict，str等是可迭代对象，但不是迭代器，使用iter()可让他们变成迭代器

# 递归函数
class Tower(object):
    def __init__(self):
        self.counter = 0

    def hanoi(self, n, org, aux, dst):
        if n == 1:
            self.counter += 1
            print('{0}->{1}'.format(org, dst))
        else:
            self.hanoi(n - 1, org, dst, aux)
            self.hanoi(1, org, aux, dst)
            self.hanoi(n - 1, aux, org, dst)

def homework(*args):
    tower = Tower()
    print('移动步骤如下:')
    tower.hanoi(*args)
    print('总共移动次数为: {0}'.format(tower.counter))

homework(100,'a','b','c')


# 切片and递归函数
def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    elif s[-1:] == ' ':
        return trim(s[:-1])




#　迭代和递归函数
def findMinAndMax(L):

    if len(L) == 0:
        result = None,None
    elif len(L) == 1:
        result = L[0],L[0]
    #     边界条件
    elif len(L) == 2:
        if L[0] < L[1]:
            result = L[0], L[1]
        else:
            result = L[1], L[0]
    else:
        # 每次递归都会用L[0]和minimum,maximum进行比较得出一个result
        minimun, maximum = findMinAndMax(L[1:])
        print(minimun,maximum)
        if minimun > L[0]:
            result = L[0],maximum
        elif maximum < L[0]:
            result = minimun,L[0]
        else:
            result = minimun,maximum
    return result

s=[5,3,8,4,7]
print(findMinAndMax(s))

# 实现过程大致如下
# 5 和 findMinAndMax(3,8,4,7)里面得到的结果对比，但是要得出结果必须执行如下过程
# 3 和 findMinAndMax(8,4,7)里面得到的结果对比，但是要得出结果必须执行如下过程
# 8 和findMinAndMax(4,7)里面得到的结果对比，但是要得出结果必须执行如下过程
# findMinAndMax(4,7)里面得到的结果是minimum=4,maximum=7
#8和(4,7)对比得到的结果是minmum=4,maximum=8
#3和(4,8)对比得到的结果是minimum=3,maximum=8
#5和(3,8)对比得到的结果是minimum=3,maximum=8


# 列表生成式
# 要生成的元素放前面，后面跟for循环，最后跟条件
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if not isinstance(x,int) if x != None]



# 生成器，递归，以及杨辉三角
def triangles(n):
    def _triangles(n):
        if n == 1:
            return [1]
        else:
            pre_line = _triangles(n - 1)
            line = [pre_line[i] + pre_line[i + 1] for i in range(len(pre_line) - 1)]
            line.insert(0, 1)
            line.append(1)
        return line
    for y in range(n):
        x = _triangles(y+1)
        yield x


# map 及 reduce
# map 接受一个函数，作用与每个元素，然后将新结果返回
# reduce 接受一个函数，将元素中的两个参数计算，然后把结果继续和下一个元素做累计计算
def str2float(s):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    l = s.split('.')
    def char2num(s):
        return DIGITS[s]

    def to_int(x,y):
        return x * 10 + y

    def to_float(f):
        n = 1
        i = 0
        while i < len(l[1]):
            n = n * 10
            i = i + 1
        return f / n

    if '.' not in s:
        result = reduce(to_int,map(char2num,l[0]),0.0)
    else:
        result = reduce(to_int,map(char2num,l[0]))+to_float(reduce(to_int,map(char2num,l[1])))
    return result


# filter
# 接受一个函数，依次作用与每个元素，然后根据返回值是True还是false决定是保留还是丢弃该元素
def _odd_iter():
    n = 1
    while True:
        yield n
        n = n + 1


def _is_palindrome(n):
    return str(n) == str(n)[::-1]


def palindrome():
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_is_palindrome,it)



for n in palindrome():
    if n < 200:
        print(n)
    else:
        break


# sorted
# 接受一个函数，作用于list中的每一个元素上
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return sorted(t,key=lambda name: name[0])

def by_score(t):
    return sorted(t,key=lambda score: score[1],reverse=True)


# 返回函数及闭包
def createCounter():
    def f():
        n = 1
        while True:
            yield n
            n = n + 1
    sum = f()
    def counter():
        return next(sum)
    return counter

# 匿名函数
# lambda 匿名函数，冒号前面为函数参数，右边为返回值
print(list(filter(lambda n: n % 2 == 1,range(1,20))))

def build(x,y):
    return lambda: x*x+y*y

s = build(3,4)

# 装饰器
def metric(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start = time.clock()
        execfunc = func(*args,**kwargs)
        end = time.clock()
        duration = end-start
        print('{0} execued in {1}'.format(func.__name__,duration))
        return execfunc
    return wrapper

@metric
def fast(x,y):
    time.sleep(0.0012)
    return x + y

f=fast(11,22)
print(f)

@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x * y * z

s = slow(11,22,33)
print(s)


# 偏函数
其实就是函数调用的时候，有多个参数 参数，但是其中的一个参数已经知道了，我们可以通过这个参数重新绑定一个新的函数，然后去调用这个新函数
通常用于函数需要多次调用同一个参数的时候

import tkinter
root=tkinter.Tk()

这个函数就是下面那个偏函数的定义版，随便用那个都可以，但是相对而言，还是偏函数更方便，更简洁
#def mybutton(**kw):
#    return tkinter.Button(root,bg='blue',fg='white',**kw)

mybutton=partial(tkinter.Button,root,bg='blue',fg='white')
b1=mybutton(text='nihiao')
b2=mybutton(text='buhao')
b1.pack()
b2.pack()
root.mainloop()



# class 及 instance

class Person(object):
# 这里就是初始化你将要创建的实例的属性
    def __init__(self,hight,weight,age):
        self.hight = hight
        self.weight = weight
        self.age = age

# 定义你将要创建的实例所有用的技能
    def paoniu(self):
        print('you have')

    def eat(self):
        print('you can eat')

# 开始创建实例
zhangsan=Person(170,50,29)
lisi = Person(175,100,30)

# 你的实例开始使用它的技能
zhangsan.paoniu()
lisi.eat()


# class 访问限制

# class 内部的变量加上__变成私有变量,只有内部可以访问，外部无法访问
# 如果看到只有一个下划线_的变量，这样的实例，外部是可以访问的，但是意思是虽然我可以被访问，但是请视我为私有变量，不要随意访问

class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def __check_gender(self):
        if self.__gender not in ('male','female'):
            raise ValueError('bad')

    def get_gender(self):
        self.__check_gender()
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender
        self.__check_gender()


# class 的继承和多态

# 多态，直白点说，多个类型的对象拥有同样的方法，当然这不准确，可以从这个角度去想，比如，三种不同形状的按钮，但是，他们有一样的作用，就是click()
# 假若你现在有个编辑器，你根本不知道用户将要打开什么类型的文件(可能是pdf，word，excel，ppt...)
# 为此，我们创建一个Document类型的父类，有一个show()的方法
# 然后，我们分别创建pdf，word类型的class，继承Document，并且有它自己的show()方法
# 这样我们就可以打开不同类型的文件了，这就是多态了
# 说到多态，还不得不说一个鸭子类型，所谓鸭子类型，其实就是只要这个对象"看起来像鸭子，走起来像鸭子，那它就是个鸭子"，什么意思呢，看下面的例子
# 在python中，对象的有效语义并不是由继承特定的类或实现特定的接口，而是由当前方法和属性的集合决定的。
# 鸭子类型通常得益于不测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用
# 其实多态在python表现的并不那么cool，python中更多的是鸭子类型
# 多态更多的表现在同一个方法，可以对多种类型进行操作，比如说 + 可以对数字进行操作，也可以对字符串进行操作，这就是多态的体现了
class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'


class Word(Document):
    def show(self):
        return 'Show word contents!'
# 这个Job就是有个show()使它看起来像Document，所以，它就是个看起来像鸭子的"鸭子"，但是，如果你通过isinstance(Job,Document)来判断的话，它实际上不真的是Document类型
class Job(object):
    def __init__(self,name):
        self.name = name

    def show(self):
        return 'Show job contents!'

documents = [Pdf('Document1'),
             Pdf('Document2'),
             Word('Document3'),
             Job('Document4')]

for document in documents:
    print(document.name + ': ' + document.show())


# class 获取对象信息，下面 有个例子

# 首先你有一个command.py文件，内容如下，这里我们假若它后面还有100个方法

class MyObject(object):
    def __init__(self):
        self.x = 9
    def add(self):
        return self.x + self.x

    def pow(self):
        return self.x * self.x

    def sub(self):
        return self.x - self.x

    def div(self):
        return self.x / self.x
# 然后我们有一个入口文件 exec.py，要根据用户的输入来执行后端的操作
from command import MyObject
computer=MyObject()

def run():
    inp = input('method>')

    if inp == 'add':
        computer.add()
    elif inp == 'sub':
        computer.sub()
    elif inp == 'div':
        computer.div()
    elif inp == 'pow':
        computer.pow()
    else:
        print('404')
# 上面使用了if来进行判断，那么假若我的command里面真的有100个方法，那我总不可能写100次判断吧，所以这里我们就会用到python的反射特性，看下面的代码

from command import MyObject

computer=MyObject()
def run(x):
    inp = input('method>')
    # 判断是否有这个属性
    if hasattr(computer,inp):
    # 有就获取然后赋值给新的变量
        func = getattr(computer,inp)
        print(func())
    else:
    # 没有我们来set一个
        setattr(computer,inp,lambda x:x+1)
        func = getattr(computer,inp)
        print(func(x))

if __name__ == '__main__':
    run(10)


# class 模块及类的动态加载

import importlib

imp_module = 'hello'
imp_class = 'ClassA'
ip_module = importlib.import_module('.',imp_module)
ip_module_cls = getattr(ip_module,imp_class)
cls_obj = ip_module_cls()
print(dir(cls_obj))
for attr in dir(cls_obj):
    if attr[0] != '_':
        class_attr_obj = getattr(cls_obj,attr)
        if hasattr(class_attr_obj,'__call__'):
            class_attr_obj()
        else:
            print(attr,' Type:',type(class_attr_obj),' Value:', class_attr_obj)

# 重新加载模块，但原来已经使用的实例还是会使用旧的模块，而新生产的实例会使用新的模块，reload后还是用原来的内存地址。
ip_module = importlib.reload(ip_module)
print(dir(cls_obj))


# class 类属性
# 实例属性和类属性不要使用相同的名字
class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Student.count = Student.count + 1


# __slots__ 绑定限制

# 正常情况下，我们可以给实例绑定属性，也可以个实例绑定方法
# 但是，绑定的属性和方法只对当前实例有效，如果有要为所有实例绑定属性和方法，则可以为类绑定属性和方法
# __slots__ 可以限定绑定的属性
# __slots__ 只对当前类实例起作用，对继承的子类是不起作用的，除非在子类中也定义__slots__，这时候子类运行绑定的属性就是父类+子类的__slots__




# property
@property

#举个例子，现在我们有一个class，可以将温度转化为华氏度
class Celsius(object):
    def __init__(self,temperature = 0):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

man = Celsius()
man.temperature = 37
man.to_fahrenheit()

#然后，有个客户提出需求，要求我们的温度不能低于-273，这时候我们可以将属性temperature隐藏起来，并且可以对参数的输入进行一下检查

class Celsius(object):
    def __init__(self,temperature = 0):
        self.set_temperature(temperature)

    def get_temperature(self):
        return self._temperature

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def set_temperature(self,value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

c = Celsius(-277)
c = Celsius(37)
c.get_temperature()
c.set_temperature(10)

#这时候温度确实被检查，已经不能设置低于-273度了，但是，这时候，我们需要对所有obj.temperature = value 修改成 obj.temperature(value)
#如果代码少还好说，要是多了，那就不得了了，那么有没有既能检查参数，又能像像属性那样的方式来访问方法呢，这时候就要用到@property了

class Celsius(object):
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(fget=get_temperature,fset=set_temperature)

#property() 本身是一个内置的函数，它的签名是property(fget=None,fset=None,fdel=None,doc=None)
#一个property对象有三种方法，getter(),setter(),delete(),对应的fget,fset,fdel
#像我们上面的temperature = property(fget=get_temperature,fset=set_temperature)
#我们可以理解为
temperature = property()
temperature = temperature.getter(get_temperature)
temperature = temperature.setter(set_temperature)

#想想前面学的装饰器，我们就知道了temperature obj通过temperature.getter装饰器来装饰了get_temperature，然后又有了temperature.setter装饰器
#所以，最终我们可以写成如下

class Celsius(object):
    def __init__(self,temperature = 0):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self,value):
        if value < -273:
            raise ValueError('Temperature below -273 is not possible')
        print("setting value")
        self._temperature = value


# 多重继承

# 所谓多重继承，是指python的类可以有两个以上的父类
# 要熟悉多重继承，只要了解结构算法中的拓扑排序即可
# 多重继承的继承关系，按照C3算法得出，通常是从入度为0的位置查起，剪掉入度为0位置的相关边，接着继续查找入度为0的位置，依次重复


# 定制类

# 在我们编写一个新的Python类的时候，总是在最开始位置写一个初始化方法__init__，以便初始化对象，然后会写一个__str__方法，方面我们调试程序。
class Student(object):
    def __init__(self,name):
        self._name = name

    def __str__(self):
        return 'Student object(name: {})'.format(self._name)
    __repr__ = __str__

s = Student('Michael')
print(s)


# 如果我们要写一个生成器类，那么我们就得用到`__iter__`和`__next__`

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 10:
            raise StopIteration()
        return self.a

s = Fib()

for i in s:
    print(i)

# for为了兼容性其实有两种机制，如果对象有__iter__会使用迭代器，但是如果对象没有__iter__，但是实现了__getitem__，会改用下标迭代的方式

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1

    def __getitem__(self, item):
        self.a,self.b = self.b,self.a+self.b
        if self.a > 20:
            raise StopIteration()
        return self.a

s = Fib()
print(s[0])


# __getattr__

# 在没找到属性的情况下调用__getattr__

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path): # __getattr__返回一个Chain类的实例，所以后面继续使用点符访问属性也是可以的，这就是链式调用的本质
        self._path = '{0}/{1}'.format(self._path,path)
        return self
        # return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path

    __call__ = __getattr__
    __repr__ = __str__



print(Chain('/status').users('michael').repos)


# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用 实例名.方法名() 的方式来调用。能不能直接把实例本身当作一个方法调用呢
# 对任何类来说，只需要实现 __call__() 方法，就可以直接对该类的实例进行调用

class Student(object):
    def __init__(self, name):
        self.name = name
    # 当我们取消__call__的注释之后，实例就变成了可被调用的对象了
    # def __call__(self):
    #     print('My name is %s.' % self.name)


s = Student('Michael')
print(callable(s))


# 枚举类
# 枚举成员名称不能重复，但是值是可以重复的
# 标准的Enum枚举是无法进行比较的
# 我们可以使用IntEnum类进行枚举，成员就可以与整数进行比较
from enum import Enum,unique

#1、函数式API调用
# 第一个参数是枚举名称
# 第二个参数是枚举成员名称的源
Month = Enum('Month',('Jan','Feb','Mar'))
for name,member in Month.__members__.items(): # list all enum members,including aliases，既然是map自然就会有items
    print(name,'=>',member,',',member.value)  #value属性是自动赋给成员的int常量，默认从1开始记数


#2、自定义枚举类
@unique  #保证不重复
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
#访问这些枚举类型可以有若干种方法：
day1 = Weekday.Mon
print(day1) #Weekday.Mon
print(day1.value) #1,通过枚举常量获取value
print(Weekday(1)) #Weekday.Mon,通过value获取枚举常量

# 枚举类可以按定义顺序进行迭代
for value in Weekday:
    print(value,value.value)




# 元类

# 元类就是用来创建这些类（对象）的，元类就是类的类，
# 1.拦截类的创建；2.修改类；3.返回修改之后的类
# 除了使用type()动态创建类以外，要控制类的创建行为，就可以使用metaclass。

# type实际上就是一个元类，因此type()函数可以创建class
# 要创建一个class对象，type()函数依次传入3个参数
# 1.class 名称；2.继承的父类集合；3.class的方法名称与函数绑定
def fn(self,name='world'):
    print('Hello,{0}'.format(name))
Hello = type('Hello',(object,),dict(hello=fn))

# 看下面这个例子
class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

# 我们知道在python中一切皆对象
# 那么下面我们的s其实就是一个类对象，它的__name__其实和Foo的__name__是一样的
# 看下面的方法是不是和type创建类有点像？
s = UpperAttrMetaclass('Foo',(object,),{'bar':'bip'})
print(hasattr(s,'bar'))
print(hasattr(s,'BAR'))
print(s.BAR)

class Foo(object,metaclass=UpperAttrMetaclass):
    bar='bip'
print(hasattr(Foo,'bar'))
print(hasattr(Foo,'BAR'))
print(Foo.BAR)
# 最后它们输出的结果其实是一模一样的，这就说明了类其实和我们普通的实例对象差不多，只不过普通实例是通过类创建，而类是通过元类创建
# 而__new__就是用来创建实例的，不论是普通的实例，还是类实例，总之就是个实例

# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；2.类的名字；3.类继承的父类集合；4.类的方法集合。
# 实际上在我们实例化对象时，python默认执行了__new__操作，先创建类实例，然后才使用__init__初始化实例

# python新类允许用户重载__new__和__init__方法。__new__创建类实例，__init__初始化一个已被创建的实例。看下面的代码
class newStyleClass(object):
    def __new__(cls):
        print("__new__ is called")
        return super(newStyleClass, cls).__new__(cls)

    def __init__(self):
        print("__init__ is called")
        print("self is: ", self)

newStyleClass()
# 我们发现__new__函数先被调用，接着__init__函数在__new__函数返回一个实例的时候被调用，并且这个实例作为self参数被传入了__init__函数

# 这里需要注意的是，如果__new__函数返回一个已经存在的实例（不论是哪个类的），__init__不会被调用。看下面的代码
obj = 12
# obj can be an object from any class, even object.__new__(object)

class returnExistedObj(object):
    def __new__(cls):
        print("__new__ is called")
        return obj

    def __init(self):
        print("__init__ is called")

returnExistedObj()

# 错误处理

from functools import reduce
def str2num(s):
    try:
        if '.' not in s:
            return int(s)
        else:
            return float(s)
    except Exception as e:
        raise

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main(s):
    r = calc(s)
    print('{0}={1}'.format(s,r))

a='100 + 200 + 345'
b='99 + 88 + 7.9'

if __name__ == '__main__':
    main(a)
    main(b)



# 调试
# 就调试而言有很多种方式
# assert断言，IDE调试，logging才是终极方案

import logging
# 定义日志级别
logging.basicConfig(level=logging.ERROR)
s = '0'
n = int(s)
# assert n !=0,'n is zero'
# 可以通过-O参数来关闭assert
# 输出错误，或者可以输出到文件
logging.error('n={0}'.format(n))
print(10/n)


# 单元测试
# 我们写好代码之后，往往需要写一些单元测试来测试程序是否满足我们的需求
# 这时候引入python自带的unittest模块，写一个测试模块
# 写一个测试类，从unittest.TestCase继承
# 每一类测试都需要编写一个test_xxx()方法
# 常用的断言是assertEqual()，判断函数返回结果是否和给出的结果相等
# assertTrue(),返回的结果是否为True
# assertRaise(KeyError),期待抛出指定类型的Error，比如说，当一个条件不满足时，抛出KeyError
# 实际例子
# mydict.py
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
            # 这里我们定义了一个AttributeError
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

#mydict_test.py
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    # 另外，我们还可以在单元测试中写两个特殊的方法setUp,setDown,这两个方法会分别在没调用一个测试方法的前后分别执行
    # 比如我们要测试一个跟数据库有关的程序时，就可以在setUp中链接数据库，在setDown中关闭数据库
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        # 断言部分，d.a 是否为1
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        # 断言部分，d是否为一个dict
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        # 这里我们就期待返回我们程序中定义的KeyError
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        # 这里我们就期待返回我们程序中定义的AttributeError
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()


# 写好测试模块后，我们可以使用 python -m unittest mydict_test来直接运行单元测试
# 用这种方法，可以依次批量运行多个单元测试



# 文档测试
# 写了个函数，或者写了个类，具体要怎么使用，可以在注释中说明，然后写个文档测试放在里面，在直接运行命令的时候，执行文档测试
def fact(n):
    """
    Calculate 1*2*3...*n
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    """
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n-1)

if __name__=='__main__':
    import doctest
    doctest.testmod()


# I/O编程

# IO操作有两个数据流input和output，这个是相对内存而言
# IO中有同步IO和异步IO
# 同步IO为，当程序部分代码需要执行一段时间，那么CPU等待着，等这部分代码执行完成后再执行后续的代码
# 而异步IO为，程序需要长时间执行的代码还是做它的事，而CPU继续去执行它后后面的代码
# 而根据通知方式的不同，如果CPU时不时的来查看这段代码是否执行完，则为轮询模式，如果是代码执行完之后，通知CPU，这就是回调模式


# 文件读写

# 如果文件小，直接read即可
# 如果文件大，用read(size)
# readline()一次读取一行
# readlines()一次读取所有内容，并返回一个list，配置文件会用到比较多

# 用with..open..as..代替try...except...finally,关闭io
with open('test.txt','r') as f:
    print(f.read())

# 像open()函数返回的这种带有read()方法的对象，称为file-like object,除了file外，还可以是内存的字节流，网络流，自定义流
# StringIO就是在内存中创建的file-like object,用作临时缓冲

# 如果我们要读取图片，视频，二进制文件，那么用'rb'模式打开即可
with open('video.mp4','rb') as f:
    print(f.read())

# 如果要读取非UTF-8编码的文件，要给open()函数传入一个encoding参数
with open('test.txt','r',encoding='gbk') as f:
    print(f.read())

# 如果我们遇到某些文本中包含了一些非编码的字符，遇到这种情况，我们只需要加上一个errors='ignore'直接忽略掉即可
with open('test.txt','r',encoding='gbk',errors='ignore') as f:
    print(f.read())


# 如果是写入文件，那么就是传入标识符不一样而已，写的时候，传入的标识符是'w'，或者二进制为'wb'，如果是追加文件内容则传入'a'
with open('test.txt','w') as f:
    f.write('nihao')

with open('test.txt','a',encoding = 'utf-8') as f:
    f.write('\nworld!')
# 同样如果要写入特定编码的文件，在open()函数传入encoding指定编码即可
with open('test.txt','w',encoding='utf-8') as f:
    f.write('nihao')


# 替换文本文件中的一些内容

# 没那么复杂，打开文件，然后读取内容到内存中
with open('test.txt','r') as f:
    s = f.readlines()
# 接着打开文件，用replace替换掉你内存中的内容，然后写入文件
with open('test.txt','w') as w:
    for i in s:
        w.write(i.replace('nihao','hi'))


# StringIO和BytesIO

# stringIO 比如说，这时候，你需要对获取到的数据进行操作，但是你并不想把数据写到本地硬盘上，这时候你就可以用stringIO
from io import StringIO
from io import BytesIO
def outputstring():
    return 'string \nfrom \noutputstring \nfunction'

s = outputstring()

# 将函数返回的数据在内存中读
sio = StringIO(s)
# 可以用StringIO本身的方法
print(sio.getvalue())
# 也可以用file-like object的方法
s = sio.readlines()
for i in s:
    print(i.strip())


# 将函数返回的数据在内存中写
sio = StringIO()
sio.write(s)
# 可以用StringIO本身的方法查看
s=sio.getvalue()
print(s)

# 如果你用file-like object的方法查看的时候，你会发现数据为空

sio = StringIO()
sio.write(s)
for i in sio.readlines():
    print(i.strip())

# 这时候我们需要修改下文件的指针位置
# 我们发现可以打印出内容了
sio = StringIO()
sio.write(s)
sio.seek(0,0)
print(sio.tell())
for i in sio.readlines():
    print(i.strip())

# 这就涉及到了两个方法seek 和 tell
# tell 方法获取当前文件读取指针的位置
# seek 方法，用于移动文件读写指针到指定位置,有两个参数，第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
# 用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值哦



# stringIO 只能操作str，如果要操作二进制数据，就需要用到BytesIO
# 上面的sio无法用seek从当前位置向前移动，这时候，我们用'b'的方式写入数据，就可以向前移动了
bio = BytesIO()
bio.write(s.encode('utf-8'))
print(bio.getvalue())
bio.seek(-36,1)
print(bio.tell())
for i in bio.readlines():
    print(i.strip())



# 文件和目录的操作
# 查看当前绝对路径
os.path.abspath('.')
# 要在目录下创建新目录，首先展出完整路径
fullpath=os.path.join(os.path.abspath('.'),'testdir')
# 然后创建一个目录
os.mkdir(fullpath)
# 或者删除一个目录
os.rmdir(fullpath)
# 在对路径进行操作时，不论是合并还是拆分，都不要直接去合并或拆分字符串，而是使用os.path.jon或者os.path.split来进行操作
# 使用os.path.split的时候，后一部分总是最后级别的目录或文件名
os.path.split(fullpath)
# 获取文件扩展名
os.path.splitext(fullpath)
# 检验给出的路径是一个文件还是目录
os.path.isfile()
os.path.isdir()
# 检验给出的路径是否存在
os.path.exists()
# 返回文件名
os.path.basename
# 返回文件路径
os.path.dirname()
#对文件的操作
# 复制一个文件
shutil.copy('test.txt','test.py')
# 对这个文件重命名
os.rename('test.py','test.json')
# 然后删除文件
os.remove('test.json')


# 遍历当前文件夹及子文件夹下的指定字符串的文件
import os
ret = []
def findFile(s,path='.'):
    for filename in os.listdir(path):
        deeper_dir = os.path.join(path,filename)
        if os.path.isfile(deeper_dir) and s in filename:
            ret.append(filename)

        if os.path.isdir(deeper_dir):
            findFile(s,deeper_dir)
    return ret

if __name__ == '__main__':
    print(findFile('test'))



# 序列化及反序列化

# json模块，用于实现python数据类型与通用json字符串之间的转换
# dumps 将python数据类型转换成对应的json格式
data = {"key1":"value1"}

d1 = json.dumps(data)
print(d1)
print(type(d1))

# loads 将json数据转换成对应的python数据类型
data = '{"key1":"value1"}'

l1 = json.loads(data)
print(l1)
print(type(l1))
# dump将数据转换成对应的json格式，并写入文件，load加载json文件，并转换成对应的python数据类型

import json
# 如果python数据是dict，则序列化成{"key1": "value1"}
# 如果python数据是str， 则序列化成"{\"key1\":\"value1\"}"

# data = {"key1":"value1"}
data = '{"key1":"value1"}'
with open('test.txt','w') as f:
    json.dump(data,f)

# 反序列化
with open('test.txt','r') as f:
    print(json.load(f))




# pickle模块，用于将实现python数据类型的序列化和反序列化

# dumps 将python数据序列化成bytes
d=dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

# loads 将bytes数据转换成对应的python数据
d=dict(name='Bob', age=20, score=88)
b1=pickle.dumps(d)
print(pickle.loads(b1))

# dump将对象序列化后，写入一个file-like object
with open('test.txt','wb') as f:
    pickle.dump('testaaaa',f)

# load 将file-like object中的数据反序列化，转换成python对应的数据
with open('test.txt','rb') as f:
    print(pickle.load(f))


# 自定义对象的json序列化

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob',20,88)

# 如果直接json.dumps(s)，会报错
# TypeError: Object of type 'Student' is not JSON serializable
# 查看dumps的参数得知，默认情况下dumps通过default参数将对象变成一个可进行序列化的对象
# 大意就是我指定default的方法是什么，然后对s这个对象用指定的方法进行操作，变成可被序列化
# 所以，我们来写一个转换的方法

def student2dict(std):
    return {
      'name': std.name,
      'age': std.age,
      'score': std.score
    }

print(json.dumps(s,default=student2dict))

# 还有另外一种方式，我们知道json.dumps是可以对dict进行序列化的，那么我们可以将实例都变成一个dict，就可以被json序列化了

print(json.dumps(s,default=lambda obj:obj.__dict__))

with open('test.txt','w',encoding='utf-8') as f:
    json.dump(s,f,default=lambda obj:obj.__dict__)

# 如果我们要把一个json反序列化成一个实例，首先loads会转换出一个dict对象，然后，我们传入objcet_hook函数，将dict转换成实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))

with open ('test.txt','r',encoding='utf-8') as f:
    json.load(f,object_hook=dict2student)
# ensure_ascii=True,保证所有传入的非ASCII的字符都被转义，如果为false，则保持原样输出



# 多进程

# linux/unix操作系统提供了一个fork()系统调用,普通的函数调用,调用一次返回一次,
# fork()调用一次,返回两次,操作系统将当前进程(称为父进程)复制了一份(称为子进程)(那既然是复制了一份，子进程，自然也就有自己的PID了)
# 然后分别在父进程和子进程内返回
# 子进程永远返回0,而父进程返回子进程的ID，子进程只需要执行getppid()就可以拿到父进程的ID

import os
print('Process {0} start ...'.format(os.getpid()))
pid = os.fork()
if pid == 0:
    print('I am child process {0} and my parent is {1}'.format(os.getpid(),os.getppid()))
else:
    print('I {0} just create a child process {1}'.format(os.getpid(),pid))


# 如果你打算写一个关于多进程的跨平台模块
# join() 方法等待子进程结束后，继续往下执行
# start() 启动进程
import multiprocessing
def run_proc(args):
    print('Run child process {0} and argument is {1}'.format(os.getpid(),args))

if __name__ == '__main__':
    print('Parent process {0}'.format(os.getpid()))
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end')


# 如果你想同时启动大量的子进程，可以用进程池的方式批量创建，如下
# Pool()默认是CPU的核数，这里指定为4个，可以同时启动4个子经常，然后要等前面的执行完之后，才能执行后面的
# 调用join()之前必须调用close()，调用close()之后就不能继续添加新的Process了
# apply 执行直到前面的任务完成，apply_async() 并行执行
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 其实跑多个进程，用上面的Process也可以，只不过是不能并行
def long_time_task(name):
    print('Run task {0} {1}...'.format(name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task {0} run {1:.2f} seconds.'.format(name,(end-start)))

if __name__ == '__main__':
    print('Parent process {0}'.format(os.getpid()))
    print('waiting for all subprocess done...')
    for i in range(5):
        p = Process(target=long_time_task, args=(i,))
        p.start()
        p.join()
    print('All subprocesses done.')


# 很多时候，子进程并不是自身，而是一个外部进程，所以我们在创建了子进程之后，还需要控制子进程的输入和输出
# subprocess.Popen用来创建新的进程
# shell=True 表示在系统默认的shell环境中执行新的进程，windows下为cmd，linux下为/bin/sh
# executable 表示当shell为True时，用executable来修改默认的shell环境
# 默认的stdin,stdout,stderr均为None，表示新进程的stdin，stdout，stderr均为默认，从keyboard获得输入，将输出和错误输出到display
# 而如果stdin,stdout,stderr为PIPE，则表示打开了一个管道至标准流
# universal_newlines,如果为True，那么所有的行结束符会被转换成对应系统平台的换行符
# Popen.communicate(input=None) 与进程交互，将数据发送到标准输入
def run_nslookup(cmd,stdinstr=''):
    p = subprocess.Popen(cmd,shell=True,universal_newlines=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,err = p.communicate(stdinstr)
    print(output)
    print('Exit code:',p.returncode)

if __name__ == '__main__':
    run_nslookup('nslookup',stdinstr='set q=mx\npython.org\nexit\n')


# 进程间的通信及队列
# queue.Queue 进程内的非阻塞队列，不能跨进程通信
# 一般在producer 和consumer在同一个进程的时候工作
import time,random,os,queue
from multiprocessing import Process

def test(q):
    print('Process to write: {0}'.format(os.getpid()))
    for value in ['A','B','C']:
        print('Put {0} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())

    print('Process to read: {0}'.format(os.getpid()))

    while not q.empty():
        value = q.get()
        print('Get {0} from queue...'.format(value))
        time.sleep(random.random())


if __name__ == '__main__':
    q = queue.Queue()
    p = Process(target=test,args=(q,))
    p.start()
    p.join()

# multiprocessing.Queue在一个进程写，在另一个进程读，能跨进程通信

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


# 并行执行
def write(q):
    print('Process to write: {0}'.format(os.getpid()))
    for value in ['A','B','C']:
        print('Put {0} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: {0}'.format(os.getpid()))
    while True:
        # 用这种方式判断有时候会不准确
        if not q.empty():
            value = q.get(True)
            print('Get {0} from queue.'.format(value))
            time.sleep(random.random())
        else:
            break
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    q = manager.Queue()
    p = Pool()
    pw = p.apply_async(write,args=(q,))
    pr = p.apply_async(read,args=(q,))
    p.close()
    p.join()

# 看到评论里有人问到，为什么print出来的结果顺序不是按照代码的流程来的，是因为进程是由操作系统调度的，我认为是cpu分片操作的缘故，如果一定要顺序来的话，得使用同步机制


# 多线程
# 进程就是由线程组成，一个进程最少都有一个进程
import os,multiprocessing,time,random,subprocess,threading

def loop():
    print('Thread {0} is running...'.format(threading.current_thread().name))

    n = 0
    while n <5:
        n = n + 1
        print('thread {0} >>> {1}'.format(threading.current_thread().name,n))
        time.sleep(1)
    print('thread {0} ended'.format(threading.current_thread().name))

print('thread {0} is running...'.format(threading.current_thread().name))
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print('thread {0} ended.'.format(threading.current_thread().name))

# current_thread()函数，获取当前线程的实例
# 主线程的名字叫MainThread，子线程的名字是在创建的时候指定的，不指定则为默认的Thread-1,Thread-2...

# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
# 这是因为线程的调度是有系统决定的，而高级语言的每一条语句在CPU执行时是若干条语句，当多个线程交替执行的时候，就可能导致数据变混乱，如下
balance = balance + n
CPU在计算的时候分为两步：
1.计算balance+n，存入临时变量
2.将临时变量赋值给blance

因此，当线程交替运行的时候，可能就会如下
balance = 0

t1: x1 = balance + 5 # x1=0+5=5

t2: x2 = balance + 8 # x2=0+8=8
t2: balance = x2     # balance = 8

t1: balance = x1     # blance = 5
t1: x1 = balance - 5 # x1 =5-5= 0
t1: balance = x1     # blance = 0

t2: x2 = balance -8  # x2 = 0 -8 = -8
t2: balance = x2     # balance = -8

# 解决这个问题比较好的办法就是确保一个线程在修改的时候，别的线程一定不能改，因此我们可以使用python中的Lock机制来实现

import time,threading

# 假设这是你的银行存款
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完之后一定要释放锁
            lock.release()

# 线程创建
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
# 启动线程
t1.start()
t2.start()
# 等待线程结束
t1.join()
t2.join()
print(balance)

# 如果是多核CPU，想实现多核任务， 可以使用多进程的方式

# ThreadLocal
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来特别麻烦。
import os,time,random,subprocess,threading

class Student(object):
    def __init__(self,name):
        self.name = name

def do_task_1(ist):
    do_subtask_1(ist)

def do_subtask_1(ist):
    print('Hello,{0} (in {1})'.format(ist.name,threading.current_thread().name))

def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)

t1 = threading.Thread(target=process_student,args=('Alice',))
t2 = threading.Thread(target=process_student,args=('Bob',))
t1.start()
t2.start()
t1.join()
t2.join()

# process_student('Alice') --> do_task_1('Alice') --> do_subtask_1('Alice') -- > print
# 每个函数一层一层的调用都这么传肯定不行，用全局变量也不行，因为每个线程处理不同的Student对象，不能共享

# 用全局dict存放所有Student对象，然后以thread自身作为key获取当前线程对应的student对象也行
import os,multiprocessing,time,random,subprocess,threading

class Student(object):
    def __init__(self,name):
        self.name = name

global_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    print('Hello,{0} (in {1})'.format(std.name,threading.current_thread().name))



t1 = threading.Thread(target=std_thread,args=('Alice',))
t2 = threading.Thread(target=std_thread,args=('Bob',))
t1.start()
t2.start()
t1.join()
t2.join()


# ThreadLocal方式
import threading

# 创建全局threadLocal对象
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, {0} (in {1})'.format(std,threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=std_thread,args=('Alice',))
t2 = threading.Thread(target=std_thread,args=('Bob',))
t1.start()
t2.start()
t1.join()
t2.join()


# 进程 vs 线程
# 进程稳定，线程效率高
# 进程创建代价大，线程不稳定

# 分布式进程
# 使用multiprocessing的managers子模块将多进程分布到多台机器上，没有跨进程的通信，所以，也就没必要用multiprocessing.Queue
# 一台机器上的服务进程作为调度者，依靠网络将任务传送到不同机器的多个进程执行

#server.py

#!/usr/bin/env python3
#-*- coding utf-8 -*-

# 导入managers子模块中的BaseManager类，这个类封装了一些常用的网络传输和接口方法
from multiprocessing.managers import BaseManager
import queue,time,random

# 初始化两个queue消息队列，一个用于传输，一个用于接收
sendMsg = queue.Queue()
receiveMsg = queue.Queue()

# 新建一个类，继承BaseManager的所有属性和方法
class CommBase(BaseManager):
    pass

# 使用BaseManager类的register方法，生成两个接口函数，名为"send_msg"和"receive_msg",使用callable参数，将两个借口函数关联到不同的queue对象上(相当于定义了两个返回queue的网络接口函数)
CommBase.register("send_msg",callable=lambda : sendMsg)
CommBase.register("receive_msg",callable=lambda : receiveMsg)

# 监听本地的5000端口，验证码为"abc"(在接收端要配置相同的验证码才能连接到这台机器的5000端口)
commMgr = CommBase(address=('',5000),authkey=b'abc')

# 启动网络监听(此时会在系统中发现127.0.0.1:5000端口处于监听状态)
commMgr.start()

# 获得商脉内创建的接口函数对象(queue对象)
send=commMgr.send_msg()
receive=commMgr.receive_msg()

# 随机生成5个1~1000的数字，将它们放到queue中
for x in range(5):
    n=random.randint(1,1000)
    print("Put task {0}".format(n))
    send.put(n)

# 之后这个程序将被阻塞，在5000端口上等待消息返回
print('Try get results...')
for x in range(5):
    r = receive.get(True)
    print('Result: {0}'.format(r))

# 关闭接口，释放资源
commMgr.shutdown()
print('Master exit.')


#client.py
#!/usr/bin/env python3
#-*- coding utf-8 -*-
from multiprocessing.managers import BaseManager

class CommBase(BaseManager):
    pass

# 接收端只需要注册两个与调度端相同的网络接口函数名称即可
CommBase.register("send_msg")
CommBase.register("receive_msg")

# 调度端IP(如果想使用同一台机器测试，就可以改成127.0.0.1)
ip_address='127.0.0.1'

# 调度端IP,端口,验证码
commMgr = CommBase(address=('',5000),authkey=b'abc')

try:
    #连接
    commMgr.connect()

    #实例化接口函数
    send=commMgr.send_msg()
    receive=commMgr.receive_msg()

    # 从调度端send_msg()接口get消息，然后，将消息返回给调度端的receive_msg()接口
    for x in range(5):
        print('connect to {0}...'.format(ip_address))
        n = send.get(True)
        r = '{0} * {1} = {2}'.format(n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.empty(result):
        print('task queue is empty')

print('Work exit.')


# 正则表达式
# \d 匹配一个数字
# \w 匹配一个字母或数字
# . 可以匹配任意字符
# * 匹配任意个字符(包括0个)
# + 表示至少一个字符
# ? 表示0或者1个字符
# {n} 表示n个字符
# {n,m} 表示n-m个字符
# \s 匹配一个空格

# 精确匹配使用[]
# [0-9a-zA-Z\_] 匹配一个数字，字母或者下划线
# [0-9a-zA-Z\_]+ 可以匹配至少由一个数字、字幕或者下划线组成的字符串，比如'a100','0_z','Py3000'等
# [a-zA-Z\_][0-9a-zA-Z\_]* 可以匹配由字母或者下划线开头，后接任意个数字、字母或下划线组成的字符串，也就是python的合法变量
# [a-zA-Z\_][0-9a-zA-Z\_]{0,19} 更精确的限制了变量的长度是1-20个字符
# A|B，可以匹配A或者B，所以(p|P)ython 可以匹配'Python'或'python'
# ^ 表示行开头
# ^\d表示以数字开头
# $ 表示行结束
# \d$ 表示以数字结束
# py可以匹配python，但是加上^py$ 之后就只能匹配py了

# python中的re模块包含了所有正则表达式的功能
# re.match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
import re
test = input('string by user input:')
if re.match(r'^\d{3}\s*\-\s*\d{3,8}$',test):
    print('ok')
else
    print('faild')

# re也包含了字符串的切分，并且比普通的字符串切分更加灵活
print(re.split(r'\s+','a b   c'))
print(re.split(r'[\s\,]+','a,b, c d'))
print(re.split(r'[\s\,\;]+','a,b;; c d'))

# 通常我们用()来表示要提取的分组，比如
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')

print(m)
print(m.group(0)) # 永远表示原始字符串
print(m.group(1)) # 表示第一个字符串
print(m.group(2)) # 表示第二个字符串

# 字符串的提取非常有用，下面我们来看一个凶残的例子

t=str(datetime.datetime.now().time())
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\.\d*$',t)
print(m.groups())

# 贪婪匹配
# Python里数量词默认是贪婪的（在少数语言里也可能是默认非贪婪），总是尝试匹配尽可能多的字符；非贪婪则相反，总是尝试匹配尽可能少的字符。在"*","?","+","{m,n}"后面加上？，使贪婪变成非贪婪。
# # 这里的0* ，意思是指匹配0个或者任意个0，刚开始还以为是在0后面匹配任意个任意字符(手动捂脸)
print(re.match(r'^(\d+?)(0*)$','102300').groups())

# 预编译正则表达式，如果一个正则表达式要重复使用无数次，处于效率考虑，我们可以先预编译正则表达式，接下来重复使用的时候，就不用编译了，直接匹配即可，如下
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())

# 常用内建模块

# datetime模块
# 获取当前日期和时间
from datetime import datetime
now = datetime.now()

# 获取指定日期和时间，我们之间用参数构造一个datetime
dt = datetime(2018,2,1,14,30,18)

# 在计算机中时间实际上是由数字表示的
# datetime转换为timestamp
dt=datetime.now()
st = dt.timestamp()

# timestamp 转换为datetime，这里进行转换实际上是和本地所在的时区时间做的转换
dt = datetime.fromtimestamp(st)

# 如果要转换为标准的格林时间应该是
dt = datetime.utcfromtimestamp(st)

# str 转换成datetime
dt = datetime.strptime('2018-2-1 15:12:00','%Y-%m-%d %H-%M-%S')

# datetime 转换成str
now_dt = datetime.now()
now_dt.strftime('%a,%b %d %H:%M:%S')

# datetime加减
from datetime import datetime, timedelta
now_dt = datetime.now()
now_dt + timedelta(hours=10)
now_dt - timedelta(days=1)
now_dt + timedelta(days=2,hours=12)

# 本地时间转换为UTC时间
from datetime import datetime, timedelta，timezone
tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00

# 时区转换
# 先通过utcnow()拿到当前的UTC时间，再转换成任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# 也不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))

# 练习的例子
import re
from datetime import datetime,timedelta,timezone
def to_timestamp(dt_str,tz_str):
    # str2datetime
    dt_dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    # 获取时区int值
    tz_tz= int(re.match(r'UTC([+-]\d+):\d+',tz_str).group(1))
    # 创建对应的时区
    tz_utc = timezone(timedelta(hours=tz_tz))
    # 强制设置为对应的时区
    dt = dt_dt.replace(tzinfo=tz_utc)
    # datetime2timestamp
    print(dt.timestamp())


# collections模块

# namedtuple 用来创建一个自定义的tuple对象，并且规定了tuple元素个数，并可以用属性而不是索引来引用tpule的元素
# namedtuple('名称', [属性list]):
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x,p.y)
# 我们可以发现Point对象实际上就是tuple的一种子类
isinstance(p,Point)
isinstance(p,tuple)

# deque
# 我们使用list存储数据，当数据量大了之后，插入和删除的效率会很低，因此我们可以使用deque来提高效率
# deque 除了支持list常用的一些方法外，还支持如appendleft()和popleft()方法
from collections import deque
l = deque(['a','b','c'])
l.append('x')
l.appendleft('y')
l.pop()
l.popleft()

# defaultdict
# 使用dict时，如果引用的key不存在，则会抛出keyerror，如果希望key不存在时，返回一个默认值，就可以使用defaultdict
# 这里要注意的是，默认值是调用函数返回的
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
# 不存在则返回N/A
print(dd['key2'])

# OrderedDict
# 使用dict时，key是无序的，在对dict做迭代时，我们无法确定key的顺序
# 如果要保持key的顺序，我们可以使用OrderedDict
from collections import OrderedDict
d = {'a':1,'b':2,'c':3}
od = OrderedDict(d)
print(od)

# OrderedDict可以实现一个FIFO(先进先出)的dict
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        #集合大小
        self._capacity = capacity

    def __setitem__(self, key, value):
        # 判断key是否在dict中
        containsKey = 1 if key in self else 0
        #当前集合大小
        if len(self) - containsKey >= self._capacity:
            #弹出前面的key-value,last=true 采用LIFI，删除最后一个，last=false采用FIFO，不删除最后一个
            # 这个last=True or False 只有在OrderedDict中才有哦
            last = self.popitem(last=False)
            print 'remove:', last
        #有当前key
        if containsKey:
             #删除存在的key
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        #往dict里面添加值
        OrderedDict.__setitem__(self, key, value)

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter() # 创建一个空的Counter类
c = Counter('chenglanguo') # 从一个可iterable对象(list,tuple,dict,string)创建
# 当然你创建一个空的Counter类之后，可以通过下面的办法来统计也是可以的
for x in 'chenglanguo':
    c[x] = c[x] + 1

# 当访问的键不存在时，返回0，而不是KeyError，否则返回它的计数
print(c['g']) # 2

# base64
# 将数据存储到硬盘上(字符转字节)就需要进行编码encode
# 将数据显示出来(字节转字符)就需要解码decode
# base64的原理很简单，首先准备一个包含64个字符的数组
['A','B','C',...'a','b','c',...'0','1','2'...,'+','/']
# 然后对二进制数据进行处理，每3个字节一组，一共就是3x8=24bit，然后再划分为4组，每组6bit
# base64编码会把3字节的二进制数据编码为4字节的文本数据
# 如果要编码的二进制的数据不是3的倍数，Base64会用\x00在末尾补足，然后在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候会自动去掉
import base64
base64.b64b64encode(b'binary\x00string')
# 由于标准的base64编码后可能会出现+和/，在URL中不能直接作为参数，所以又有一个 urlsaft的base64编码，其实就是把字符+和/分辨变成-和_
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd++//'
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
b'abcd--__'
# 由于=字符也可能出现在base64编码中，但=在URL,Cookie里面会造成歧义，一次很多Base64编码后会把=去掉
# 由于base64是把3个字节变成4个字节，所以解码的时候，base64编码的长度永远是4的倍数，当那些没有=号的base64编码，则需要加上=号base64字符串长度变为4的倍数
# 如下例子解码那些去掉了=号的base64编码
def safe_base64_decodes(s):
    if len(s) % 4 == 0:
        return base64.b64decode(s)
    else:
        b_str = (str(s,'utf-8'))
        b_str = b_str + '='
        return safe_base64_decodes(bytes(b_str,encoding='utf-8'))
        return safe_base64_decodes(b_str.encode('utf-8'))

# struct模块
# 当python需要通过网络与其他平台进行交互的时候，必须考虑到将这些数据类型与其他平台或语言之间的类型进行相互转换。
# 比如：C++写的客户端发送一个int型变量的数据到python写的服务器，python接收到表示这个证书的4个字节的数据，怎么解析成python认识的整数呢，就可以用struct
# 先看看fmt格式
FORMAT  [C TYPE]            [PYTHON TYPE]   [STANDARD SIZE]     [NOTES]
x       pad byte            no value
c       char                string of length    1               1
b       signed char         integer             1               (3)
B       unsigned char       integer             1               (3)
?       _Bool               bool                1               (1)
h       short               integer             2               (3)
H       unsigned short      integer             2               (3)
i       int                 integer             4               (3)
I       unsigned int        integer             4               (3)
l       long                integer             4               (3)
L       unsigned long       integer             4               (3)
q       long long           integer             8               (2), (3)
Q       unsigned long       long integer        8               (2), (3)
f       float               float               4               (4)
d       double              float               8               (4)
s       char[]              string
p       char[]              string
P       void *              integer                             (5), (3)

# 指示打包数据的字节顺序，大小和对齐方式
# 对于字节顺序，只有大端和小端两种方式，只是比如你用@和=代表你用本机的字节顺序，!代表你使用网络的字节顺序。你不指定字节顺序则默认的是@
# 本地字节顺序是大端或小端，取决于主机系统，使用sys.byteorder来检查你系统的字节顺序
CHARACTER   [BYTE ORDER]            [SIZE]      [ALIGNMENT]
@           native                  native      native
=           native                  standard    none
<           little-endian           standard    none
>           big-endian              standard    none
!           network(=big-endian)    standard    none

# 例子
# struct.pack 用于将python的值根据格式符，转换为字符串(以为python中没有字节类型，但是str就是字节流)
import struct

a = 20
b = 200
str = struct.pack('ii',a,b)
print(len(str)) # 8
print(str) # b'\x14\x00\x00\x00\xc8\x00\x00\x00'
print(repr(str)) # b'\x14\x00\x00\x00\xc8\x00\x00\x00'
# 格式符i表示转换为int，ii表示有两个int变量，我们还可以用2i来表示

# struct.unpack 用于将字节流转换为python数据类型
str2 = struct.unpack('ii',str)
print(len(str2)) # 2
print(str2) # (20, 200)
print(repr(str)) # b'\x14\x00\x00\x00\xc8\x00\x00\x00'

# 廖雪峰blog中有个例子，windows位图文件的前30个字节表示了这个文件的一些关键信息，我们试试看
# 自己随便画一个bmp的位图，然后取前30个字节，我们就能获取到这个文件的关键信息
import base64, struct
with open('test.bmp','rb') as f:
    s = f.read()

print(struct.unpack('<ccIIIIIIHH',s[:30]))


# hashlib
# 摘要算法、哈希算法、散列算法，通过一个函数，把任意长度的数据转换为一个长度固定的数据串(通常用16进制的字符串表示)
# 常见的有MD5,SHA1等
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
# 如果数据量很大，可以分块多次调用update()，最后的计算结果都是一样的
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest()) # 16进制就是32个
print(bin((int(md5.hexdigest(),16)))) # 2进制就是128个

# MD5生成结果是固定的128bit字节，通常是用一个32位的16进制表示

# 还有另一种比较常见的算法是SHA1，调用SHA1算法MD5完全类似
import hashlib
print(hashlib.sha1('how to use sha1 in python hashlib?'.encode('utf-8')).hexdigest())
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

# hash 算法常用在比如存储用户密码之类的情况
# 而我们在使用hash值存储密码的时候，还需要给密码加上随机的salt值，这样黑客就无法通过对比hash值来破解用户帐户，如下例子
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        # 随机一个salt值，与用户的password合并，然后计算出hash值，这样黑客就不容易破解了
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alxiice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == get_md5(password+user.salt)


# hmac
# 为了防止黑客通过hash值反推原始口令，我们在计算hash值的时候，通常会加上一个salt值
# 如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message+salt)。
# 但是实际上，我们假如把salt看成一个‘口令’，加salt的hash就是：计算一段message的哈希时，根据不同的口令，计算不同的hash，要验证hash，我们就得提供正确的口令
# 这实际就是hmac算法，需要注意的是，hmac传入的key和message都是bytes类型，str类型首先需要转换成bytes
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key,message,digestmod = 'MD5')
print(h.hexdigest())
# 如果消息很长，我们可以多次调用h.update(msg)

# 所以上面那个使用salt的例子，我们可以改造成如下
import hmac,random
def hmac_md5(key,msg):
    return hmac.new(key.encode('utf-8'),msg.encode('utf-8'),'MD5').hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.key = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = hmac_md5(self.key,password)

db = {
    'michael': User('michael','123456'),
    'bob': User('bob','abc999'),
    'alice': User('alice','alice2008')
}

def login(username,password):
    user = db[username]
    return user.password == hmac_md5(user.key,password)


# itertools

# count(start=0,step=1)
import itertools
# 从1000开始，每次加100，无限迭代
natuals = itertools.count(1000,100)
for n in natuals:
    print(n)

# cycle
# 无限重复一个可迭代对象
import itertools
# cycle(iterable)
cs = itertools.cycle('ABC')
for c in cs:
    print(c)

# repeat(p_object,times=None)
# 负责把一个元素无限重复,第二个参数可以限定重复次数
ns = itertools.repeat('A',3)
for n in ns:
    print(n)


# 无限序列会无限迭代，但是，我们通常会通过takewhile()等函数条件来判断截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x<=10,natuals)
print(list(ns))

# chain(*itertable)
# chain()可以将一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC','XYZ'):
    print(c)

# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起
for key,group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))
# 实际上，挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而返回的值就作为组的key
# 比如，我们想要忽略大小写分组，就可以让'A'和'a'返回的key是相同的
for key,group in itertools.groupby('AaaBBbcCAAa',key=lambda x:x.lower()):
    print(key,list(group))


# 计算前N个序列的和
def pi(N):
    step1 = itertools.count(1,2)
    step2 = itertools.takewhile(lambda x: x <= 2*N - 1,step1)
    step3 = itertools.cycle([4,-4])
    return sum(next(step3)/next(step2) for x in range(N))


# contextlib

# @contextmanager
# 我们知道file-like-object对象是可以用open()函数打开的，因此可以使用with语句，实际上，任何对象，只要实现了上下文管理，就可以用于with语句
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的，下面的class实现了这两个方法，因此它就可以用于with语句
class Query(object):
    def __init__(self,name):
        self.name = name
    def __enter__(self):
        print('Begin')
        return self
    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print('Query info about {0}'.format(self.name))

with Query('Bob') as q:
    q.query()

# 自己编写__enter__和__exit__仍然很繁琐，因此python库contextlib提供了更简单的方法，如下
# @contextmanager装饰器将一个函数中yield语句之前的代码当做__enter__方法执行，yield语句之后的代码当做__exit__方法执行。同时yield返回值赋值给as后的变量
from contextlib import contextmanager

class Query(object):
    def __init__(self,name):
        self.name = name
    def query(self):
        print('Query info about {0}'.format(self.name))

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('end')

# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现，如下：
@contextmanager
def tag(name):
    print('<{0}>'.format(name))
    yield
    print('</{0}>'.format(name))

with tag('h1'):
    print('Hello')
    print('World')

# 上述代码执行顺序：
# 1.with 语句首先执行yield语句之前的语句，因此打印出<h1>
# 2.yield调用会执行with语句内部的所有语句，一次打印出Hello和World
# 3.最后执行yield之后的语句，打印出</h1>
# @contextmanager让我们通过编写generator来简化上下文管理

#closing

# 如果一个对象没有实现上下文，我们就不能将它用于with语句，这个时候，可以用closing()来把该对象变成上下文对象。例如，用with语句使用urlopen()
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)


# urllib
# urllib 提供了一系列用于操作RUL的功能

# request
# 我们访问一个页面，实际上就是发送一个GET请求到指定页面，返回HTTP响应，这时候，我们就可以用urllib的request模块
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    # 可以返回HTTP响应状态
    print('Status:',f.status,f.reason)
    # 返回HTTP响应的头
    for k,v in f.getheaders():
        print('{0}: {1}'.format(k,v))
    print('Data:',data.decode('utf-8'))

# 如果我们要模拟浏览器发送get请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器，这其实就是包装头部信息
from urllib import request
# 使用Request对象
req = request.Request('http://www.douban.com/')
# 往Request对象添加HTTP头
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# 如果我们要以POST发送一个请求，只需要把参数data以bytes形式传入
# 下面是个登录微博的例子
from urllib import request, parse
print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# handler
# 如果还有更复杂的控制，比如说通过一个proxy去访问网站，我们需要利用ProxyHandler来处理
# OpenerDirector使用handler处理任务，所有的重活都交给这些handlers来做，每一个handlers知道怎么以特定的url协议打开url
from urllib import request
google_url = 'https://www.google.com.hk/'

proxy_handler = request.ProxyHandler({
    'https': 'https://127.0.0.1:19888',
    'http': 'http://127.0.0.1:19888'
})

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


# 返回一个OpenerDirector实例，即这里的opener
opener = request.build_opener(proxy_handler)
# 安装一个OpenerDirector实例作为全局的默认opener
request.install_opener(opener)
# 包装下HTTP头
req = request.Request(google_url,headers=headers)

with request.urlopen(req) as f:
    print(f.read().decode())

# with opener.open(req) as f:
#     print(f.read().decode())


# XML
# 操作XML有两种方法：DOM和SAX。
# DOM会把整个XML读入内存，解析为树，因此内存占用大，解析慢，有点是可以任意便利树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。
# 如果我们自己处理事件的话，如下：
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print(name,str(attrs))
    def end_element(self,name):
        print(name)
    def char_data(self,text):
        print(text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

# 另外，我们如果不自己处理事件的话，我们可以使用python的parse，如下：
from urllib.request import urlopen
from xml.etree.ElementTree import parse
import time

# Download the RSS feed and parse it
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def parseXml(URL):
    rss = parse(urlopen(URL)).getroot()
    location = {}
    data = {}
    forecast = []

    elment = rss.find('results/channel/{'+'{0}'.format(WEATHER_NS)+'}location')
    location['city'] = elment.get('city')

    elment = rss.findall('results/channel/item/{'+'{0}'.format(WEATHER_NS)+'}forecast')
    for x in elment:
        data['date'] = time.strftime('%Y-%m-%d',time.strptime(x.get('date'),'%d %b %Y'))
        data['high'] = x.get('high')
        data['low'] = x.get('low')
        forecast.append(data)
    return {'city': location['city'],
            'forecast': forecast}

result = parseXml(URL)
assert result['city'] == 'Beijing'
print('ok')


# HTMLparser
# 这个标记下，看的不是很明白
# python提供了HTMLParser来解析HTML
#handle_startendtag  处理开始标签和结束标签
#handle_starttag     处理开始标签，比如<xx>
#handle_endtag       处理结束标签，比如</xx>
#handle_charref      处理特殊字符串，就是以&#开头的，一般是内码表示的字符
#handle_entityref    处理一些特殊字符，以&开头的，比如 &nbsp;
#handle_data         处理数据，就是<xx>data</xx>中间的那些数据
#handle_comment      处理注释
#handle_decl         处理<!开头的，比如<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
#handle_pi           处理形如<?instruction>的东西
from html.parser import HTMLParser
from urllib import request
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False
        self.result = []
        self.dict = {}
        self.isHandling = None

    def handle_starttag(self, tag, attrs):
        # 先找出ul和list-recent-events menu的部分
        if tag == 'ul' and attrs[0][1] == 'list-recent-events menu':
            self.flag = True

        # 然后分别找出tag为a，time，span的部分，分别赋值
        if self.flag == True:
            if tag == 'a':
                self.isHandling = 'title'
            if tag == 'time':
                self.isHandling = 'time'
            if tag == 'span':
                self.isHandling = 'location'

    def handle_endtag(self, tag):
        # 接着再处理结尾为ul部分
        # 这里判断结尾为ul并且开头为ul和list-recent-events menu的部分，如果是这样的就将flag定位flase
        # 其实就是取非ul的部分
        if tag == 'ul' and self.flag == True:
            self.flag = False
        # 取li里面的部分
        if self.flag == True and tag == 'li':
            self.result.append(self.dict)
            self.dict = {}

    def handle_data(self, data):
        # 然后处理li里面的数据
        if self.isHandling != None:
            self.dict[self.isHandling] = data
            self.isHandling = None

parser = MyHTMLParser()

with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parser.feed(data)

for item in parser.result:
    for k,v in item.items():
        print('{0}:'.format(k),v)
    print('--------------')


# 前面这个是自己写处理事件的方法，下面有个pyquery是不用自己写的，用起来很方便
from pyquery import PyQuery as pq

url = 'https://www.python.org/events/python-events/'
doc = pq(url)
events = doc('.shrubbery .list-recent-events.menu').text()
print('Upcoming Events:')
print('----------------------------------------')

print(events)


#Pillow ，图像处理的标准库

from PIL import Image,ImageFilter
import os
im = Image.open('1.png')
w,h = im.size
print('Original image size: {0}x{1}'.format(w,h))
print(im.mode)

# 缩放比例，注意图片的mode，需要转换
rgb_im = im.convert('RGB')
rgb_im.thumbnail((w//2,h//2))
print('Resize image to:{0}x{1}'.format(w//2,h//2))
print(rgb_im.mode)
rgb_im.save('2.jpg')

# 模糊图片
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.png')


# 绘图

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

# 生成随机字母
def rndChar():
    return chr(random.randint(65,90))
# 生成随机颜色，用来填充背景
def rndColor():
    return(random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 生成随机颜色2，用来填充文本
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 定义长宽
width = 60 * 4
height = 60
# 新建RGB类的图片，默认为白色
image = Image.new('RGB',(width,height),(255,255,255))
# 新建字体对象
font = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf',36)
# 新建draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

# 填充文本文字
for t in range(4):
    draw.text((60 * t + 10,10),rndChar(),font=font,fill=rndColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
# 保存图片
image.save('code.jpg')
# 显示图片
image.show('code.jpg')



# requests
# 前面我们用过urllib库，但是用起来麻烦，而且缺少很多高级功能，更好的方案是使用requests

# 通过get访问一个页面
import requests
url = 'https://www.douban.com/'
r = requests.get(url)

# 返回状态吗
print(r.status_code)

# 返回页面内容
print(r.text)

# 对于带参数的URL，传入一个dict作为params参数
params = {'q':'python','cat':1001}
r = requests.get(url,params=params)

# 返回实际请求url
print(r.url)

# 返回HTTP响应的头
print(r.headers)
print(r.headers['Content-Type'])

# 无论响应是文本还是二进制内容，我们都可以使用content属性获得bytes对象
print(r.content)

# requests还内置了一个JSON解码器，用来处理JSON数据
url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
r = requests.get(url)
print(r.json())

# 如果我们传入HTTP Header的话，我们可以传入一个dict作为headers参数
headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
r = request.get(url,headers=headers)
print(r.text) # 可以看到返回的内容确实是手机版了

# requests发送POST请求也变得十分容易
def login_page(url):
    login_url = 'http://cmdb.quark.com/account/login?cburl=http://job.quark.com/jobapp/login1'
    print('Login to job page...')
    username = input('Username: ')
    password = input('Password: ')
    data = {
        'user': username,
        'password': password
    }

    s = requests.Session()
    s.post(login_url,data=data)
    result = s.get(url)
    return result.status_code,result.cookies

page_url = 'http://job.quark.com/jobapp/'
print(login_page(page_url))

# requests默认使用application/x-www-form-urlencode对POST数据编码，如果要传递JSON数据，可以直接传入json参数
params = {'key': 'value'}
r = requests.post(url,json=params)

# 同样，上传文件需要复杂的编码格式，但是requests把它简化成files参数
upload_files = {'file': open('report.xls','rb')} # 读取文件的时候，注意务必使用'rb'进行读取，这样获取的bytes长度才是文件的长度
r = requests.post(url,files=upload_files)

# 把post() 方法替换成put() delete()等，就可以PUT和DELETE对资源进行操作了

# requests 对cookie做了特殊处理，使得我们不必去解析cookie就可以轻松获取指定的cookie
print(r.cookies)
print(r.cookies['csrftoken'])

# 要在请求中传入cookie，我们可以传入一个dict作为cookies参数
cs = {'token': '12345', 'status': 'working'}
r = requests.get(url,cookies=cs)

# 要指定超时，可以传入timeout参数
r = requests.get(url,timeout=2.5)


# chardet 检测编码
# 用chardet.detect 检测编码，获取到编码后，再转换为str，就可以方便后续处理
import chardet
data = '离离原上草，一岁一枯荣'.encode('utf-8')
s=chardet.detect(data)['encoding']
print(data.decode(s))

# 当我们拿到一个bytes时，就可以检测其编码
print(chardet.detect(b'Hello,world'))

# GBK
print(chardet.detect('中国'.encode('gbk')))

# UTF-8
print(chardet.detect('中国'.encode('utf-8')))


# psutil 获取系统信息
# 用python来编写脚本简化日常运维工作很常见，在linux下，我们可以通过subprocess模块调用并获取结果，但是这样挺麻烦
# 我们可以使用psutil这个第三方模块，来获取系统信息，实现系统监控，而且可以跨平台使用

# 统计当前时间CPU的用户/系统/空闲时间

# 通过统计这个，我们可以来计算下top命令显示出的一些利用率，和没有显示出来的利用率之类的，比如，统计用户空间的CPU利用率
r'''top上的cpu利用率，大致算法如下
CPU总时间2=user2+system2+nice2+idle2+iowait2+irq2+softirq2
CPU总时间1=user1+system1+nice1+idle1+iowait1+irq1+softirq1
用户cpu利用率 = user_pass * 100% / (CPU总时间2 - CPU总时间1)
内核cpu利用率 = system_pass * 100% / (CPU总时间2 - CPU总时间1)
总的cpu利用率= 用户cpu利用率 + 内核cpu利用率
'''

while True:
    cs1 = sum(psutil.cpu_times())
    cu1 = psutil.cpu_times().user
    time.sleep(3)
    cs2 = sum(psutil.cpu_times())
    cu2 = psutil.cpu_times().user
    ss = cs2 - cs1
    print(((cu2 - cu1) / ss) * 100)

print(psutil.cpu_times())

# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次
# 当percpu=True，会返回每个CPU的使用率， 否则就是总使用率
for x in range(10):
    print(psutil.cpu_percent(interval=1,percpu=True))

# 获取物理内存信息
print(psutil.virtual_memory())

# 获取swap内存信息
print(psutil.swap_memory())

# 获取磁盘分区信息
print(psutil.disk_partitions())

# 获取磁盘使用情况
print(psutil.disk_usage('/'))

# 获取磁盘IO
print(psutil.disk_io_counters())

# 获取网络读写字节/包的个数
print(psutil.net_io_counters())

# 获取网络接口信息
print(psutil.net_if_addrs())

# 获取网络接口状态
print(psutil.net_if_stats())

# 获取当前网络连接信息
print(psutil.net_connections())

# 获取所有进程ID
print(psutil.pids())

# 获取指定的进程ID
p = psutil.Process(2418)

# 获取进程名称
print(p.name())

# 获取进程执行文件路径
print(p.exe())

# 获取进程工作目录
print(p.cwd())

# 获取进程启动命令
print(p.cmdline())

# 获取进程父进程ID
print(p.ppid)

# 获取进程父进程
print(p.parent())

# 获取进程子进程
print(p.children())

# 获取进程状态
print(p.status())

# 获取进程用户名
print(p.username())

# 获取进程创建时间
print(p.create_time())

# 获取进程中断
print(p.terminal())

# 获取进程使用的CPU时间
print(p.cpu_times())

# 获取进程使用的内存
print(p.memory_info())

# 获取进程打开的文件
print(p.open_files())

# 获取进程相关的网络连接
print(p.connections())

# 获取进程的线程数量
print(p.num_threads())

# 获取进程的所有线程信息
print(p.threads())

# 获取进程的环境变量
print(p.environ())

# 结束经常
p.terminate()

# psutil 还提供了一个test()函数，可以模拟出ps命令的效果
print(psutil.test())




# virtualenv
# virtualenv就是为了创建一套“隔离”的python运行环境
# 首先我们通过pip安装virtualenv
pip3 install virtualenv
# 然后假定我们要开发一个新项目，需要一套独立的python运行环境，就可以这么做

# 第一步，创建一个独立的python运行环境
mkdir myproject
cd myproject

# 第二步，创建一个独立的python运行环境，命名为venv
virtualenv --no-site-packages venv
Using base prefix '/usr/local/.../Python.framework/Versions/3.4'
New python executable in venv/bin/python3.4
Also creating executable in venv/bin/python
Installing setuptools, pip, wheel...done.

# 第三步，通过source venv/bin/activate进入该环境，然后就想干嘛就干嘛吧
# 在venv环境下，用pip安装的包都被安装到venv这个环境下，系统python环境不受影响


# 图形界面
# 常见的图形界面库包括Tk,wxWidgets,Qt,GTK等等
# python自带的Tkinter,无需安装任何包，就可以直接使用，这里我们简单介绍下如何使用Tkinter进行GUI编程

# 第一个GUI程序
from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLabel=Label(self,text='Hello,world!')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='quit',command=self.quit)
        self.quitButton.pack()

app = Application()
app.master.title('Hello,World!')
app.mainloop()


# 再对这个GUI程序改进下，加入一个文本框，让用户可以输入文本，然后点击按钮后，弹出消息对话框
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello, {0}'.format(name))

app = Application()
app.master.title('Hello World')
app.mainloop()

# 网络编程

# TCP 编程
# socket是网络编程的一个抽象概念。通常我们用一个socket表示 "打开了一个网络链接"，而打开一个socket需要知道目标计算机的IP和port，再指定procotol即可

# 客户端
#大多数连接都是可靠的tcp连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器
import socket
import threading,time
def sockClient(url,port=80):
    # 创建一个socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 建立连接
    s.connect((url,port))
    # 建立连接之后，我们发送请求数据
    s.send(b'GET / HTTP/1.1\nHost: www.sina.com.cn\nConnection: close\n\n')
    buffer = []
    while True:
        # 接收服务器响应的数据，为了后面保存到本地
        data = s.recv(1024)
        if data:
            buffer.append(data)
        else:
            break
    data = b''.join(buffer)
    # 关闭连接
    s.close()
    header,html= data.split(b'\n\n',1)
    # 保存到本地
    with open('sina.html','wb') as f:
        f.write(html)
    return

# server

def sockServer():
    # 创建一个socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 监听端口
    s.bind(('127.0.0.1',9999))
    # 等待连接的最大数量
    s.listen(5)

    # 具体处理连接的方法
    def tcplink(sock,addr):
        print('Accept new connection from {0}:{1}'.format(addr[0],addr[1]))
        # 发送欢迎信息，对应下面客户端的接受欢迎信息
        sock.send(b'Welcome...')
        while True:
            # 接收从客户端发过来的信息
            data = sock.recv(1024)
            time.sleep(1)
            # 如果没有信息或者信息为exit，则推出循环
            if not data or data.decode('utf-8') == 'exit':
                break
            # 发送Hello信息
            sock.send(('Hello, {0}'.format(data.decode('utf-8'))).encode('utf-8'))
        # 关闭连接
        sock.close()
        # 打印连接地址和端口
        print('Connection from {0}:{1}'.format(addr[0],addr[1]))

    print('Waiting for connection...')
    while True:
        # 接受连接并返回（sock,address）,其中sock是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址
        sock,addr = s.accept()
        # 线程的方式
        t = threading.Thread(target=tcplink,args=(sock,addr))
        t.start()


# client
def sockClient(url,port=9999):
    # 创建一个socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 连接到服务器
    s.connect((url,port))
    # 接受从服务器上发送的欢迎信息
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael',b'Tracy',b'Sarah']:
        # 发送数据到服务器
        s.send(data)
        # 打印出从服务器返回的Hello信息
        print(s.recv(1024).decode('utf-8'))
    # 发送exit
    s.send(b'exit')
    # 关闭连接
    s.close()


# UDP编程
# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口，就可以直接发送数据包，但是能不能到达就不知道了
# 虽然UDP传输数据不可靠，但它的优点是和TCP比，速度快(真的很快啊)，对于不要求可靠到达的数据，就可以使用UDP协议


# 插播一个知识点：
# recv的recvfrom是可以替换使用的，只是recvfrom多了个返回参数addr，对于udp这种无连接的，可以很方便的进行回复
# 而换过来如果你在udp中使用recv，那么就不知道该回复给谁了，如果你不需要回复的话，是可以使用的
# 另外对于tcp是已经知道对端的，就没必要每次接受还多接受一个地址，没有意义，要获取地址信息，在accept中取得就好


# udp server
# 创建一个UDP的socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
while True:
    # 接受数据，还返回一个对端地址
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    # 发送数据到客户端
    s.sendto(b'Hello,%s!' % data,addr)


# udp client
# 创建一个UDP的socket，不用连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据，这里我们并不需要回复了
    print(s.recv(1024).decode('utf-8'))
s.close()


# 电子邮件

# MUA：Mail User Agent——邮件用户代理
# MTA：Mail Transfer Agent——邮件传输代理
# MDA：Mail Delivery Agent——邮件投递代理
# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

# 下面写了个简单的发送多种格式邮件的脚本
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr,formataddr

# 定义一个函数来格式化邮件地址
def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
# 发送地址
from_addr = '362240111@qq.com'
# 发送邮件密码，如果开启了验证的，则需要获取到这个加密的密码，不是你的邮箱账户密码哦
password = 'xxxxxxx'
# 收件地址
to_addr = 'gochna@sina.com'
# 发件MTA SMTP server
smtp_server = 'smtp.qq.com'
# 邮件主题
subject = 'Picture and html mail test'

# 同时支持html和plain格式
msg = MIMEMultipart('alternative')
# 格式化发件地址
msg['From'] = _format_addr('Python lover <{0}>'.format(from_addr))
# 格式化收件地址
msg['To'] = _format_addr('root <{0}>'.format(to_addr))
msg['Subject'] = Header(subject,'utf-8')

# html 格式，嵌入图片就是那个cid:0，表示图片I，就是下面的<0>
underline = """
    <html>
      <head>测试一下</head>
      <body>
        <p>兄弟们!<br>
           你们好啊<br>
           点击进入 <a href="https://www.python.org/">Python</a>
           <br><img src="cid:0"></br>
        </p>
      </body>
    </html>
"""
# 构造html
underly = MIMEText(underline,'html','utf-8')
msg.attach(underly)

# 构造图片
with open('1.png','rb') as f:
    msgImage = MIMEImage(f.read())
msgImage.add_header('Content-ID','<0>')
msg.attach(msgImage)

# 构造附件
att = MIMEText(open('sslocal.tar.gz','rb').read(),'base64','utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attatchment;filename="sslocal.tar.gz"'
msg.attach(att)

# 发送哟件
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()




# POP3收取邮件

import poplib
from functools import reduce
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


# 下载邮件
def down_email():
    # 邮件地址，口令和POP3服务器地址
    email = 'gochna@sina.com'
    password = 'Yin1110!'
    pop3_server = 'pop3.sina.com'
    # 连接到POP3服务器
    server = poplib.POP3(pop3_server)
    # 打印POP3服务器的欢迎文字
    print(server.getwelcome().decode('utf-8'))
    # 开启debug
    server.set_debuglevel(1)
    # 身份认真
    server.user(email)
    server.pass_(password)
    # 返回邮件的数量和占用的空间(单位为字节)
    print('Messages: %s. Size: %s' % server.stat())
    # list 方法返回[response,['msg_number,octet'...],octets]
    # response为响应结果(包含总的字节大小)，msg_number为邮件编号，octet为每个邮件的大小(单位为字节)，octets为list方法返回数据大小(单位为字节)
    resp,mails,octets = server.list()
    print(resp,mails,octets)
    # 我们可以用如下方法来试试看，结果是不是这样的
    mailSizeList = list(map(lambda x:int(x.decode('utf-8').split(' ')[1]),mails))
    mailTotalSize = reduce(lambda x,y:x+y,L)
    print(mailTotalSize)

    # 获取最新一封邮件，注意从索引1开始，默认下标越大，邮件越新，所以index就表示最新的邮件
    index = len(mails)
    # retr方法返回 ['response','data','octet']
    # response 为响应结果(包含邮件大小),data 为邮件的二进制数据，待会我们再做处理,octet为邮件大小(单位字节)
    resp,lines,octets = server.retr(index)
    # 获得邮件的原始文本
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)
    return msg
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    server.quit()

# 邮件的subject或者Email中包含的名字都是经过编码后的str，要正常显示，就必须先decode
def decode_str(s):
    # 取parseaddr(msg.get('xxx')) 或者 msg.get('Subject')的内容，也就是编码的部分，然后返回一个list(值和编码)，然后对value值进行解码
    value,charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

# 文本邮件的内容也是str,还需要检测编码，
# 否则，非UTF-8编码的邮件都无法正常显示：
def guess_charset(msg):
    # 获取字符集
    charset = msg.get_charset()
    if charset is None:
        # content_type变小写
        content_type = msg.get('Content-Type','').lower()
        # 检测字符串中是否包含charset=
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def print_info(msg,indent=0):
    if indent == 0:
        # 遍历From，To，Subject
        for header in ['From','To','Subject']:
            # 获取对应的内容
            value = msg.get(header,'')
            # 有内容
            if value:
                # 如果是subject
                if header == 'Subject':
                    value = decode_str(value)
                # 如果是From or To
                else:
                    # 解析字符串，返回一个元组(编码的name，邮件地址)
                    hdr,addr = parseaddr(value)
                    # 对编码的部分进行解码
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name,addr)
            print('%s%s: %s' % (' ' * indent,header,value))

    # 如果消息由多个部分组成
    if (msg.is_multipart()):
        # 返回list，包含所有子对象
        parts = msg.get_payload()
        # enumerate将其组成一个索引序列，利用它可以同时获得索引和值
        for n,part in enumerate(parts):
            # 打印消息模块编号
            print('%spart %s' % (' ' * indent,n))
            # 打印分隔符
            print('%s---------------------' % (' ' * indent))
            # 递归处理，处理到msg没有多个部分的时候，执行下面的else部分的代码
            print_info(part,indent + 1)
    else:
        # 返回消息的内容类型
        content_type = msg.get_content_type()
        # 如果是text或者html类型
        if content_type == 'text/plain' or content_type=='text/html':
            # 返回list，包含所有子对象并解码
            content = msg.get_payload(decode=True)
            # 猜测字符集
            charset = guess_charset(msg)
            # 字符集不能为空
            if charset:
                # 解码
                content = content.decode(charset)
            print('%sText: %s' % (' ' * indent,content+'...'))
        else:
            print('%sAttachment: %s' % (' ' * indent,content_type))


# SQLite
#SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，体积小，所以经常被集成到各种应用程序中
# 表是数据库中存放关系数据的集合

import sqlite3,os
# __file__获取当前文件位置，通过join，组成完整的db_file路径
db_file = os.path.join(os.path.dirname(__file__),'test.db')
# db文件如果存在就删除
if os.path.isfile(db_file):
    os.remove(db_file)
#连接到sqlite数据库
conn = sqlite3.connect(db_file)
# 创建一个cursor
cursor = conn.cursor()
# 通过cursor来执行sql语句
cursor.execute('create table user(id varchar(20) primary key, name varchar(20),score int)')
cursor.execute(r"insert into user values('A-001','Adam',95)")
cursor.execute(r"insert into user values('A-002','Bart',62)")
cursor.execute(r"insert into user values('A-003','Lisa',78)")
# 执行完成后记得关闭cursor
cursor.close()
# 提交事务，不提交的话，执行的语句没用
conn.commit()
# 关闭连接
conn.close()

def get_score_in(low,high):
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        # 查询数据，如果有参数，那么需要将参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数
        cursor.execute('select name from user where ?<=score and score<=? order by score ASC',(low,high))
        # 通过fetchall()获得查询结果集
        values = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return [i[0] for i in values]
使用cursor对象可以执行select，insert，update，delete等语句


#mySQL
# 安装mysql之后，记得将编码改成utf-8
# 安装mysql驱动
# pip install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector
# 创建数据库连接
conn = mysql.connector.connect(user='root',password='root',database='test')
# 创建cursor
cursor = conn.cursor()
# 创建user表，并插入数据
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id,name) values (%s,%s)',['1','Michael'])
# 提交事务
conn.commit()
# 关闭cursor
cursor.close()
# 关闭数据库连接
conn.close()
# 执行查询，和SQLite不同，MYSQL的占位符是%s
cursor.execute('select * from user where id = %s',('1',))
# 获取查询的值
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


# ORM
#!/usr/bin/python3
#-*- coding:utf-8 -*-

from sqlalchemy import Column, String, create_engine,Table,MetaData,Integer,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base
# 一对多
# 创建对象的基类
Base = declarative_base()

class Parent(Base):
    # 表的名称
    __tablename__ = 'parent'
    # 表的结构
    id = Column(Integer,primary_key=True)
    parent_name = Column(String(20))
    # 一对多
    child = relationship('Child',backref='parent')
    def __str__(self):
        return 'id:%s,parent_name:%s,child:%s'%(self.id,self.parent_name,self.child)
    __repr__ = __str__

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer,primary_key=True)
    child_name = Column(String(20))
    # 多的一方的child表是通过外键关联到parent表的
    parent_id = Column(Integer,ForeignKey('parent.id'))
    def __str__(self):
        return 'id:%s,child_name:%s,parent_id:%s' % (self.id,self.child_name,self.parent_id)
    __repr__=__str__

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://root:root@172.29.19.37:3306/test')
# 创建所有表
Base.metadata.create_all(engine)
# 创建DBSession，绑定engine
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()

# 创建各个对象
kevinguo = Parent(id='1',parent_name='kevinguo')
kaiz = Child(id='1',child_name='kaiz',parent_id='1')
zhihuic = Child(id='2',child_name='zhihuic',parent_id='1')
# 将数据添加到session
session.add_all([kevinguo,kaiz,zhihuic])
# 提交事务
session.commit()
session.close()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(Parent).filter(Parent.parent_name=='kevinguo').one()
session.close()

# 多对一

# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer,primary_key=True)
#     parent_name = Column(String(20))
#     child_id = Column(Integer,ForeignKey('child.id'))
#     child = relationship('Child',backref='parent')
#     def __str__(self):
#         return 'id:%s,parent_name:%s,child:%s'%(self.id,self.parent_name,self.child)
#     __repr__ = __str__
#
# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer,primary_key=True)
#     child_name = Column(String(20))
#     def __str__(self):
#         return 'id:%s,child_name:%s' % (self.id,self.child_name)
#     __repr__=__str__

# kevinguo = Parent(id='1',parent_name='kevinguo',child_id='1')
# kaiz = Parent(id='2',parent_name='kaiz',child_id='1')
# weiy = Child(id='1',child_name='weiy')

# 一对一
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer,primary_key=True)
    parent_name = Column(String(20))
    child_id = Column(Integer,ForeignKey('child.id'))
    child = relationship('Child',back_populates="parent")
    def __str__(self):
        return 'id:%s,parent_name:%s,child:%s'%(self.id,self.parent_name,self.child)
    __repr__ = __str__

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer,primary_key=True)
    child_name = Column(String(20))
    parent=relationship("Parent",back_populates="child",uselist=False)
    def __str__(self):
        return 'id:%s,child_name:%s' % (self.id,self.child_name)
    __repr__=__str__

engine = create_engine('mysql+mysqlconnector://root:root@172.29.19.37:3306/test')
Base.metadata.create_all(engine)

kevinguo = Parent(id='1',parent_name='kevinguo',child_id='1')
kaiz = Parent(id='2',parent_name='kaiz',child_id='1')
weiy = Child(id='1',child_name='weiy')
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add_all([kevinguo,kaiz,weiy])
session.commit()
session.close()

user = session.query(Parent).all()
print([x for x in user])
session.close()

# 我们还可以使用下面的方式来创建表
# metadata = MetaData()
# users_table = Table('user',metadata,
#                     Column('id',Integer,primary_key=True),
#                     Column('name',String(20)),
#                     Column('password',String(20))
#                     )
# engine = create_engine('mysql+mysqlconnector://root:root@172.29.19.37:3306/test',echo=True)
# conn = engine.connect()
# users_table.create(bind=engine)

# engine.execute(
#     r"INSERT INTO test.user(id,name,password) VALUES ('2','michael','234566');"
# )
# conn.execute(users_table.insert(),{'id':3,'name':'bobo','password':'kevinguo'})
# conn.close()



# HTTP协议简介

# 1.http request headers
# GET / HTTP/1.1
# Host: www.sina.com
# 如果请求是POST，那么请求还会包含body，包含请求数据

# 2.http response headers (可选body，但是通常都会有body)
# 200 OK
# Content-Type: text/html 浏览器靠这个来判断响应内容是啥

# 3.other resources request
# 如果浏览器还要请求其他的资源，那么会再次发出HTTP请求，重复12步骤

# HTTP格式如下
# 每个Header一行一个，换行符是\r\n
# 遇到连续两个\r\n，header部分结束，后面全是body
# http响应如果包含body，是通过\r\n\r\n来分割的


# HTML简介
# HTML是由一系列的Tag组成，最外层的是<html></html>，由于html是富文档模型，所以还有一些tag来表示链接，图片，表格，表单等
# CSS 用来控制HTML里的所有元素如何展现
# javascript是为了让HTML具有交互性而作为脚本语言添加的，javascript可以内嵌到html中，也可以从外部链接到html中


# WSGI接口 (web server gateway interface)
# 最简单的web应用就是把HTML文件用文件保存好，然后用一个现成的HTTP服务器软件，来接受用户请求，从文件中读取html，返回。如nginx，apache
# 如果要动态生成html，我们可以忽略掉底层的代码，用python专注生成html，所以，需要一个统一的接口，这个接口就是wsgi
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数
# environ: 一个包含所有HTTP请求信息的dict对象
# start_response: 一个发送HTTP响应的函数
# HTTP请求的所有输入信息都可以通过environ获得
# HTTP响应的输出都可以通过start_response()加上函数返回值作为body
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body = '<h1>Hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
# 复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。



# Flask框架
# Flask通过request.form['name']来获取表单的内容
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return '''
    <form action="/signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>
    '''

@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='admin':
        return '<h2>hello,admin!</h2>'
    return '<h2>Bad username or password.</h2>'

if __name__ == '__main__':
    app.run()


# 使用模板

# 我们前面的例子中，函数中包含了HTML，但是，我们知道，如果你要写一个几千行的HTML，怎么可能在python中用字符串写出来
# 所以，我们需要模板，即MVC(module view controller)
# 这个模板不是普通的模板，而是嵌入了一些变量和指令，然后，根据我们传入的数据，渲染后，得到最终的HTML
from flask import Flask
from flask import request
from flask import render_template

# app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__
app = Flask(__name__)

# URL和函数的路由
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
    # Flask通过request.form['name']来获取表单的内容
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        # 说白了，其实render_template的功能是先引入signin-ok.html，同时根据后面传入的参数，对html进行修改渲染
        return render_template('signin-ok.html',username=username)
    # 这里就是引入form.html，然后根据后面传入的参数，对form.html进行渲染
    return render_template('form.html',message='Bad username or password',username=username)

if __name__ == '__main__':
    app.run()


# 异步和IO多路复用
# 这其实就是事件驱动的 epoll IO模型，本质上还是 同步IO。
# 真正意义上的 异步IO 是说内核直接将数据拷贝至用户态的内存单元，再通知程序直接去读取数据。
# select / poll / epoll 都是同步IO的多路复用模式

# 1.同步和异步
# 同步和异步关注的是消息通信机制
# 所谓同步，就是在发出一个*调用*时，没得到结果之前，该*调用*就不返回。但是一旦调用返回就得到返回值了，*调用者*主动等待这个*调用*的结果
# 所谓异步，就是在发出一个*调用*时，这个*调用*就直接返回了，不管返回有没有结果。当一个异步过程调用发出后，*被调用者*通过状态，通知来通知*调用者*，或者通过回调函数处理这个调用

# 2.阻塞和非阻塞
# 阻塞和非阻塞关注的是程序在等待调用结果时的状态
# 阻塞调用是指调用结果返回之前，当前线程会被挂起。调用线程只有在得到结果之后才返回
# 非阻塞调用是指在不能立即得到结果之前，该调用不会阻塞当前线程

# 网络上的例子
#老张爱喝茶，废话不说，煮开水。
#出场人物：老张，水壶两把（普通水壶，简称水壶；会响的水壶，简称响水壶）。
#1 老张把水壶放到火上，立等水开。（同步阻塞）；立等就是阻塞了老张去干别的事，老张得一直主动的看着水开没，这就是同步
#2 老张把水壶放到火上，去客厅看电视，时不时去厨房看看水开没有。（同步非阻塞）；老张去看电视了，这就是非阻塞了，但是老张还是得关注着水开没，这也就是同步了
#3 老张把响水壶放到火上，立等水开。（异步阻塞）；立等就是阻塞了老张去干别的事，但是老张不用时刻关注水开没，因为水开了，响水壶会提醒他，这就是异步了
#4 老张把响水壶放到火上，去客厅看电视，水壶响之前不再去看它了，响了再去拿壶。（异步非阻塞）；老张去看电视了，这就是非阻塞了，而且，等水开了，响水壶会提醒他，这就是异步了
#所谓同步异步，只是对于水壶而言。普通水壶，同步；响水壶，异步。对应的也就是消息通信机制
#虽然都能干活，但响水壶可以在自己完工之后，提示老张水开了。这是普通水壶所不能及的。同步只能让调用者去轮询自己（情况2中），造成老张效率的低下。
#所谓阻塞非阻塞，仅仅对于老张而言。立等的老张，阻塞；对应的也就是程序等待结果时的状态
#看电视的老张，非阻塞。
#情况1和情况3中老张就是阻塞的，媳妇喊他都不知道。虽然3中响水壶是异步的，可对于立等的老张没有太大的意义。所以一般异步是配合非阻塞使用的，这样才能发挥异步的效用。

# 栈和堆

# 桶栈(LIFO)
# 栈是计算机内存的一个特殊区域，它是一个LIFO的数据结构，它存储着由函数创建的临时变量，栈中分配的都是局部变量。
# 栈是由CPU来管理和优化的，不需要你手动来分配或释放内存
# 既然由CPU来组织栈内存，因此读取和写入栈内存的速度非常快
# 每次函数声明一个新变量时，它都被“push”到栈中。然后每次函数退出时，所有由该函数压入堆栈的变量都被释放（也就是说，它们被删除）。
# 一旦释放堆栈变量，该区域的内存就可用于其他堆栈变量。
# 栈有大小的限制

# 树堆(堆的特点是根节点的值要么最大要么最小)
# 堆是计算机内存中的一个区域，堆中分配的变量可以被全局访问。
# 堆不会自动为你进行管理，而且不受严格的CPU管理。它是一个更自由浮动的内存区域
# 与栈不同，堆没有可变大小的大小限制（除了计算机明显的物理限制外）。由于必须使用指针访问堆上的内存，因此堆内存的读取和写入速度稍慢
# 如果你要分配堆内存，那么你必须手动指定malloc()或calloc()。如果你要释放堆内存，也必须的手动操作free()
# 如果你忘记手动释放的话，可能会出现内存泄漏，也就是说该内存还被保留着，并不会给其他进程使用。



# 协程
# 微线程，纤程，包含于线程
# 协程就是你可以暂停执行的函数，我们可以把它理解成“就像生成器一样”
# 线程内部的协程，通过中断暂停的方式，完成多个任务
# 协程是用户自己来编写调度逻辑的，对CPU来说，协程是单线程，CPU不用去考虑怎么调度、切换上下文，省去了CPU的切换开销，所以协程在一定程度上又好于多线程。
# 协程的特点在于每次只有一个线程，不存在线程切换的消耗，有点类似于CPU的中断，所以，不存在多线程的锁机制，不存在变量冲突
# 如果我们要利用多核CPU，可以使用多进程+协程，既充分利用多核，又充分发挥协程的高效率

# 用个例子来理解下协程的过程
# 这里是一个传统的生产者-消费者模型
# 这个例子的关键，在于要记住yield在这里即接受send()发过来的值，也返回值
def consumer():
    r = None
    while True:
        # 2.consumer通过yield拿到传递的None，yield跳出
        n = yield r
        # 4.从上次跳出的位置，接着往下执行
        if not n:
            return
        print('[CONSUMER] Consuming %s ...' % n )
        r = '200 OK'
        # 6.从这里开始循环，到yield的时候，再跳出来

def produce(c):
    # 1.启动生成器，会跳到consumer
    c.send(None)
    # 3.接着往下执行，产生数据，通过c.send(n)，再切换到consumer
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s ...' % n )
        r = c.send(n)
        # 7.跳出来后，函数返回值是200 OK，所以往下执行，print出200 OK
        print('[PRODUCER Consumer return: %s' % r)
        # 8.从这里开始循环前面的步骤，直到最后
    c.close()

c = consumer()
produce(c)


# asyncio

# 前面的yield返回了一个生成器
# 而这里的yield from解析了生成器对象，将其中的每个item返回了，yield from iterable 本质上等于for item in iterable: yield item
# yield from 后面必须跟iterable对象(可以是生成器，迭代器)
# yield from语法可以让我们方便地调用另一个generator

import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 试试注释掉这行，你会发现，这时候是按顺序执行的，因为中间没有IO耗时操作，所以就没有中断
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    # 返回的是generator,内容是reader和writer
    connect = asyncio.open_connection(host, 80)
    # 这里就直接yield from 调用了这个coroutine
    reader, writer = yield from connect
    # 指定header
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    # 这算是操作了
    writer.write(header.encode('utf-8'))
    # 刷新底层传输的写缓冲区。也就是把需要发送出去的数据，从缓冲区发送出去。没有手工刷新，asyncio为你自动刷新了，针对内存不足的时候， 写一下刷一下，写一下刷一下
    yield from writer.drain()
    while True:
        # 这部分是读取文件内容，自行调度reader.readline()这个协程
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in [ 'www.163.com','www.sina.com.cn','www.python.org']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()


# async/await
# 使用asyncio提供的@asyncio.coroutine可以把一个genterator标记为coroutine类型，然后在内部使用yield from调用另一个coroutine实现异步操作
# 为了简化并更好的标识异步IO，从python3.5开始引入新的语法async和await，可以让coroutine的代码更简单
# @asyncio.coroutine 替换为async
# yield from 替换为await

import asyncio
async def hello():
    print('hello world!')
    r = await asyncio.sleep(1)
    print('hello again!')

# 下面这个例子，最能说明协程的工作原理
async def outer():
    print('in outer')
    print('waiting for result1')
    result1 = await phase1()
    print('waiting for result2')
    result2 = await phase2(result1)
    return (result1,result2)

async def phase1():
    print('in phase1')
    return 'result1'

async def phase2(arg):
    print('in phase2')
    return 'result2 derived from {}'.format(arg)

loop = asyncio.get_event_loop()
tasks = [outer()]
return_value = loop.run_until_complete(asyncio.wait(tasks))
print(return_value)
loop.close()


# aiohttp
# asyncio 可以实现单线程并发IO操作。
# asyncio实现了TCP,UDP,SSL等协议，aiohttp则是基于asyncio实现的HTTP框架
# aiohttp的具体用法，改天再看
import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
