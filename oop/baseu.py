#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student(object):
#    def __init__(self, name,score):
#        self.name = name
#        self.score = score

import pprint as pp





class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
         if gender == 'male' or gender == 'female':
             self.__gender=gender

# class Animal(object):
#     def run(self):
#         print('Animal is running...')

# class Dog(Animal):
#      def run(self):
#          print('Dog is running....')
#      def eat(self):
#          print('Eating meat....')

# class Cat(Animal):
#     pass

# dog =Dog()
# dog.run()


#继承   鸭子模型
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):

    def run(self):
        print('Cat is running...')
class people():
    def run(self):
        print("people do not extends Animal")
def run_twice(x):
    x.run()
    x.run()

run_twice(Cat())
run_twice(Animal())
run_twice(people())



# 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')