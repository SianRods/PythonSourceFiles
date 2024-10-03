# ----------------------------------------------------------------------------------
# The __getitem(self,key)__ and __setitem(self,key,value)__ are special types of methods 
# (dunder ) methods which can be used to define the way data is stored an retireved from 
# iterables / data storage objects like lists , tuples,dictionaries , etc 


class StudentDataBase :
    # Creating the class variables : -
    name =None
    age=19
    grade =5

    def __init__(self,name,age,grade,marks_dict_) :
        self.name=name
        self.age=age
        self.grade=grade
        self.marks_dict_={}

    
    def __setitem__(self,key,value):
        self.marks_dict_[key]=value


    def __getitem__(self,key):
        return (self.marks_dict_[key])


s1=StudentDataBase("Smayan",21,14,{})

s1.marks_dict_['English']=95

print(s1.marks_dict_)

# ----------------------------------------------------------------------------------