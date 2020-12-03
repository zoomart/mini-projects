#SeaBattle
import random
map = [

	["a1","b1","c1"],
	["a2","b2","c2"],
	["a3","b3","c3"]
	
	]

mapLevel = ""

for i in map:
	f = ""
	for j in i:
		f = f+j+" "
	mapLevel = mapLevel+f+"\n"
print(mapLevel)

hp = True
y = random.choice(map)
x = random.choice(y)
TryCount = -1
#print(str(x))

while hp == True:
	dam = input('Пожалуйста, выберите координату для нападения:\n>>> ')
	dam = dam.lower()
	if dam == x:
		print("Поздравляю, Вы победили!!!")
		hp = False
	elif TryCount == 3:
		print("Ты проиграл")
		hp = False
	else:
		print("К сожалению, вы промазали")
	TryCount = TryCount+1
input("Game over")

		
