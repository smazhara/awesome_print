""" Attempt to clone https://github.com/michaeldv/awesome_print

Usage:
    ap(object)
"""
import __builtin__
from types import *

mode = 'ansi'

def ap(*args):
    for arg in args:
        print format(arg)

def indent(level):
    return '  ' * level

def format(obj, level = 0):
    type = __builtin__.type(obj)

    if type is NoneType:
        return red('None')

    if type is TypeType:
        pass

    if type is BooleanType:
        return green(str(obj))

    if type in [StringType, UnicodeType]:
        return yellow(str(obj))

    if type in [IntType, LongType, FloatType, ComplexType]:
        return bold_blue(str(obj))

    if type in (TupleType, ListType):
        open, close = ('(', ')') if type is TupleType else ('[', ']')
        if len(obj) is 0:
            return open + close

        s = []
        i = 0
        width = str(len(str(len(obj))))
        for e in obj:
            s.append(('%s[%' + width + 'd] %s') % \
                    (indent(level + 1), i, format(e, level + 1)))
            i+=1

        return open + "\n" + \
                        ",\n".join(s) + \
               "\n" + indent(level) + close

    if type is DictType:
        if len(obj) is 0:
            return '{}'

        width = str(max([flen(format(k)) for k in obj.keys()]))
        s = []
        for k in obj.keys():
            v = obj[k]
            s.append(('%s%' + width + 's: %s') % \
                    (indent(level + 1), format(k), format(v, level + 1)))

        return '{' + "\n" + \
                        ",\n".join(s) + \
               "\n" + indent(level) + '}'

    if type is LambdaType:
        return str(obj)

    return str(obj)

def flen(str):
    return max(len(s) for s in str.split("\n"))

def black(str):
    return color(str, '30')

def dark_gray(str):
    return bold(str, '30')

def red(str):
    return color(str, '31')

def bold_red(str):
    return bold(str, '31')

def green(str):
    return color(str, '32')

def green(str):
    return bold(str, '32')

def yellow(str):
    return color(str, '33')

def bold_yellow(str):
    return bold(str, '33')

def blue(str):
    return color(str, '34')

def bold_blue(str):
    return bold(str, '34')

def purple(str):
    return color(str, '35')

def bold_purple(str):
    return bold(str, '35')

def cyan(str):
    return color(str, '36')

def bold_cyan(str):
    return bold(str, '36')

def light_gray(str):
    return color(str, '37')

def white(str):
    return bold(str, '37')

def color(str, color, intensity='0'):
    if mode == 'plain':
    	return str
    return '\033['+intensity+';'+color+'m'+str+'\033[0m'

def bold(str, col):
    if mode == 'plain':
    	return str
    return color(str, col, '1')
