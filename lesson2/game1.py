import random
def main():
    number = int(random.randint(1,7))
    print(number)
     while True: 
        guess = int(input("введите число от 1 до 7:"))
        if guess == number :
            print('That right')
            print('Ok')
            return True
        elif guess < number :
            print('too small')
        else :
            print('too many')
    else :
        print('end of cycle')
    print('that is all')

main()
