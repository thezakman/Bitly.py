#!/usr/bin/python
# -*- coding: utf-8 -*-

#		 _     _ _   _       
#		| |   (_) | | |      
#		| |__  _| |_| |_   _ 
#		| '_ \| | __| | | | |
#		| |_) | | |_| | |_| |
#		|_.__/|_|\__|_|\__, |
#		                __/ |
#		 - URL-Shorter |___/ 

'''
Bitly URL Shortener - Python Script/Module
'''

#	https://github.com/thezakman
#	https://twitter.com/thezakman

__author__ = "TheZakMan"


# [Como usar:]=================
#  Copie o url que você queira 
#  encurtar e execute o script.
#  Basta dar Ctrl+v agora :)
# =============================

# [Dependencias:]=============
# sudo pip install clipboard
# ============================


# [Importando:]=============
# Caso queria importar e usar como um modulo:

# import bitly

# bitly.encurtar('https://github.com/thezakman')
# bitly.expandir('http://bit.ly/1FunbVI')
# bitly.clicks('http://bit.ly/1FunbVI')
# ============================


import requests
import json
import re
import clipboard

# Remove a porra do 'Unverified HTTPS request is being made.'
requests.packages.urllib3.disable_warnings() 

# Adiciona seu Clipboard a uma variavel 
ctrlv = clipboard.paste()

# Coloque aqui a sua oauth-key:
# https://bitly.com/a/oauth_apps
API_KEY = 'SUA_API_AQUI'


# Função para mostrar o numero de vezes que o link foi clickado.
def clicks(ctrlv):
	query_params = {'access_token': API_KEY,
                'link': 'http://bitly.com/RYYpZT'} 

	URL = 'https://api-ssl.bitly.com/v3/link/clicks'
	response = requests.get(URL, params=query_params, verify=False)

	data = json.loads(response.content)
	
	print '[ URL Clickado ]: %s vezes' % data['data']['link_clicks']




# Função para exandir links
def expandir(ctrlv):
	if 'bit.ly' in ctrlv:
			print '[!] Expandindo o URL:'
			print requests.get(ctrlv).url



# Função principal encurta/expande links
def encurtar(ctrlv):

	global API_KEY


	# (╯°□°)╯ Preciso melhorar esse regex!
	regexes = [
    	"http[s]?://",
    	"(www\.)?[a-z0-9\.:].*?(?=\s)"
    	]

	# Cria um regex que inclue todas nossas condições.
	HTTP_regex = "(" + ")|(".join(regexes) + ")"

	# Condição para expandir o link bitly do cliboard.
	if 'bit.ly' in ctrlv:
			print '[ Expandindo o URL ... ]'
			print requests.get(ctrlv).url
			clicks(ctrlv)
			exit(1)

	# Condição para verificar se o cliboard é um UR valido ou não.
	if re.match(HTTP_regex, ctrlv):
		print "[ Encurtando o URL ... ]"

		parametros = {'access_token': API_KEY,'longUrl': ctrlv} 

		URL = 'https://api-ssl.bitly.com/v3/shorten'
		response = requests.get(URL, params=parametros, verify=False)

		data = json.loads(response.content)
		
		

		if '500' in response.content:
			print '[!] Não é um URL válido'
		else:
			print data['data']['url']
			
			# Variavel do Clipboard 
			short_url = data['data']['url']
			
			# Adiciona ao Clipboard, agora é só dar ctrl+v nessa porra.
			clipboard.copy(short_url)

	else:
		print "[!] Não achei URL no seu clipboard"



# Acho que não preciso explicar isso, nem pra mim nem pra você.
if __name__ == '__main__':
	encurtar(ctrlv)
