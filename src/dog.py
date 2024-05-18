class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """
        构造函数
        self必须是第一个, self前缀的变量可以供所有方法使用
        """
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name} is now sitting')
    
    def roll_over(self):
        print(f'{self.name} rolled over')