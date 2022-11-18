from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys 
import variables

def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.01)

driver = webdriver.Chrome(executable_path=variables.path)
driver.get(variables.web)
driver.maximize_window()  

usuari = driver.find_element_by_name('email')
time.sleep(3)  
slow_typing(usuari, variables.usuari)
contrasenya = driver.find_element_by_name('contrasenya')
slow_typing(contrasenya, variables.password)
driver.find_element_by_id("entrar").click()
time.sleep(0.5)  
driver.find_element_by_id("fichar_web").click()