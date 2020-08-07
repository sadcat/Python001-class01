- class
 - style
   - old (python < 3)
   - new (python >= 2.2)
 - access base class
   - ```super().field```
 - field
   - static: @staticmethod
   - class: @classmethod
     - 1st argument: cls
     - used for 'factory method'
   - instance
     - 1st argument: self
   - accessibility
     - protected: prefix with '_field'
     - private: prefix with '__field'
   - access to field associated with instance
     - use ```.```: ```instance.field```
   - delete field
     - ```del instance.field```
   - hook
     - ```__getattribute__```: hook for all fields.
     - ```__getattr__```: hook for non-existing fields.
     - execute seq: ```__getattribute__``` > ```__get_attr__``` > ```__dict__```
   - accessor
     - ```__get__```
     - ```__set__```
     - ```__delete__```
   - turn method into field
     ```
     @property
     def password(self)
       return None
     
     @password.setter
     def password(self, password)
       self.password_hash = hash(password)
     ```
   - diagnostic
     - ```__dict__```: list fields
     _ ```__class__```: return its class
     - ```__bases[0]```: return its first base class
     _ ```__subclasses()```: return its all derived classes
   - ```__new__```: class constructor
   - ```__init__```: class initialization method 
- design pattern
  - singleton
  - factory
  - mixin: multiple inheritance
    - method resolution order: object.mro()
      - BFS on graph
