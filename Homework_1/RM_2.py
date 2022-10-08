import random
 
rand_list=random.choices(range(10), k=5)
#rand_list = [3,0,1,1,9,7]
print(rand_list)

a = int(input("Введите а: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

counter = 0

for i in range(len(rand_list)):
    for j in range(i+1, len(rand_list)):
        for k in range(j+1, len(rand_list)):
            if abs(rand_list[i]-rand_list[j]) <= a:
                if abs(rand_list[j]-rand_list[k]) <= b:
                    if abs(rand_list[i]-rand_list[k]) <= c:
                        counter+=1 
print(counter)


