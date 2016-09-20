def age(): 
    while True: 
        age = input("What is your age? ")
        try:
            if int(age) >= 18 and len(age) > 0:
                print("Awesome! you can buy alcohol.")
                break
            elif int(age) > 0 and len(age) > 0:
                print("So you are " + age + " years old.")
                break
            else: 
                print("Age has to be above 0.")
        except ValueError:
            print("Your age cannot be empty and cannot contain letters.")
age() 
