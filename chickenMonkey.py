num_1_to_100 = range(1,101)

for i in num_1_to_100:
    if i%5 == 0 | i%7 == 0:
        print(i, "ChickenMonkey")
    elif i%7 == 0:
        print(i, "Monkey")
    elif i%5 == 0:
        print(i, "Chicken")
    else :
        print(i)
    
