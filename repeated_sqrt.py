from math import sqrt #import square root function
for n in range(1,60): #creates a loop for numbers 1-60
    r = 2.0 #sets the variable equal to r
    for i in range(60): #creates a loop taking the square root of r n number of times
        r = sqrt(r) #square root of r
    for i in range(60): #creates a new loop squaring r n number of times
        r = r**2 #squares r
    print('%d times sqrt and **2: %16f' % (n,r)) #prints all r and n values
#As n value gets larger and larger, the value that comes from the second for loop will get extremely small
#with several decimal points. At a certain point, the program cuts off the decimals and when the first r
#value gets squared the same number of time as the square root was taken, the new r value will not be quite as big
#as the original r value because decimals were rounded off.
