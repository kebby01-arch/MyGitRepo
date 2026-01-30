k = 60
print(k)
print(id(k))

x = 30
print(x)
print(id(x))
y = x
print("y="+str(y))
print("id(y)="+str(id(y)))
result = x+y
print("result="+str(result))
print("id(result)="+str(id(result)))  
'''
Immutable object example
不可變物件範例
int str float tuple

Mutable object example
可變物件範例
list dict set

小常數池
Small Integer Cache
Python 在內部會對小整數（通常是 -5 到 256 之間的整數）進行緩存，這意味著在這個範圍內的整數會共用同一個記憶體位址。因此，當你創建多個相同值的小整數時，它們實際上指向的是同一個物件。
這就是為什麼在上面的範例中，變數 a、b、c 和 d 都指向相同的記憶體位址。

大整數
Large Integer Example

x = 10000
y = 10000   
print(id(x))
print(id(y))


'''



''' 註釋
var1 = None
var1 = "Hello!"
var1 = 20
var1 = 12.3
var2 = 30
var1 = var2
result = var1 + var2
result = var1 - var2
result = var1 * var2
result = var1 / var2
result = var1 % var2
'''