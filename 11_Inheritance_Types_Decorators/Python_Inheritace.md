In Python, inheritance allows one class (called the child or subclass) to inherit attributes and methods from another class (called the parent or superclass). Python supports multiple types of inheritance:

### 1. **Single Inheritance**
   - A subclass inherits from one parent class.
   - This is the simplest form of inheritance.
   
   ```python
   class Parent:
       def display(self):
           print("This is the parent class")
   
   class Child(Parent):
       def show(self):
           print("This is the child class")

   obj = Child()
   obj.display()  # Inherited method from Parent
   obj.show()     # Child's own method
   ```

### 2. **Multiple Inheritance**
   - A subclass can inherit from more than one parent class.
   - Python allows a class to have multiple base classes.
   
   ```python
   class Parent1:
       def method1(self):
           print("Parent1 method")

   class Parent2:
       def method2(self):
           print("Parent2 method")

   class Child(Parent1, Parent2):
       def method3(self):
           print("Child method")

   obj = Child()
   obj.method1()  # Inherited from Parent1
   obj.method2()  # Inherited from Parent2
   obj.method3()  # Child's own method
   ```

### 3. **Multilevel Inheritance**
   - A subclass inherits from a parent class, which in turn inherits from another parent class (grandparent).
   
   ```python
   class Grandparent:
       def method1(self):
           print("Grandparent method")

   class Parent(Grandparent):
       def method2(self):
           print("Parent method")

   class Child(Parent):
       def method3(self):
           print("Child method")

   obj = Child()
   obj.method1()  # Inherited from Grandparent
   obj.method2()  # Inherited from Parent
   obj.method3()  # Child's own method
   ```

### 4. **Hierarchical Inheritance**
   - Multiple subclasses inherit from the same parent class.
   
   ```python
   class Parent:
       def method(self):
           print("Parent method")

   class Child1(Parent):
       def method1(self):
           print("Child1 method")

   class Child2(Parent):
       def method2(self):
           print("Child2 method")

   obj1 = Child1()
   obj2 = Child2()
   obj1.method()   # Inherited from Parent
   obj2.method()   # Inherited from Parent
   ```

### 5. **Hybrid Inheritance**
   - A combination of two or more types of inheritance.
   - Typically involves complex structures and may involve both multiple and multilevel inheritance.
   
   ```python
   class Parent:
       def method(self):
           print("Parent method")

   class Child1(Parent):
       def method1(self):
           print("Child1 method")

   class Child2(Parent):
       def method2(self):
           print("Child2 method")

   class GrandChild(Child1, Child2):
       def method3(self):
           print("GrandChild method")

   obj = GrandChild()
   obj.method()    # Inherited from Parent
   obj.method1()   # Inherited from Child1
   obj.method2()   # Inherited from Child2
   obj.method3()   # GrandChild's own method
   ```

### Method Resolution Order (MRO)
In Python, especially with multiple inheritance, the **MRO** defines the order in which methods are inherited. Python uses the **C3 linearization algorithm** (or C3 superclass linearization) to determine the method lookup order.

You can check the MRO using:

```python
print(Child.mro())
```

These types of inheritance allow flexibility and code reusability in Python's object-oriented programming.