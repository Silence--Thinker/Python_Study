#!/usr/bin/python
# -*- coding: utf-8 -*-

class Employee:
    '类的帮助/文档信息'
    empCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    def displayCount(self):
        print "total employee %d" % Employee.empCount

    def displayEmployeeInfo(self):
        print "name: %s, age: %d" % (self.name, self.age)

    def class_info(self):
        print self
        print self.__class__

    def __del__(self):
         print self.__class__.__name__, "id: ", id(self), "销毁"

employee1 = Employee('caoxiujin', 28)
employee2 = Employee('caoxiufa', 24)
employee1.displayCount()
employee1.displayEmployeeInfo()
employee2.displayCount()
employee2.displayEmployeeInfo()

# self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类。
Employee('caoxiujin', 23).class_info()

# 添加属性
employee1.profession = 'engineer'
employee2.profession = 'student'
print employee1.profession, employee2.profession
del employee1.profession
# print employee1.profession, employee2.profession   # 报错
print employee2.profession
del employee2.profession

print hasattr(employee1, 'profession')          # 如果存在 'profession' 属性返回 True。
setattr(employee1, 'profession', 'engineer')    # 添加属性 'profession' 值为 engineer
getattr(employee1, 'profession')                # 返回 'profession' 属性的值
print hasattr(employee1, 'profession')          # 如果存在 'profession' 属性返回 True。
delattr(employee1, 'profession')                # 删除属性 'profession'

# 内置类属性
print "Employee.__doc__: ", Employee.__doc__
print "Employee.__name__: ", Employee.__name__
print "Employee.__module__: ", Employee.__module__
print "Employee.__bases__: ", Employee.__bases__
print "Employee.__dict__: ", Employee.__dict__

# 对象销毁
del employee2


# 类的继承
class Father: 
    father_profession = 'engineer'
    def __init__(self, name, age):
        print "调用父类构造方法"
        print self.__class__.__name__
        self.name = name
        self.age = age

    def father_method(self):
        print '调用父类方法 father_method'

    def setAttr(self, attr):
        Father.father_profession = attr

    def getAttr(self):
        print "父类属性：", Father.father_profession

    def my_method(self):
        print '调用父类方法 my_method'


class Child(Father):
    def __init__(self):

        
        print "调用子类构造方法"
        print self.__class__.__name__

    def child_method(self):
        print '调用子类方法 child_method'

    def my_method(self):
        Father.my_method(self) # 调用父类方法需要携带self参数
        print '调用子类方法 my_method'

child = Child()
child.child_method()
child.father_method()
child.setAttr('student')
child.getAttr()
# 方法重写
child.my_method()

# 类属性与方法

# 类的私有属性: ==>> __private_attrs：两个下划线开头，声明该属性为私有，
# 不能在类的外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。

# 类的方法: ==>> 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
# 类的私有方法: ==>> __private_method：两个下划线开头，声明该方法为私有方法，
# 不能在类的外部调用。在类的内部调用 self.__private_methods

# 单下划线、双下划线、头尾双下划线说明：
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。