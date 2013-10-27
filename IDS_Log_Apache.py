import re
import os

arquivo = open("access.log")
texto = arquivo.read()
'''
Lê do arquivo de log do apache, o IP, a data (dia, mes e ano) e a hora (hora, minutos e segundos). 
'''
ip_data_hora = re.findall(r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) - - \[([0-9]{2})/([a-zA-Z]{3})/([0-9]{4}):([0-9]{2}):([0-9]{2}):([0-9]{2})',texto)
ips_encontrados = []
qtde_vezes_ip = []
primeiro_acesso = []

for i in ip_data_hora:
	# Elimina as linhas escritas pelo próprio servidor dentro do arquivo de log.
	if (i[0] != "127.0.0.1"):
		# Verifica se o IP na linha do arquivo já foi lido e está armazenado no vetor dos IP's encontrados
		if (ips_encontrados.__contains__(i[0])):
			indice = ips_encontrados.index(i[0])
			'''
			Só sera incrementado a quantidade de vezes que o IP foi encontrado se o novo acesso tiver acontecido na mesma data, 
			hora e minuto realizado no primeiro acesso.
			'''
			if (i[1]==primeiro_acesso[indice][0] and i[2]==primeiro_acesso[indice][1] and i[3]==primeiro_acesso[indice][2] 
				and i[4]==primeiro_acesso[indice][3] and i[5]==primeiro_acesso[indice][4]):
				qtde_vezes_ip[indice] += 1
		else:
			ips_encontrados.append(i[0])
			qtde_vezes_ip.append(1)
			l = [i[1],i[2],i[3],i[4],i[5],i[6]]
			primeiro_acesso.append(l)

'''
Ao analisar os IP's que foram encontrados, irei considerar aqui que se em um instante
de um minuto houver 50 ou mais acessos realizados pelo mesmo IP, o mesmo será bloqueado pelo firewall.
'''
for i in ips_encontrados:
	if (qtde_vezes_ip[ips_encontrados.index(i)]>=50):
		#print "iptables -I INPUT -s {0} -j DROP".format(i)
		os.system("iptables -I INPUT -s {0} -j DROP".format(i));