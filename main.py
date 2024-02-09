from typing import *

class Student:
    list_all_student = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.list_all_student.append(self)

    def rate_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in (lecture.courses_attached and self.courses_in_progress):
            if lecture.grade_of_lessons.get(course):
                lecture.grade_of_lessons[course] += [grade]
            else:
                lecture.grade_of_lessons[course] = [grade]
        else:
            print('Ошибка')

    def avg_grades(self):
        if len(self.grades):
            count = 0
            for val in self.grades.values():
                count += sum(val)/len(val)
            return round(count/len(self.grades),2)
        else:
            return "У данного ученика пока нет оценок за домашние задания."

    def __eq__(self, other):
        try:
            return self.avg_grades() == other.avg_grades()
        except TypeError:
            return 'Кто-то из них еще выполнил ни одного задания.'

    def __lt__(self, other):
        try:
            return self.avg_grades() < other.avg_grades()
        except TypeError:
            return 'Кто-то из них еще выполнил ни одного задания.'

    def __gt__(self, other):
        try:
            return self.avg_grades() > other.avg_grades()
        except TypeError:
            return 'Кто-то из них еще выполнил ни одного задания.'

    def __le__(self, other):
        try:
            return self.avg_grades() <= other.avg_grades()
        except TypeError:
            return 'Кто-то из них еще выполнил ни одного задания.'

    def __ge__(self, other):
        try:
            return self.avg_grades() >= other.avg_grades()
        except TypeError:
            return 'Кто-то из них еще выполнил ни одного задания.'

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.avg_grades()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress) if len(self.courses_in_progress) else 0}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses) if len(self.finished_courses) else 0}"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecture(Mentor):
    list_all_lector = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_of_lessons = {}
        Lecture.list_all_lector.append(self)

    def avg_grades(self):
        if len(self.grade_of_lessons):
            count = 0
            for val in self.grade_of_lessons.values():
                count += sum(val)/len(val)
            return round(count/len(self.grade_of_lessons),2)
        else:
            return "У данного лектора пока нет оценок от учеников."

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.avg_grades()}"

    def __gt__(self, other):
        try:
            return self.avg_grades() > other.avg_grades()
        except TypeError:
            return 'Видимо у кого-то из них нет оценок от учеников'

    def __lt__(self, other):
        try:
            return self.avg_grades() < other.avg_grades()
        except TypeError:
            return 'Видимо у кого-то из них нет оценок от учеников'

    def __ge__(self, other):
        try:
            return self.avg_grades() >= other.avg_grades()
        except TypeError:
            return 'Видимо у кого-то из них нет оценок от учеников'

    def __le__(self, other):
        try:
            return self.avg_grades() <= other.avg_grades()
        except TypeError:
            return 'Видимо у кого-то из них нет оценок от учеников'

    def __eq__(self, other):
        try:
            return self.avg_grades() == other.avg_grades()
        except TypeError:
            return 'Видимо у кого-то из них нет оценок от учеников'

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in (self.courses_attached and student.courses_in_progress):
            if student.grades.get(course):
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"



if __name__== '__main__':

    '''Функция подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса '''
    def avg_hw_student(lst_students: List, name_course: str) -> float:
        grades_student = []
        for student in lst_students:
            if name_course in student.courses_in_progress:
                grades_student.extend(student.grades[name_course])
        return sum(grades_student)/len(grades_student)


    '''Функция подсчета средней оценки за лекции всех лекторов в рамках курса'''
    def avg_grades_lector(lst_lectors: List, name_course: str) -> float:
        grades_lectors = []
        for lector in lst_lectors:
            if name_course in lector.courses_attached:
                grades_lectors.extend(lector.grade_of_lessons[name_course])
        return sum(grades_lectors)/len(grades_lectors)

    student_id1 = Student('Иван', 'Иванов', 'мужчина')
    student_id2 = Student('Александра', 'Александрова', 'девушка')
    student_id1.courses_in_progress = ['Python', 'SQL']
    student_id2.courses_in_progress = ['Python', 'Аналитика']

    lector_id1 = Lecture('Олег', 'Тинькоф')
    lector_id2 = Lecture('Анна', 'Михайлова')
    lector_id1.courses_attached = ['Python', 'Back-End', 'SQL']
    lector_id2.courses_attached = ['HTML', 'CSS', 'Java-Script']

    review_id1 = Reviewer('Денис', 'Бузин')
    review_id2 = Reviewer('Виктория', 'Покладова')
    review_id1.courses_attached = ['Python', 'Back-End', 'SQL']
    review_id2.courses_attached = ['HTML', 'CSS', 'Java-Script']

    student_id2.rate_lecture(lector_id1, 'Python', 9)
    student_id1.rate_lecture(lector_id1, 'Python', 7.5)
    student_id1.rate_lecture(lector_id1, 'SQL', 5)

    review_id2.rate_hw(student_id1, 'Python', 5)
    review_id1.rate_hw(student_id2, 'Python', 10)

    print(student_id1.grades)
    print(student_id2.grades)
    print(lector_id1 > lector_id2)
    print(lector_id1.grade_of_lessons)
    print(lector_id1)
    print(lector_id2.avg_grades())
    print(avg_hw_student(Student.list_all_student, 'Python'))
    print(avg_grades_lector(Lecture.list_all_lector, 'Python'))
