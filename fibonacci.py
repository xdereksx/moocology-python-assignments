def fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        count += 1
        old_a = a
        old_b = b
        a = old_b
        b = old_a + old_b
        print (old_a)
    
fibonacci(30)