# coding: utf-8

import re
import os

arquivo = open("auth.log")
texto = arquivo.read()
'''
Lê do arquivo de log do ssh, o IP, a data (dia e mes) e a hora (hora, minutos e segundos). 
'''
conteudo=texto.split('\n')
ips_encontrados = []
num_vezes_hora = []
primeiro_acesso_hora = []
ips_bloqueados = []

for i in conteudo:
	aux = i.split(" ")
	'''
	Pega a linha do arquivo do syslog e verifica se a linha possui a palavra ssh2 e a expressão
	"Failed password" que indicam respectivamente o serviço ssh e a falha das credenciais para o serviço. 
	'''
	if ("Failed password" in i and aux[len(aux)-1]=="ssh2"):
		#print i
		# Verifica se o ip da linha já está na variável de IP's encontrados ou se ele está bloqueado
		if (aux[10] in ips_encontrados and not aux[10] in ips_bloqueados):
			indice = ips_encontrados.index(aux[10])
			hora = aux[2].split(":")
			# Verifica se o dia e o mês são os mesmos para o primeiro registro encontrado
			if (primeiro_acesso_hora[indice][0]==aux[0] and primeiro_acesso_hora[indice][1]==aux[1]):
				'''
				Nesta parte do código, o programa verifica a hora da tentativa. Se a hora for diferente, o aplicativo já verifica a 
				quantidade de tentativas falhas e bloqueia o IP no firewall. Se a hora for igual ao do registro analisado, o programa
				acrescenta mais uma tentativa e também verifica o número de tentativas. Nos dois casos, o ip que ultrapassa o limite 
				estabelecido de no máximo 3 tentativas em uma hora vai para uma variável de IP's bloqueados.
				'''
				if (primeiro_acesso_hora[indice][2]!=hora[0]):
					if (num_vezes_hora[indice]>=3):
						print "Bloqueia ip ",aux[10]
						#os.system("iptables -I INPUT -s {0} -j DROP".format(aux[10]));
						ips_bloqueados.append(aux[10])
					else:
						primeiro_acesso_hora[indice][2]=hora[0]
						primeiro_acesso_hora[indice][3]=hora[1]
						primeiro_acesso_hora[indice][4]=hora[2]
						num_vezes_hora[indice]=1
				elif (primeiro_acesso_hora[indice][2]==hora[0]):
					num_vezes_hora[ips_encontrados.index(aux[10])] += 1
					if (num_vezes_hora[indice]>=3):
						print "Bloqueia ip ",aux[10]
						#os.system("iptables -I INPUT -s {0} -j DROP".format(aux[10]));
						ips_bloqueados.append(aux[10])
		else:
			ips_encontrados.append(aux[10])
			num_vezes_hora.append(1)
			hora = aux[2].split(":")
			l = [aux[0],aux[1],hora[0],hora[1],hora[2]]
			# print l
			primeiro_acesso_hora.append(l)
