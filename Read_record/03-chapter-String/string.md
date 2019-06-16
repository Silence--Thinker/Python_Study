# 使用字符串
[toc]

## 字符串的基本操作

所有标准序列操作都适用于字符串，但是`字符串是不可变的`，因此所有的元素赋值和切片赋值都是非法的。

    >>> website = 'http://www.python.org'
    >>> website[-3] = 'com'
    TypeError: 'str' object does not support item assignment

## 设置字符串的格式（精简版）

有三种方式，设置字符串格式设置

* 使用字符串格式设置运算符——百分号
* 使用模板字符串，类似于UNIX shell的语法
* 使用字符串方法format

[相关代码](./03-01.py)

## 设置字符串的格式（完整版）

字符串格式设置涉及的内容很多。这里的基本介绍的是对字符串调用format，并提供设置其格式的值。

替换用花括号括起来的替换字段

    print "{{Hello world}}".format()
    # {Hello world}

替换字符串由如下部分组成，其中每个部分都是可选的。

* **字段名**

索引或者表示符，指出要设置哪个值的格式，并用结果来替换该字段。

* **转换标志**

跟在叹号后面的单个字符。当前支持的字符包括r（表示repr）、s（表示str）和a（表示ascii）。如果指定了转换标志，将不使用对象本身的格式设置机制，而是使用指定的函数将对象转换为字符串，在做进一步的格式设置。

* **格式说明符**

跟着冒号后面的表达式。格式说明符包括格式类型（如字符串、浮点数或者十六进制数）、字段宽度和数的精度。如何显示符号和千位分隔符，以及各种对齐和填充方式。

### 替换字段名

使用索引和字段名格式化

    print "{foo} {} {bar} {}".format(1, 2, bar=4, foo = 3)
    # 3 1 4 2

    print "{foo} {1} {bar} {0}".format(1, 2, bar=4, foo = 3)
    # 3 2 4 1

注意：不可同时使用自动编号，和手动编号。

### 基本转换

**修改转换标志**
指定字段包含的值后，还可以添加相关的转换标志。

    print("{pi!s} {pi!r} {pi!a}".format(pi="π"))
    # π 'π' '\xcf\x80'

Python3.x中的转换标志a，相当于Python2.x中转换标志r。

**修改格式说明符**

    string = "The number is {num}".format(num=42)
    print string
    # The number is 42

    # 浮点数
    string = "The number is {num:f}".format(num=42)
    print string
    # The number is 42.000000

    # 二进制数
    string = "The number is {num:b}".format(num=42)
    print string
    # The number is 101010

|类型|含义|
|:---|:---|
|b|将整数表示为二进制数|
|o|将整数表示为八进制数|
|d|将数表示为十进制数|
|x|将整数表示为十六进制数|
|f|将数表示为浮点数|
|%|将数表示为百分比值（乘以100，按说明符f设置格式，再在后面加上%）|

### 宽度、精度、和千位分隔符

### 符号、对齐和用0填充

## 字符串方法

### center

### find

### join

### lower

### replace

### split

### strip

### translate

### 判断字符串是否满足特定的条件

## 小结

### 本章介绍的新函数