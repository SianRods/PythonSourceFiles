In Python, variables starting with an underscore (e.g., `_name`) follow a naming convention that signals their intended scope and use. Here's a breakdown:

1. **Single Leading Underscore (`_name`)**: 
   - A single leading underscore is a convention that indicates a variable is intended for **internal use** only. However, this is just a convention and does not restrict access to the variable.
   - Example:
     ```python
     class MyClass:
         def __init__(self):
             self._internal_var = "This is an internal variable"
     obj = MyClass()
     print(obj._internal_var)  # This is accessible
     ```

2. **Double Leading Underscore (`__name`)**: 
   - This triggers **name mangling** in Python. The interpreter modifies the variable name to prevent it from being accidentally overridden in subclasses. It changes the variable name by adding `_ClassName` before the actual variable name.
   - Example:
     ```python
     class MyClass:
         def __init__(self):
             self.__private_var = "This is a private variable"
     obj = MyClass()
     print(obj.__private_var)  # Raises an AttributeError
     print(obj._MyClass__private_var)  # This works due to name mangling
     ```

3. **Single Trailing Underscore (`name_`)**: 
   - This is used to avoid conflicts with Python keywords or built-in names.
   - Example:
     ```python
     class MyClass:
         def __init__(self):
             self.class_ = "Avoids conflict with the 'class' keyword"
     ```

Let me know if you need more details on accessing or modifying these variables!