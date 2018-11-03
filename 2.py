
# ques 1
n = int(input("how many elements in the list: "))
l = []
for i in range (0,n):
	l.append(int(input('enter list element: ')))
print (l)

# ques 2
l1= ['google','apple','facebook','microsoft','tesla']
l.extend(l1)
print(l)

#q3
l=[1,2,3,1,3,4,5]
print(l.count(3))

#q4
a=[]
l=[8,6,4,7,3,6]
l.sort()
print(l)

#q5
l1 = [1,2,3,4,5,6]
l2= [2,5,6,7,8,9]
l1.extend(l2)
l1.sort()
print(l1)

#q6
e=0
o=0
for x in l:
	if x%2==0:
		e+=1
	else:
		o+=1
print("total even no.: "+str(e))
print("total odd no.: "+str(o))

#q7 
t = (3,5,4,6,8)
print(t[::-1])

#q8
print(max(t))
print(min(t))

#q9
s='Vinny'
print(s.upper())

#q10
a=0
s='12345'
for x in s:
	if x.isnumeric:
		a+=1
	else:
		break
if a==len(s):
	print("true")
else:
	print('false')
	
#q11

s="Hello World"
l = s.split(' ')
l.remove("World")
l.append("Vinny")
print( l[0]+' '+l[1])