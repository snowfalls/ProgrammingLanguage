

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # 方法的本质就是函数，是定义在类内的函数
    def run(self, speed):
        print("%s的%s正在以%s千米每小时的速度行驶" % (self.color, self.brand, speed))


car = Car('宝马', '白色')
car.run(100)
