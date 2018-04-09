#Test Collatz Conjecture against number

def Collatz(num):
    x = 0
    while(x != 2):
        x = num
        if (num % 2) == 0 and num > 0:
            num = (num / 2)
            print num
        elif (num % 2) != 0 and num > 0:
            num = (num*3)+1
            print num
        else:
            print("You can test only positive integers!")
            break    
                    
Collatz(int(raw_input("Enter number to check: ")))
print
