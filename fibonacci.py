def fibonacci(n):
    a = 0
    b = 1
    count = 0
    if n > 0:
        while count < n:
            count += 1
            old_a = a
            a = b
            b += old_a
            print (old_a)
    elif n < 0:
        print "Value below zero"
    else:
        print "Error"
        return None
    
fibonacci(10)