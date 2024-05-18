# Import whole py module, use dog.xxx. Or use "from dog import Dog"
import dog
import electric_car

def use_string():
    first_name = "ada"
    last_name = "lovelace"
    full_name = f"{first_name} {last_name}"
    # f: Replace variable in {} in string. 
    message = f"Hello, {full_name.title()}!"
    print(message)


def use_list():
    # 引号可以是单、或双引号
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    # Appent list
    bicycles.append("hunter 2.0")
    message = f"My first bicycle was a {bicycles[0].title()} and last was {bicycles[-1].title()}."
    print(message)

    # Sort list
    bicycles.sort()
    print(f"Sorted list: {bicycles}, length: {len(bicycles)}")

    # Iterate list
    print("Iterate list: ")
    for bicycle in bicycles:
        print(f"- {bicycle}")

    # Range
    print ("Range: ")
    for value in range(1, 5):
        print(f"- {value}")

    # 切片
    print(f"切片: {bicycles[0:3]}")

    # 复制列表
    bicycles_new = bicycles[:]
    bicycles_new.append("hunter 3.0")
    print(f"复制列表: {bicycles_new[:]}")
    
    # 元组：不可变的列表
    dimensions = (200, 50)
    print(f"元组：{dimensions}")

def use_dictionary():
    alien_0 = {'color': 'green', 'points': 5}
    print(f"alien_0: color: {alien_0['color']}, 'points': {alien_0['points']}")
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

def use_if():
    cars = ['audi', 'bmw', 'volvo', 'byd']
    for car in cars:
        # Compare: and, or, in, not in, !=
        if car == 'volvo' or car == 'byd': 
            print(car.upper())
        elif car == 'bmw':
            print(car.lower())
        else:
            print(car.title())

def use_while():
    current_number = 1
    while current_number <= 5:
        print(current_number)
        current_number += 1

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

def use_func():
    author = get_formatted_name("zhong hua", "shu")
    print(f"formated: name: {author}")

def use_class():
    my_dog = dog.Dog("Little black", 6)
    print(f"My dog's name is: {my_dog.name}.")
    print(f"My dog' age is: {my_dog.age}.")
    my_dog.sit()
    my_dog.roll_over()

    my_tesla = electric_car.ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()

def use_file():
    filename = 'data/pi_digits.txt'
    temp_file = "data/temp_pi.txt"
    pi_string = ""
    
    # Open file
    print(f"Read file: {filename}")
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())        # Delete line end \n.
            pi_string += line.strip()   # Remove empty space.
    print(pi_string)

    # Write file
    print(f"Write file: {temp_file}")
    with open(temp_file, 'w') as file_object:
        file_object.write(pi_string)

def use_exception():
    try:
        print(5/0)
    except ZeroDivisionError:
        # 使用异常，避免程序奔溃
        print("You can't divide by zero!")
    else:
        # 没有异常，执行成功
        print("No error")
