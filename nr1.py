kasa=0
zestaw=0
pnazwa='idk'
prywal='idk'
print ('SUPERGRA Super-Alpha1')
print('----------------------------------------------------')
print("Cześć, witaj w SUPERGRZE!, jak nasz na imię?")
name=input("Podaj swoje imię: ")
while pnazwa=='idk':
	pnazwa=input('Potwierdzasz nazwę postaci? tak=t nie=n: ')
	while pnazwa=='n':
		print('W porządku! Zatem wybierz nową nazwę.')
		name=input("Podaj swoje imię: ")
		pnazwa=input('Potwierdzasz nazwę postaci? tak=t nie=n: ')
print("Witaj, ", end='')
print(name)
print('SUPERGRA to tak naprawdę nudna gra o walce. Przed rozpoczęciem gry musisz nazwać swojego rywala.')
rywal=input("Podaj imię swojego rywala: ")
while prywal=='idk':
	prywal=input('Potwierdzasz nazwę rywala? tak=t nie=n: ')
	while prywal=='n':
		print('W porządku! Zatem wybierz nową nazwę.')
		name=input("Podaj imię swojego rywala: ")
		prywal=input('Potwierdzasz nazwę rywala? tak=t nie=n: ')
print('Za chwilę rozpoczniesz walkę z ', end='')
print(rywal, " na poziomie pierwszym, nie będzie on trudny, ale aktualnie masz maksymalnie 10 HP i podstawowy miecz. Powodzenia!")
input("\n\nAby aby rozpocząć poziom 1, naciśnij klawisz Enter.")
lvl=1
if name=='czity':
	lvl=2
while lvl==1:
	hp=10
	rhp=10
	print('ty zaczynasz! twoje życie: 10 życie rywala: 10')
	atak=int(input('aktualnie możesz użyć tylko patyka który zadaje od 1 do 2 obrażeń- napisz 1| Twój wybór: '))
	if atak==1:
		import random
		rhp=rhp-random.randint(1, 2)
		print(rywal, "ma teraz", rhp, "HP!")
		while hp>0 and rhp>0:
			print('Kolej rywala!')
			hp=hp-random.randint(1,2)
			if hp<=0:
				print('Nie żyjesz!')
			else:
				print('masz teraz', hp , 'HP!')
				print('Twoja kolej!')
				atak=int(input('patyk(1)| Twój wybór: '))
				if atak==1:
					rhp=rhp-random.randint(1, 2)
					print(rywal, "ma teraz", rhp, "HP!")
		if hp>rhp:
			lvl=2
			print('Awansujesz do poziomu 2!')
			kasa=random.randint(4, 5)
			print('wygrywasz', kasa, 'monet!')
		else:
			input("\n\nAby zresetować poziom, naciśnij klawisz Enter.")
while lvl==2:
	print("możesz wstrzynać się z rozpoczęciem poziomu drugiego i zajrzeć do sklepu!")
	openmenu=1
	while openmenu==1:
		menu=int(input("1-Sklep 2-Rozpocznij drugi poziom| Twój wybór:"))
		if menu==1:
			print('1-Zestaw startowy(1 moneta) 2-Miksura +2 HP (2 monety) 3- wróć | Pieniądze: ', end='')
			opcja=input(kasa)
			if opcja==1:
				if kasa<=1 or zestaw==1:
					print('Nie możesz tego kupic!')
				else:
					kasa=kasa-1
					print('otrzymałeś zwykły miecz (2-3 obrażenia i +2 HP!) ')
					zestaw=1
					