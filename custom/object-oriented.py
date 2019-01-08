class Student:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self._score = score

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def __repr__(self):
        return 'name is :' + self.__name + '    age is :' + str(self.__age)


if __name__ == '__main__':
    student = Student('zhangjun', 25, 99)
    print(student)
    print(student.get_name())
    print(student._score)
    print(student._Student__name)
