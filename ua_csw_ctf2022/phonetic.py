import sys

s = ["charlie","tango", "foxtrot","uniform","alfa","{","three","november","charlie","romeo","yankee","papa","tango","three","delta","comma","_","tango","hotel","one","sierra","_", "india","sierra","_","november","zero","tango","}"]

codes = {
    "alfa"   : 'a',
    "bravo"   : 'b',
    "charlie"   : 'c',
    "delta"   : 'd',
    "echo"    : 'e',
    "foxtrot"   : 'f',
    "golf"    : 'g',
    "hotel"   : 'h',
    "india"   : 'i',
    "juliet"    : 'j',
    "kilo"    : 'k',
    "lima"    : 'l',
    "mike"    : 'm',
    "november"    : 'n',
    "oscar"   : 'o',
    "papa"    : 'p',
    "quebec"    : 'q',
    "romeo"   : 'r',
    "sierra"    : 's',
    "tango"   : 't',
    "uniform"   : 'u',
    "victor"    : 'v',
    "whisky"    : 'w',
    "xRay"    : 'x',
    "yankee"    : 'y',
    "zulu"    : 'z',
    "zero"    : '0',
    "one"   : '1',
    "two"   : '2',
    "three"   : '3',
    "four"    : '4',
    "five"    : '5',
    "six"   : '6',
    "seven"   : '7',
    "eight"   : '8',
    "nine"    : '9',
    "_"   : '_',
    "{"   : '{',
    "}"   : '}',
    "comma" : ','
}

for lettre in s:
    if lettre in codes:
        print(codes[lettre], end="")
print()
