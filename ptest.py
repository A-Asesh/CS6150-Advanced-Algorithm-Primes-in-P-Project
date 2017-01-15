#reference: Discussions on Stack Overflow and Geeks for Geeks

import time
inputnumber=input("Please type number for Primality Test")
if inputnumber == 2:
    print "It is Prime"
if inputnumber == 3:
    print "It is Prime"
if inputnumber % 2 == 0:
    print "It is not Prime"
if inputnumber % 3 == 0:
    print "It is not Prime"

i = 5
w = 2

while i * i <= inputnumber:
    if inputnumber % i == 0:
        print "It is not Prime"

    i += w
    w = 6 - w

print "It is Prime"

start_time = time.clock()
print time.clock() - start_time, "seconds"
