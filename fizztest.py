
n = (int(raw_input("enter a number:")))

def is_fizz(n):
    if n % 3 == 0 and n % 5 == 0:
        print "FizzBuzz"
    elif n % 3 == 0:
        print "Fizz"
    elif n % 5 == 0:
        print "Buzz"
    else:
        print "N is not devisible neither by 3 nor by 5"
        
is_fizz(n)