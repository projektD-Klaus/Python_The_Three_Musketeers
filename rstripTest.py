# delete the space within strings.s

str="   ddjj  "
str=str.rstrip()
print(str)
print(len(str))
#只移除末尾空白 r:right
str=str.lstrip()
print(str)
print(len(str))