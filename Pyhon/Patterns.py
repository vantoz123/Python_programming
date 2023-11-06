# this program is for printing various patterns
#pattern 1 (a right angled triangle)
'''for a in range(10):
    print("*" * a)'''
# pattern 2 (a rectangle)
'''
for i in range(5):
        print("*" * 5)'''

# Another approach to print right angled triangle
'''def pyramid(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end= " ")

        print("")

n = 5
pyramid(n)'''

# drawing a triangle

'''def Triangle(n):
    k = 2 * n -2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k-=1
        for j in range(0, i+1):
            print("* ", end=" ")

        print("\r")
        
n = 15
Triangle(n)'''

'''def PrintNum(n):
    num = 1
    for i in range(0, n):
        #num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num+=1
        print('\r')

n = 5
PrintNum(n)'''

'''def ConsonantPrint(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
        num+=1

        print("\r")

n = 5
ConsonantPrint(n)'''

