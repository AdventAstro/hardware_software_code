globalVar = 42

def my_address (str, var):
    print("{1} address:{0}/n{1} value: {2}".format(id(var) , str,var))

def ask_me(*num): #Ask the user for a number
    if num[0] == 1:
        ans = int(input("Please provide a number:"))
        return answer
    elif num[0] == 2:
        print("What do you think you will get.")
        print("When you add globalVar + num1?")
        input("globalVar = {} and num = {} ".format(num[1], num[-1]))
    else:
        print("globalVar = {} and num = {}".format(num[1], num[-1]))

    def add(num1):
        globalVar = num1
        my_address('add globalVar', globalVar)
        globalVar = globalVar + num1
        print('In add function globalVar + num1 = {}'.format(globalVar))

    def global_add(num1):
        global globalVar
        my_address('globalVar address', globalVar)
        globalVar = globalVar + num1
        print('In global_add globalVar + num1 = {}'.format(globalVar

    def main():
        my_address('main globalVar', globalVar)
        num1 = ask_me(1)
        my_address('main num1', num1)
        ask_me(2,globalVar, num1)
        sum = add(num1)
        ask_me(3,globalVar, sum)
        input("Why is that?")
        print("Now let's look at global_add")
        sum = global_add(num1)
        ask_me(3,globalVar, sum)

        __name__ == "__main__":
         main()

    def clear_screen():
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def main():
        clear_screen()
        my_address('1. main globalVar', globalVar)
        num1 = ask_me(1)
        my_address('2. main num1', num1)
        ask_me(3,globalVar, sum, 'sum')
        input("Why is that?")
        print("Now let's look at global_add")
        sum = global_add(num1)
        my_address('7. main sum', sum)
        ask_me(3,globalVar, sum, 'sum'
        my_address('8. main globalVar', globalVar)
        my_address('9. main num1', num1)

    if __name__ == "__main__":
        main()
