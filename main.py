from random import randint


class HomeAndPeople:

    def __init__(self):
        self.n = randint(5, 20)
        self.k = int()
        self.elevator = []
        self.people = []
        self.elevator_step = -1
        self.step = -1

    def set_k(self):
        self.k = randint(0, 10)  # количество человек на этаже

    def get_k(self):
        return self.k

    def home(self):  # заполняет дом людьми
        a = 0
        g = -1
        for i in range(self.n):
            h = 0
            a += 1
            g += 1
            self.people.append([])
            self.set_k()
            k = self.get_k()
            for b in range(k):
                b = randint(1, self.n)
                h += 1
                if a == b:
                    pass
                else:
                    self.people[g].append((h, a, b))
                    # h - порядковый номер человека на этаже, a - с какого он этажа, b - на какой этаж хочет ехать

    def step_up(self):  # лифт едет на следующий этаж
        self.elevator_step += 1
        if len(self.elevator) == 0:
            for i in range(5):
                if len(self.people[self.elevator_step]) > 0:
                    self.elevator.append(self.people[self.elevator_step][0])
                    print(f'{self.people[self.elevator_step][0]} come in elevator and want ride up')
                    self.people[self.elevator_step].pop(0)
        self.on_step()

    def step_down(self):  # лифт едет на предыдущий этаж
        self.elevator_step -= 1
        if len(self.elevator) == 0:
            for i in range(5):
                if len(self.people[self.elevator_step]) > 0:
                    self.elevator.append(self.people[self.elevator_step][0])
                    print(f'{self.people[self.elevator_step][0]} come in elevator and want ride down')
                    self.people[self.elevator_step].pop(0)
        self.on_step()

    def checking_up(self):  # проверяет может ли лифт поехать выше
        b = 0
        for i in self.elevator:
            if i[2] < self.elevator_step + 1:
                b += 1
        if b == 5:
            self.checking_down()
        else:
            self.step_up()

    def checking_down(self):  # проверяет может ли лифт поехать ниже
        b = 0
        for i in self.elevator:
            if i[2] > self.elevator_step + 1:
                b += 1
        if b > 0:
            self.checking_up()
        else:
            self.step_down()

    def on_step(self):  # на этаже проверяет куда хотят ехать пасажиры и берет их или высаживает
        print(f'STAGE {self.elevator_step + 1}')
        for i in self.elevator:
            if i[2] == self.elevator_step + 1:
                print(f'{i} out from elevator')
                self.elevator.remove(i)
            else:
                pass
        v = len(self.elevator)
        if v == 5:
            self.checking_up()
        b = 5 - v
        upper = []
        downer = []
        for i in self.people[self.elevator_step]:
            if i[2] > self.elevator_step + 1:
                upper.append(i)

        if len(upper) > 0:
            for i in range(b):
                self.elevator.append(upper[0])
                self.people[self.elevator_step].remove(upper[0])
                print(f'{upper[0]} come in elevator and want ride up')
                upper.pop(0)
                print(f'{v} in elevator')
                self.checking_up()

        else:
            for i in self.people[self.elevator_step]:
                if i[2] < self.elevator_step + 1:
                    downer.append(i)
            if len(downer) > 0:
                for i in range(b):
                    self.elevator.append(downer[0])
                    self.people[self.elevator_step].remove(downer[0])
                    print(f'{downer[0]} come in elevator and want ride down')
                    downer.pop(0)
                    print(f'{v} in elevator')
                    self.checking_down()

            else:
                if self.elevator_step == -1:
                    from sys import exit
                    exit('thats all')
                else:
                    self.checking_down()

    def work(self):
        self.home()
        self.step_up()


if __name__ == "__main__":
    go = HomeAndPeople()
    go.work()
