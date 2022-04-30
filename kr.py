import random

brands_of_phone = {
"Iphone":{"battery":90, "strength":50},
"Samsung":{"battery":90, "strength":60},
"Huawei":{"battery":70, "strength":70},
"Xiaomi":{"battery":80, "strength":100},
}

school_list = {
"Школа №18":{"education":50},
"Католицький ліцей":{"education":40},
"Школа №23":{"education":45},
"Гімназія №1":{"education":70},
}

class Human:
    def __init__(self, name = "Human", phone=None, school=None ):
        self.name = name
        self.money = 20
        self.gladness = 30
        self.progress = 0
        self.alive = True
        self.phone = phone
        self.school = school

    def get_phone(self):
        self.phone = Phone(brands_of_phone)

    def get_school(self):
        self.school = School(school_list)

    def to_study(self):
        print("Пішов вчитись")
        self.gladness -= 4
        self.progress += 2
        self.money += 5

    def to_walk(self):
        self.gladness += 2
        self.money -= 1

    def to_do_homework(self):
        self.gladness -= 1
        self.progress += 2

    def to_play(self):
        self.gladness += 3
        self.progress -= 2
        rand = random.randint(1, 2)
        if rand == 1:
            print("Закинув гроші в стім")
            self.money -= 3
        elif rand == 2:
            print("Сьогодні не закидав гроші в стім")

    def days_indexes(self, day):
        print(f"День {day} гравця {self.name}")
        print(f"Гроші = {self.money} Щастя = {self.gladness} ")
        print(f"Прогрем у навчані = {self.progress}")
        print(f"Рівень заряду телефона {self.phone.battery}")

    def is_alive(self):
        if self.progress < -10:
            self.alive = False
            print("Кікнули з шараги")


        elif self.gladness <= 0:
            self.alive = False
            print("Лівнув зі школи, бо школа фуфло")


        elif self.progress >= 50:
            self.alive = False
            print("ЗНО на 200")


    def live(self, day):
        if self.is_alive() == False:
            return False

        if self.school is None:
            self.get_school()
            print(f"Поступаємо {self.school}")

        if self.phone is None:
            self.get_phone()
            print(f"Я получив телефон {self.phone}")
        self.days_indexes(day)
        rand = random.randint(1, 4)
        if rand == 1:
            print("Йду в школу")
            self.to_study()
        elif rand == 2:
            print("Йде гуляти")
            self.to_walk()
        elif rand == 3:
            print("Йде робити домашку")
            self.to_do_homework()
        elif rand == 4:
            print("Йде грати")
            self.to_play()


        self.is_alive()


class Phone:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.battery = brand_list[self.brand]["battery"]
        self.strength = brand_list[self.brand]["strength"]


class School:
    def __init__(self, school_list):
        self.school = random.choice(list(school_list))
        self.education = school_list[self.school]["education"]


kaneki = Human(name="Kaneki")

for day in range(365):
    if kaneki.alive == False:
        print(kaneki.phone.brand )
        print(kaneki.school.school)
        break
    kaneki.live(day)






