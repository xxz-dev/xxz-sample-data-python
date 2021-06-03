import sys
import ast

def non_conformant_1(c):
    command = 'os.system("%s")' % c
    eval(command)

def non_conformant_2(command):
    eval(command)

def non_conformant_3():
    c = input()
    eval(c)

def non_conformant_4():
    c = sys.argv[0]
    eval(c)

def non_conformant_5():
    with open('file.txt') as f:
        for line in f:
            eval(line)

def conformant_1():
    c = '1 + 2'
    eval(c)

def conformant_3():
    c = input()
    ast.literal_eval(c)

def conformant_4():
    f = open('file.txt')
    command = f.read()
    ast.literal_eval(command)