
class Person:

    def __init__(self, name=None , surname=None, age=None):
        self._name = name
        self._surname = surname
        self._age = age

    # getting   
    @property
    def name(self): 
        return self._name 
          
    # setting    
    @name.setter 
    def name(self, name): 
        self._name = name.upper()
          
    # deleting
    @name.deleter 
    def name(self):
        del self._name
    
    @property
    def surname(self): 
        return self._surname
          
    # setting    
    @surname.setter 
    def surname(self, surname): 
        self._surname = surname.upper()
          
    # deleting
    @surname.deleter 
    def surname(self):
        del self._surname
    
    @property
    def age(self): 
        return self._age 
          
    # setting    
    @age.setter 
    def age(self, age): 
        self._age = age 
          
    # deleting
    @age.deleter 
    def age(self):
        del self._age    


 
 