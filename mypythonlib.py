import os
import sys

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

def killcode(varprompt):
     import ctypes  
     def Mbox(title, text, style):
          return ctypes.windll.user32.MessageBoxW(0, text, title, style)
     Mbox('Woah', 'Why are you trying to kill your code', 16)
     sys.exit()

def ReadFile(filename):
     contents = open(filename)
     print(contents)
     return contents

def DeleteFile(filename):
     os.remove(filename)

def new_File(filename):
     open(filename, "x") 

def append_File(filename, content):
     with open(filename, "a") as f:
          f.write(content)

def write_File(filename, content):
     with open(filename, "w") as f:
          f.write(content)

def Clear():
     os.system("cls")

def HowMuchCPU():
     print("Number of CPUs in the system:", os.cpu_count())

def PythonVersion():
     print(sys.version)

def PythonVersionExtended():
     print(sys.version_info)

def ListModules():
     print(sys.modules)

def Platform():
     print(sys.platform)