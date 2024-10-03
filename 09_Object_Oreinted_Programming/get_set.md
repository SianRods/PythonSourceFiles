In Python, the `__setitem__` and `__getitem__` methods are special methods used to define how objects of a class can handle setting and retrieving values using the bracket notation (`[]`), typically associated with dictionaries, lists, or other container-like objects. These methods can be customized in user-defined classes to allow for indexing, setting, and retrieving elements like these built-in types.

### 1. `__setitem__(self, key, value)`
This method is called when an item is set in a container (like assigning a value to a specific index or key). For example, in a dictionary, `dict[key] = value` internally calls `dict.__setitem__(key, value)`.

**Usage:**
- Allows you to define how an object should handle assigning a value for a specific key or index.

**Example:**
```python
class MyDict:
    def __init__(self):
        self.data = {}
    
    def __setitem__(self, key, value):
        print(f'Setting {key} to {value}')
        self.data[key] = value

my_obj = MyDict()
my_obj['a'] = 10  # Calls my_obj.__setitem__('a', 10)
```

**Output:**
```
Setting a to 10
```

### 2. `__getitem__(self, key)`
This method is called when you retrieve an item using the bracket notation, e.g., `my_dict[key]` internally calls `my_dict.__getitem__(key)`.

**Usage:**
- Allows you to define how an object should handle retrieving a value for a specific key or index.

**Example:**
```python
class MyDict:
    def __init__(self):
        self.data = {'a': 1, 'b': 2}
    
    def __getitem__(self, key):
        print(f'Getting value for {key}')
        return self.data.get(key, None)

my_obj = MyDict()
print(my_obj['a'])  # Calls my_obj.__getitem__('a')
```

**Output:**
```
Getting value for a
1
```

### Summary
- `__setitem__(self, key, value)`: Defines how an object handles the assignment to a key/index.
- `__getitem__(self, key)`: Defines how an object retrieves values for a key/index.

These methods are helpful for creating custom classes that behave like dictionaries, lists, or other data structures that support key-based access.