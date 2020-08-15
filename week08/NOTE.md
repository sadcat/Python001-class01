### Variable and Data types

- Everything is object, class is object as well.
- Data types
  - mutable/immutable: whether the object can be changed once it's created
  - immutable: int, float, str, tuple, ...
  - mutable: list, dict, set
  - sequence:
    - container: where it's able to contain multiple types. list, tuple, ..
    - other: where only contains just one type: str, bytes, array.array, ..
- Different variables that points to the same value have same object id.
  ```
  a = 123
  b = 123
  assert id(a) == id(b)
  c = 'hello'
  d = 'hello'
  assert id(c) == id(d)
  ```
- clone
  - copy.copy(object)
  - copy.deepcopy(object)

### Function

- Callable object
- Variable scope
  - LEGB: Local Enclosing Global Built-in
- Argument
  - required
  - default
  - variant
  - named
  - named keyword
- lambda expression
  - simple function can be written as a lambda expression
  - func = lambda (arg1,arg2): arg1 + arg2
  ```
  def func(arg1, arg2)
    return arg1 + arg2
  ```
- variadic function
  ```
  def func(*arg, **kargs)
    pass
  ```
  - kargs: keyword arguments
  - args: other arguments

- return
  - return
  - yield

### Partial function

- allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited edition.
```
from functools import partial
def multiply(x, y):
  return x * y
dbl = partial(multiply, 2)
# dbl = lambda y: 2*y
r = dbl(4)
# r = 8
```

### Higher order function

- Any function is called higher order function where any one of arguments is function
- module: functools
- map
- reduce
- filter


### Closure

- A closure is a function object that remembers values in enclosing scopes even if they are not present in memory
  ```python
  def line_conf():   # 
    b = 10           # enclosing scope starts, b is a enclosing/free var.
    def line(x):     #
      return 2*x+b   #
    return line      # enclosing scope ends, return a function object

  my_line = line_conf()
  ```
    - ```my_line.__code__.co_varnames```: show local vars
    - ```my_line.__code__.co_freevars```: show free vars


### Decorator

- A decorator is a function tht takes another function and extends the behavior of the latter function without explicitly modifying it
```python
# A full example
from functools import wraps

# Defines a decorator called 'enhancer', it has one argument called 'parameter'
def enhancer(parameter):
  def outer(func):
    @wraps(func)            # Keep 'func' as is
    def inner(*args, **kwargs):
      print('do whatever that enhances func')
      print(f'with {parameter}')
      ret = func(*args, **kwargs)
      print('do more')
      return ret
    return inner
  return outer

@enhancer('good')
def fancy_func(a, b, c):
  print(f'{a} {b} {c}')
```

### Object protocol & Duck typing

- protocol = interface
- If n object of type A that can do the same as type B is also an object of type B
- dynamic typing
- magic function


### iterable & iterator 

- iterable: __getitem__() or __iter__()
- iterator: next() and __iter__()

### yield

- a function returns an object
- a function yields an generator

### Coroutine

- For I/O bound application
- async / await syntax
