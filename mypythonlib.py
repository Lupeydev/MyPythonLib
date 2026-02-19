import os

# C++ Output
def cout(word):
    print(word)

#Java Output
def System_out_print(word):
        print(word)

#C# Output
def Console_WriteLine(word):
    print (word)

# Output Variable for C
def printf(word):
     print(word)

# Input Variable for C++
def cin(inputted):
    varcin = input(inputted)
    return varcin

# Input Variable for C#
def Console_ReadLine(inputted):
    varReadLine = input(inputted)
    return varReadLine

# Input Variable for C
def scanf(inputted):
     varScanF = input(inputted)
     return varScanF

# Converts the varable to Int32 in C# Syntax
def Convert_ToInt32(convertvar):
    return int(convertvar)

def Convert_ToString(convertvar):
     return str(convertvar)

# Increment the number by 1
def plusinc(varas):
     varas += 1
     return varas

def minusinc(varas):
     varas -= 1
     return varas

def killcode():
    import ctypes  
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    Mbox('Woah', 'Why are you trying to kill your code', 16)

def ReadFile(filename):
     contents = open(filename)
     return contents

def DeleteFile(filename):
     os.remove(filename)

def Clear():
     os.system("cls")