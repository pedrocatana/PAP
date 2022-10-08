import webbrowser as wb
import random as rd

print('-------------------------')
print('|      WWWWWWWWWWW       |')
print('-------------------------')

def randomica():
	ran = rd.randint(1, 5) 
	if ran == 1:
		wb.open('https://valdorio.net/a-escola/val-do-rio-oeiras/avisos')
	elif ran == 2:
		wb.open('https://github.com/pedrocatana')
	elif ran == 3:
		wb.open('https://www.discord.com/')
	elif ran == 4:
		wb.open('https://www.youtube.com/channel/UC2LT0au7E1fmPIVTCCKSW9Q')
	elif ran == 5:
		wb.open('https://www.twitch.tv/ocatana')
		
def main():
	while True:	
		print('ValdoRio Horários[1], Github[2], Discord: Catana#7975[3], Youtube[4], Twitch[5], Sair [6].')
		x = int(input('>>>'))
		#Condições:
		if x == 1:
			wb.open('https://valdorio.net/a-escola/val-do-rio-oeiras/avisos')
		elif x == 2:
			wb.open('https://github.com/pedrocatana')
		elif x == 3:
			wb.open('https://www.discord.com/')
		elif x == 4:
			wb.open('https://www.youtube.com/channel/UC2LT0au7E1fmPIVTCCKSW9Q')
		elif x == 5:
			wb.open('https://www.twitch.tv/ocatana')
		elif x == 6:
			input('Aperte "Enter" para sair.')
			break
		else:
			print('Opção não aceita, por favor digite uma opção válida.')
		print()		
main()

