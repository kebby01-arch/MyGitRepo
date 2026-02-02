
def BMI(para1, para2=75)->float:
    height = para1 / 100
    weight = para2         
    bmi = weight / (height * height)
    return bmi

height = float(input("請輸入身高(公分) => "))
weight = float(input("請輸入體重(公斤) => "))
bmi = BMI(height,weight)

if bmi < 18.5:
    print(f"您的BMI值為 {bmi:.1f}，屬於過輕")
elif bmi < 24:
    print(f"您的BMI值為 {bmi:.1f}，屬於正常")
elif bmi < 27:
    print(f"您的BMI值為 {bmi:.1f}，屬於過重")
else:
    print(f"您的BMI值為 {bmi:.1f}，屬於肥胖")






'''
if var1 >= 10:
    print("condition is true")


if var1 >= 10:
    print("condition is true")
else:
    print("condition is false")


if var1 >= 20:
    print("this condition is true")
elif var1 >= 10:
    print("this condition is true")
else:
    print("conditions are false")


for i in range(1, 11):
    print("i = " + str(i))

i = 1
while i <= 10:
    print("i = " + str(i))
    i = i + 1

if i > 5:
    break

if i % 2 == 0:
    continue
'''