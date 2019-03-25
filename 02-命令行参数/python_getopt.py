#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt

print "获取命令行 参数个数为:", len(sys.argv), "个"
print "获取命令行 参数列表为:", str(sys.argv)

# python命令行参数：
# http://www.runoob.com/python/python-command-line-arguments.html
# 函数：getopt.getopt   
# 函数：getopt.GetoptError:

def main(argv):
    filename = sys.argv[0]
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print filename, "-i <inputfile> -o <outputfile>"
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print filename, "-i <inputfile> -o <outputfile>"
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print '输入的文件为：', inputfile
    print '输出的文件为：', outputfile

if __name__ == "__main__":
    main(sys.argv[1:])

x = "100"
y = int(x, base=10)
print y
