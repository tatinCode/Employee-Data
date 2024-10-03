#
#
#   Encapsulates the employee's details and provides methods to set 
#   and get these details, ensuring that the data is managed in a controlled 
#   manner. The __str__ method is particularly useful for printing the employee’s 
#   information in a readable format.
#   
#   the parameters: name, id, department, job
#
class Employee:
    def __init__(self, name, id_num , dept, job):
        self.__name = name
        self.__id = id_num
        self.__dept = dept
        self.__job = job
        
    def set_name(self, name):
        self.__name = name
        
    def set_id(self, id):
        self.__id = id_num
        
    def set_dept(self, dept):
        self.__dept = dept
        
    def set_job(self, job):
        self.__job = job
    #_______________________________________________________________________________________________

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

    def get_dept(self):
        return self.__dept

    def get_job(self):
        return self.__job

    def __str__(self):
        return "%-*s %-*s %-*s %-s" %(13, self.__name, 9, self.__id,14 , self.__dept, self.__job)
