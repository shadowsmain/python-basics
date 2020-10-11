class Student:
    def __init__(self):
        self.college = 'KPK'
        self.name = None
        self.surname = None
        self.patronymic = none
        self.age = None
        self.group = Unknown
        self.tnumber = 0
        self.adress = 0
        self.courator = 0

pupil_1 = Student()
pupil_1.name = 'Владислав'
pupil_1.surname = 'Теплов'
pupil_1.age = '54'
pupil_1.group = '33'

pupil_2 = Student()
pupil_2.name = 'Дмитрий'
pupil_2.age = '19'
pupil_2.group = '33'


class Teacher:
    def __init__(self):
        self.name = 0
        self.group = 'all group', '33', '43'
user_1 = Teacher()
user_1.name = 'Ревняков Е.Н.'
user_1.group = '33'

class Study_group:
    def __init__(self):
        self.number =  None
        self.curator = None

group_33 = Study_group()
group_33.courator = 'Кныш.Е.Г.'
group_43 = Study_group()
group_43.courator = 'Иванов.И.И'


class College:
    def __init__(self):
        self.name = 0
KPK = College()
KPK.name = 'Курганский Педагогический Колледж'
KGK = College()
KGK.name = 'Курганский Государственный Колледж'


class Exam:
    def __init__(self):
        self.datetime = None
        self.Teacher = None
        self.name = None

Subject_1 = Exam()
Subject_1.datetime = '18.04.2021, 14:00'
Subject_1.Teacher = 'Ревняков Е.Н.'
Subject_1.name = 'МДК 09.01 Проект и разработка web прил.'




class Student_on_exam:
    def __init__(self):
        self.mark = None
        self.subject = None
ex_1 = Student_on_exam()
ex_1.subject = 'MDK0801'
ex_1.mark = '5'




class Car:
    def __init__(self):
        self.country = None
        self.color = None
        self.mark = None

MarkII = Car()
self.color = 'White'
self.mark = 'Toyota'
self.country = 'Japan'

SupraV = Car()
self.color = 'Gray'
self.mark = 'Toyota'
self.Country = 'Japan'