import random
brands_of_car = {
"BMW":{"fuel":100, "strength":100,"consumption": 8},
"Lada":{"fuel":50, "strength":40,"consumption": 10},
"Volvo":{"fuel":70, "strength":150,"consumption": 8},
"Ferrari":{"fuel":80, "strength":120,"consumption": 14},
"Nissan GT-R":{"fuel":80, "strength":120,"consumption": 40},
"Бандерамобіль":{"fuel":100500, "strength":999999999,"consumption": 1000},
}
job_list = {
"Java developer":{"salary":50, "gladness_less": 10 },
"Python developer":{"salary":40, "gladness_less": 3 },
"C++ developer":{"salary":45, "gladness_less": 25 },
"Rust developer":{"salary":70, "gladness_less": 1 },
}

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 99
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.car.fuel += 20
                self.money -= 20
                return
            else:
                self.to_repair()
                return

        if manage == "fuel":
            print("Заправим машину")
            x = self.car.fuel_max - self.car.fuel
            self.money -= x
            self.car.fuel += x
        elif manage == "food":
            print("Купив їди")
            self.home.food += 50
            self.money -= 50
        elif manage == "delicacies":
            print("купили вкусняшки")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_house(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        print(f"День {day} гравця {self.name}")
        print(f"Гроші = {self.money} Щастя = {self.gladness} Ситість = {self.satiety}")
        print("Будинок")
        print(f"Рівень хаосу = {self.home.mess} К-сть їди = {self.home.food}")
        print("Бібіка")
        print(f"К-сть поїздок до ТО {self.car.strength} Рівень плаьного = {self.car.fuel}")

    def is_alive(self):
        if self.gladness < 0:
            print("депресія....... 1000-7?")
            return False
        if self.satiety < 0:
            print("PRESS F TO PAY RESPECT")
            return False
        if self.money < -500:
            print("Банкрот")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Заселяємось")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Отримуєм машину {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Я пішов працювати {self.job.job} і мій оклад = {self.job.salary}")
        self.days_indexes(day)
        rand = random.randint(1, 4)
        if self.satiety < 20:
            print("я хаваю борщ")
            self.eat()
        elif self.gladness < 20:
            if self.home > 15:
                print("Йду прибирати")
                self.clean_house()
            else:
                print("Чіл")
                self.chill()
        elif self.money < 0:
            print("йди працюй")
            self.work()
        elif self.car.strength < 15:
            print("Треба поремонтувати машину")
            self.to_repair()
        if rand == 1:
            print("Чіл")
            self.chill()
        elif rand == 2:
            print("йди працюй")
            self.work()
        elif rand == 3:
            print("Час прибирання")
            self.clean_house()
        elif rand == 4:
            print("Йду наїмся вкуснях")
            self.shopping(manage="delicacies")



class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
        self.fuel_max = brand_list[self.brand]["fuel"]

    def drive(self):
        if self.fuel >= self.consumption and self.strength > 0:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("This car can`t move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


nick = Human(name="Nick")

for day in range(1, 36000):
    if nick.live(day) == False:
        print(nick.car.brand)
        break


