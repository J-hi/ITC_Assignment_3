
class Individual():
    from datetime import date
    
    def __init__(self,name):
        self.birthday=None
        self.name=name
    
    def get_name(self):
        return self.name
    
    def add_birthday(self,year,month,day):
        self.birthday=date(year,month,day)
    
    def get_age(self):
        current=date.today()
        age=(current-self.birthday).days
        age=age//365
        return age
    
    def __str__(self):
        return str(self.name)


class AU_Employee(Individual):
    
    new_id=1
    
    def __init__(self,name):
        super().__init__(name)
        self.id_str='AU'        
        
    def get_unique_id(self):
        new_id_copy=AU_Employee.new_id
        id_o=1
        
        while new_id_copy>0:
            id_o+=1
            new_id_copy=new_id_copy//10
            
        self.id_=self.id_str+((4-id_o)*'0')+str(AU_Employee.new_id)
        AU_Employee.new_id+=1
        
        return self.id_


class Faculty(AU_Employee):
    
    def __init__(self,name):
        super().__init__(name)


class EN_Faculty(Faculty):
    
    def __init__(self,name,classroom_year):
        super().__init__(name)
        self.classroom_year=classroom_year
        self.id_str='AU_EN'
    
    def assign_batch(self):
        self.batch='EN_'+str(self.classroom_year)+'-'+str(self.classroom_year+1)
        return self.batch
    

class Design_Faculty(Faculty):
    
    def __init__(self,name,classroom_year):
        super().__init__(name)
        self.classroom_year=classroom_year
        self.id_str='AU_DN'
    
    def assign_batch(self):
        self.batch='DN_'+str(self.classroom_year)+'-'+str(self.classroom_year+1)
        return self.batch

class Roster():
    
    def __init__(self):
        self.faculty_courses=[]
        self.courses_assigned={}
    
    def add_faculty(self,faculty):
        try:
            if isinstance(faculty,Faculty):
                if faculty not in self.courses_assigned.keys():
                    self.courses_assigned[faculty]=self.faculty_courses
            else:
                raise Exception
        except:
            print(f'Invalid input type---->{faculty}')
            
                
        #return print(self.courses_assigned.keys())
    
    def add_course(self,faculty,course): 
        try:
            if faculty in self.courses_assigned.keys():
                self.courses_assigned[faculty].append(str(course))
            else:
                raise Exception
            
        except:
            print(f'Faculty not in Roster---->{faculty}')


    def get_courses(self,faculty):
        try:
            if faculty in self.courses_assigned.keys():
                print(self.courses_assigned[faculty])
            else:
                raise Exception
        except:
            print(f'Faculty not in Roster---->{faculty}')

        list_faculty=list(self.courses_assigned.keys())
        list_faculty.sort()
        return print(list_faculty)
