# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:11:08 2020

@author: Abdul
"""

def sayHello(name): return f'Hello {name}'


def sayHowRU(name): return f'How Are You {name}?'


keyboardE = {
    '`': 'ذ',
    '[': 'ج',
    ']': 'د',
    'p': 'ح',
    'o': 'خ',
    'i': 'ه',
    'u': 'ع',
    'y': 'غ',
    't': 'ف',
    'r': 'ق',
    'e': 'ث',
    'w': 'ص',
    'q':'ض'
    ,"'": 'ط',
        ';': 'ك',
    'l': 'م',
    'k': 'ن',
    'j': 'ت',
    'h': 'ا',
    'g': 'ل',
    'f': 'ب',
    'd': 'ي',
    's': 'س',
    'a': 'ش',
        '/': 'ظ',
    '.':'ز',
    ',':'و',
    'm': 'ة',
    'n': 'ى',
    'b': 'لا',
    'v': 'ر',
    'c': 'ؤ',
    'x': 'ء',
    'z': 'ئ',
    ' ': ' ',
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    '~': 'ّ',
	'Q': 'َ',
	'W': 'ً',
	'E': 'ُ',
	'R': 'ٌ',
	'T': 'لإ',
	'Y': 'إ',
	'U': '‘',
	'I': '÷',
	'O': '×',
	'P': '؛',
	'{': '<',
	'}': '>',
	'A': 'ِ',
	'S': 'ٍ',
	'D': ']',
	'F': '[',
	'G': 'لأ',
	'H': 'أ',
	'J': 'ـ',
	'K': '،',
	'L': '/',
	':': ':',
	'"': '"',
	'Z': '~',
	'X': 'ْ',
	'C': '}',
	'V': '{',
	'B': 'لآ',
	'N': 'آ',
	'M': '’',
	'<': ',',
	'>': '.',
    '?': '؟',
    '-': '-',
    '=': '=',
    '_': '_',
    '+': '+',
    '*': '*',
    '(': ')',
    ')': '(',
    '!': '!',
    '@': '@',
    '#': '#',
    '$': '$',
    '%': '%',
    '^': '^',
    '&': '&',
    '\\': '\\',
    '|': '|',
    '\n': '\n'
    }


def tranE_A_looped(_str):
    a_str = []
    a = ''
    
    for letter in _str: a_str.append(keyboardE[letter])
    a_str = a.join(a_str)
    
    from pyperclip import copy
    copy(a_str)        
    print(a_str)

    _str = input("Enter English Letter\s, Then Press ENTER.\nTo Stop: Type 'break'\n")
    if _str == 'break': pass
    else: tranE_A_looped(_str)

        
def tranE_A(_str, looping=False):
    a_str = []
    a = ''
    
    for letter in _str: a_str.append(keyboardE[letter])
    a_str = a.join(a_str)
    
    from pyperclip import copy
    copy(a_str)
    print(a_str)
    
    if looping==True:
        _str = input("Enter English Letter\s, Then Press ENTER.\nTo Stop: Type 'break'\n")
        if _str != 'break': tranE_A_looped(_str)



