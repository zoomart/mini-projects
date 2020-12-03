#epic
import requests, time
while True:
	r = requests.get('https://www.epicgames.com/store/ru/')
	print(r)
	time.sleep(10)
	if r.status_code == 200:
		print("Епик готов раздавать халяву")
		break 
input()