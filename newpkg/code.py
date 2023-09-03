class Package(object):
    
     # successive classes override these in their init
     def __init__(self): #,instance="Instance Name"):
         self._id = id(self)
         self._name="Package"
         self._desc="Package for test pypi build"
         self._vers="v0.01.01" 
         self._model = "" # more for derived classes
         self._about="About package class"
         self._instance_name = ""
         self._debug_flag = False
       
     def whoami(self):
          print(self._name,self._vers,self._model)
     def name(self):
          print(self._name)
     def vers(self):
          return self._vers
       