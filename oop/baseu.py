# class Student(object):
#    def __init__(self, name,score):
#        self.name = name
#        self.score = score

#    def print_score(self):
#        print('%s:%s' % (self.name,self.score))




class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
         if gender == 'male' or gender == 'female':
             self.__gender=gender

bart = Student('Bart Simpson',59)
bart.print_score()