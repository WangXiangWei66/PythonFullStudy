# coding:utf-8
x=20  # 直接赋值，直接将20赋值给左侧的变量x
y=10
x=x+y #将x+y的和赋值给x,x的值为30
print(x)
x+=y
print(x) # 40
x-=y  #相当于x=x-y
print(x) #30
x*=y  # x=x*y
print(x)  #300
x/=y  # x=x/y
print(x)  # 30.0
x%=2   #x=x%2
print(x) #0.0
z=3
y//=z  # y=y//z  ：向下取整法，也叫做地板除
print(y)  #3

y**=2  # y=y**2
print(y)

#Python支持链式赋值
a=b=c=100   #相当于 执行了a=100   b=100  c=100
print(a,b,c)

#Python支持系列解包赋值
a,b=10,20  # 相当于执行了  a=10   b=20
print(a,b)

print('-----------如何交换两个变量的值----------------')
#temp=0
#temp=a  #将a的值班赋值给temp, temp的值为10
#a=b    # 将b的值赋值给a ,a的值为20
#b=temp   #将temp的值赋值给b, b的值是10
#print(a,b)
b,a=a,b   # 将a的值赋给了b,将b的值赋给了a
print(a,b)



