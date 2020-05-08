class Soldier:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    
    def __str__(self):
        return f'Солдат {self.name} {self.lastname}'
    

class Guns:
    def __init__(self):
        self.bullets = 40

    def bullets_left(self):
        print(f'осталось патронов {self.bullets}')

    def AK47(self):
        print('Стреляю на поражения')
        if self.bullets > 0:
            tshhh = 0
            for x in range(self.bullets):
                tshhh += 1
                self.bullets -= 1
            print("tigi-tigitishh" * tshhh)
        else:
            print(f'Нет патронов!')
            self.bullets_left()

    def reload(self):
        self.bullets += 30
        print('Перезаредка прошла успешно. Можно стрелять!')

class Act_of_shooting(Soldier, Guns):
    def __init__(self, name, lastname):
        Soldier.__init__(self, name, lastname)
        Guns.__init__(self)




Soldier = Act_of_shooting('Rayan', 'Rich')




