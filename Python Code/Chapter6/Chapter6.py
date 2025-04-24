class Robot:
    ingredient = "metal"  # class attribute

    def __init__(self, name, age):
        self.name = name  # 上面的name
        self.age = age  # 上面的age

    def walk(self):
        print(f"{self.name} is walking...")

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours ")

    def greet(self):
        print(
            f"Hi my name i {self.name}, and I am made of {self.__class__.ingredient}.")


my_robot_1 = Robot("Ray", 25)
my_robot_2 = Robot("Ken", 26)


my_robot_1.greet()
my_robot_2.greet()
