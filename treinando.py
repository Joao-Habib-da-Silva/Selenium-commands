from selenium import webdriver
import time
nav = webdriver.Chrome()
nav.get("https://www.hashtagtreinamentos.com/curso-python?utm_source=site&utm_medium=header&utm_content=link-header-cursos&utm_campaign=programacao&conversion=lpy22-abr-25")
nav.find_element("id", 'firstname').send_keys("Flamengo.com.bt")
nav.find_element("id", 'email').send_keys("paiton.gmail.com")
nav.find_element("id", 'phone').send_keys("agua")
time.sleep(10000)