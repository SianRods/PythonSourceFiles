class ClassName:

    def __init__(self,para1,para2,para3):
        self.public = para1
        self._protected=para2 # Just Like Public 
        self.__private = para3  # Cannot be accessed outside class with instance name 


c1=ClassName(10,12,244)

print(f" Public values of C1 : {c1.public}")
print(f"Protected Values of C1 : {c1._protected}")
# changing the protected variable 
c1._protected=23
print(f"Protected Value of C1 has now been updated to : {c1._protected}")
# print(c1.__private) 
print(f"Private Variables : {c1._ClassName__private}")
        