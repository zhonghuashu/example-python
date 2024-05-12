def use_string():
    first_name = "ada"
    last_name = "lovelace"
    full_name = f"{first_name} {last_name}"
    # f: Replace variable in {} in string. 
    message = f"Hello, {full_name.title()}!"
    print(message)


def use_list():
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

