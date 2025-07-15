add = lambda x,y: x+y
print(add(5,3))

square = lambda x:x**2
print (square(4))

numbers = [1,2,3,4,5,6]
even_number = list(filter(lambda x:x%2 == 0,numbers))
print(even_number)

multiply = lambda  x,y,z:x*y*z
print(multiply(2,3,4))

data = [(1,'apple'),(3,'banana'),(2,'cherry')]
stored_data=sorted(data,key=lambda x:x[1])
print(stored_data)

numbers = [1,2,3,4,5]
doubled= list[map(lambda x:x*2,numbers)]
print(doubled)

numbers=[10,15,20,25,30]
odd=list[filter(lambda x:x%2!0,numbers)]
print(odd)

operation={
    'add':lambda x,y:x+y,
    'sub':lambda x,y:x-y,
    'mul':lambda x,y:x*y,
    'div':lambda x,y:x/y,


}