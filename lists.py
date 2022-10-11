fruits = ["Apple", "Kiwi", "Grapes", "Oranges", "Pineapples"]
print("2nd fruit in my basket is ",fruits[1])
fruits[2] =" Muskmelon"
print("total fruits", len(fruits))
print(fruits)

for i,fruit in enumerate(fruits):
    print(i+1,")",fruit)
fruits.append("Grapes")
print("After append", fruits)
fruits.insert(2,"guava")
print("After insert", fruits)
fruits.reverse()
print("reverse",fruits)
seasonal_fruits = ["Mango", "Dragon Fruit"]
fruits.extend(seasonal_fruits)
print("after extend", fruits)
print(fruits.pop())
print("after pop", fruits)
fruits.remove("Grapes")
print("after remove", fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
print("first 2 fruits", fruits[:2])
print("fruits in between 3,5", fruits[3:5])
num_list = [1,2,3,"4",4,5,3,4,2]
print(num_list.count(4))
if 10 not in num_list:
    print("success")
