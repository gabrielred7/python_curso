times = ('Athletico-PR', 'Sport', 'Atlético-MG', 'Grêmio', 'Internacional', 'Bragantino', 'Santos', 'Atlético-GO', 'Bahia', 'Botafogo', 'Corinthians', 'Goiás', 'Palmeiras', 'São Paulo', 'Vasco', 'Ceará', 'Flamengo', 'Fluminense', 'Coritiba', 'Fortaleza')
print("-="*30)
print(f"Esses são os times do brasileirão de 20-21: {times}")
print("-="*30)
libertadores = times[:4]
print(f'Por enquanto os times na fase de grupos da Libertadores são: {libertadores}')
print("-="*30)
sula = times[6:12]
print(f'Por enquanto os times na fase de grupos da Sul-Americana são: {sula}')
print("-="*30)
rebaixados = times[16:]
print(f'Os times que podem ser rebaixados são: {rebaixados}')
print("-="*30)
ordem = sorted(times)
print(f"Os times em ordem alfabetica fica {ordem}")
print("-="*30)
for c in range(0, len(times)):
    if times[c] == "Vasco":
        print(f"O Vasco está na {c}ª posição")