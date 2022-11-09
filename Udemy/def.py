def say_something2():
	s = "hi"
	return s

result = say_something2()
print(result)

def what_is_this(color):
	if color == "red":
		print("tomato")
	else:
		print("I don't know")


what_is_this("red")

def add_num(a:int, b:int) -> int:
	return a + b

r = add_num(3,2)
print(r)

def menu(entree,drink):
	print(f"メインのお肉は{entree}で、ドリンクは{drink}で")

menu("beef","water")
