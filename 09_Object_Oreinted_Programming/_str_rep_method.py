# ----------------------------------------------------------------------------------------------
# Implementing the toString() Method Similar to Java we have __str__() method in python 


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
    
    # Defining the __str__() method :
    def __str__(self):
            return f"name of the student is {self.name}"


s1=StudentDataBase("Sian Rodrigues ",19,14,{})

print(s1)