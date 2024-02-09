'''
print("welcome");
print("This is my first prgrm");
x=30;
y=20;
z=15;
a=x+y;
b=x-y;
c=x*y;
d=x/y;
print("Added value is :",a);
print("Subtracted value is :",b);
print("Multiply value is :",c);
print("Divided value is :",d);
print("Incerment value is " , (x + 2));
print("Decerment value is " ,(x-2)); 

if x<y :
	print("Y is greater than X")
else :
	print("X is greater than Y")

if x<y :
	if y<z :
		print("y is greater than z")
	else :
		print("z is greater than y")
else :
	print("Not applicabl")

                                                                                                                                                
i="san"
print(i);
print(type(i));

x = ["sangari","jaya","kayal"] #list
print(x);
print(type(x));

x = ("sangari","jaya","kayal") #tuple
print(x);
print(type(x));

x = {"sangari","jaya","kayal"} #set
print(x);
print(type(x));

x = {("sangari","jaya","kayal")} #frozenset
print(x);
print(type(x));

x = {"sangari" : "good_girl", "education" : "BE"} #dictonary
print(x);
print(type(x));

a = ("cat","dog","cow") 
(x,y,z) = a 
print(x,y,z)
		
san="Hi sangari! You are a bold girl. You can do anything. Always be hope with your self"
print(san);
print(san.upper())
print(san.lower())

vj = " hi how ,   are you "
print(vj.strip())

roll_no = 35
<<<<<<< HEAD
text = " Sangari Roll no is : {}"
=======
text = " Sangari Roll no is :{} "
>>>>>>> 7ee6ffa56b5cf2de87281f0a4d432d527929a69e
print(text.format(roll_no))
'''

x = ["COW" , "CAT" , "DOG" , "GOAT" , "HUMAN"]
print(x)
print(type(x))
print(len(x))
for y in x :
	if y == "CAT":
		continue
	print(y);

x[3] = "TIGER"
print(x)




