пользователь = {
	'энштейн': {
	'имя': 'альберт',
	'фамилия': 'энштейн',
	'место жительства': 'прингстон',
	},
	'мкюри': {
	'имя': 'мария',
	'фамилия': 'кюри',
	'место жительства': 'париж',
	},
}
for имя_пользователя, пользовательская_информация in пользователь.items():
	print(f"Имя_пользователя: {имя_пользователя}")
	полное_имя = f"{пользовательская_информация['имя']} {пользовательская_информация['фамилия']}"
	место_жительства = пользовательская_информация['место жительства']
	print(f"Полное имя: {полное_имя.title()}")
	print(f"\tМесто жительства: {место_жительства.title()}")
