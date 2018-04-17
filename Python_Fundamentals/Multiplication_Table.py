#Multiplication Table 

def make_table(num):
    print "x 1 2 3 4 5 6 7 8 9 10 11 12",
    for i in range(1,num+1):
        print "\n", i,
        for j in range(1,num+1):
            print i*j,

make_table(15)