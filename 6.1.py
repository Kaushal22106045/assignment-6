num = int(input("Enter number: "))
a = [0, ]
for x in range (1,num):
    if num%x == 0:
        a.append(x)
if sum(a) == num or sum(a) == num/2:
    print ("You entered a perfect number")
else :
    print ("Entered number is NOT perfect")