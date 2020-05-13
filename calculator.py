#calculator

while True:
	a = input("первое число")
	b = input("второе число")
	c = input("действие(+,-,*,/)")
	s = ""
	if c == '+':
		s = int(a)+int(b)
		print(str(s))
		input()
	elif c == '-':
		s = int(a)-int(b)
		print(str(s))
		input()
	elif c == '*':
		s = int(a)*int(b)
		print(str(s))
		input()
	elif c == '/':
		s = int(a)/int(b)
		print(str(s))
		input()



