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

 
import requests
import json
import re
import clipboard

# Remove porra do 'Unverified HTTPS request is being made.'
requests.packages.urllib3.disable_warnings() 

ctrlv = clipboard.paste()

def bitly(ctrlv):

	# Coloque aqui a sua oauth-key:
	# https://bitly.com/a/oauth_apps
	API = '3efaf0a42a5c4a2274e193cee7f1efb84197610b'


	# Preciso melhorar esse regex.
	regexes = [
    	"http[s]?://",
    	"(www\.)?[a-z0-9\.:].*?(?=\s)"
    	]

	# Cria um regex que inclue todas nossas condições.
	HTTP_regex = "(" + ")|(".join(regexes) + ")"

	# Adiciona seu Clipboard a uma variavel 



	# Condição para verificar se o cliboard é um UR valido ou não.
	if re.match(HTTP_regex, ctrlv):
		print "[ Encurtando o URL... ]"

		parametros = {'access_token': API,'longUrl': ctrlv} 

		bitly = 'https://api-ssl.bitly.com/v3/shorten'
		response = requests.get(bitly, params=parametros, verify=False)

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

if __name__ == '__main__':
	bitly(ctrlv)
else:
	bitly(ctrlv)

# caso queria importar e usar como um modulo :)

# import bitly
# bitly('https://github.com/thezakman')
