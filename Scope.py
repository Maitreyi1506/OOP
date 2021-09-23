#string literals
courseName="OOP course"
core_course="y"
comment="""This is a comment"""
testcode=u"\u00dcnic\u00f6de"
imp_raw_str = "raw \n string"
raw=r"raw \n string"

print(courseName,core_course,comment,testcode)
print(imp_raw_str)
print(raw)

#Literal collections
list=[1,"apple",'c']
tuple=(1,2,3,4,27)
dict={'1':'obj1','2':'obj2','3':'obj3'}
set={'d','m','o',4}

print(list)
print(tuple)
print(dict)
print(set)

# Namespaces
b=2
print("id(2)=",id(2))
print("id(b)=",id(b))