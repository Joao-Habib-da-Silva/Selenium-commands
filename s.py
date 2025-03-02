from selenium import webdriver
import time as t
#Primeiro, identifique o navegador que vai usar, o selenium só suporta drivers do Firefox, Chrome, Edge e Safari
nav = webdriver.Chrome()
#Agora nós direcionamos ela a um link, usando a função get
nav.get('https://www.hashtagtreinamentos.com')
#Agora iremos mudar o tamanho de sua tela
nav.maximize_window()
# Agora, iremos identificar um elemento
botao = nav.find_element('class name', 'botao-verde')
#podemos agora usa-la
botao.click()
#vamos ver o que acontece se usarmos o header

#tempo, para isso, iremos usar a biblioteca padrão para podermos acionar a função
t.sleep(10000)  