
num = int(input())
dup = num
sum = 0

if(num>=100 and num<=999):
    for i in range((len(str(num)))) :
        cub = dup%10
        sum += cub**3
        dup = dup//10
    if num == sum:
        print(str(num)+" is a Armstrong number")
    else:
        print(str(num) + " is not a Armstrong number")
else:
    print("Invalid input")



