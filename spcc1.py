import re

keyword = ['break','case','char','const','countinue','deafult','do','int','else','enum','extern','float','for','goto','if','long','register','return','short','signed','sizeof','static','switch','typedef','union','unsigned','void','volatile','while']
built_in_functions = ['clrscr()','printf(','scanf(','getch()','main()']
operators = ['+','-','*','/','%','==','!=','>','<','>=','<=','&&','||','!','&','|','^','~','>>','<<','=','+=','-=','*=']
specialsymbol = ['@','#','$','_','!']
separator = [',',':',';','\n','\t','{','}','(',')','[',']']

dispkey=[]
dispBIF=[]
dispOp=[]
dispSpecial=[]
dispSep=[]
dispHeader=[]
dispNumerals=[]
dispIdentifier=[]
file = open('hello.txt','r+')
contents = file.read()
splitCode = contents.split() 
length = len(splitCode)      
for i in range(0,length):
    if splitCode[i] in keyword:
        dispkey.append(splitCode[i])
        continue
    if splitCode[i] in operators:
        dispOp.append(splitCode[i])
        continue
    if splitCode[i] in specialsymbol:
        dispSpecial.append(splitCode[i])
        continue
    if splitCode[i] in built_in_functions:
        dispBIF.append(splitCode[i])
        continue
    if splitCode[i] in separator:
        dispSep.append(splitCode[i])
        continue
    if re.match(r'(#include*).*', splitCode[i]):
        dispHeader.append(splitCode[i])
        continue
    if re.match(r'^[-+]?[0-9]+$',splitCode[i]):
        dispNumerals.append(splitCode[i])
        continue
    if re.match(r"^[^\d\W]\w*\Z", splitCode[i]):
        dispIdentifier.append(splitCode[i])
  
print(f'Keywords :{dispkey}')
print(f'Keywords count : {len(dispkey)}')
print(f'Operators :{dispOp}')
print(f'Operators count : {len(dispOp)}')
print(f'Special Symbols :{dispSpecial}')
print(f'Special Symbols count : {len(dispSpecial)}')
print(f'Built-in Functions :{dispBIF}')
print(f'Built-in Functions count : {len(dispBIF)}')
print(f'Separators :{dispSep}')
print(f'Separators count : {len(dispSep)}')
print(f'Header files :{dispHeader}')
print(f'Header files count : {len(dispHeader)}')
print(f'Numerals :{dispNumerals}')
print(f'Numerals count : {len(dispNumerals)}')
print(f'Identifiers :{dispIdentifier}')
print(f'Identifiers count : {len(dispIdentifier)}')
