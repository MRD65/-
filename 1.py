import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 100

    def to_study(self):
        print("Студент пішов вчитися")
        self.progress += 0.12
        self.gladness -= 5
        self.money += 8.1

    def to_sleep(self):
        print("Студент спить")
        self.gladness += 3

    def to_chill(self):
        print("Студент відпочиває")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 8


    def is_alive(self):
        if self.progress < -0.5:
            print("Кікнули за погану успішність")
            self.alive = False

        elif self.gladness <= 0:
            self.alive = False
            print("Лівнув(")

        elif self.progress >5:
            print("Все успішно здав")
            self.alive = False

        elif self.money < 50:
            print("Кінкули за неоплату")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {round(self.money, 2)}")

    def live(self, day):
        print(f"Студент навчається{day} день")
        rand = random.randint(1, 3)
        if rand == 1:
            self.to_study()
        elif rand == 2:
            self.to_sleep()
        elif rand == 3:
            self.to_chill()


        self.end_of_day()
        self.is_alive()

student = Student("Роман")

for day in range(365):
    if student.alive == False:
        break
    student.live(day)






