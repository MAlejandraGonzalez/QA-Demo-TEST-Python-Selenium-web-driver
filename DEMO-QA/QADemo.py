from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string

def generar_nombre():
 return "User_" + ''.join(random.choices(string.ascii_letters, k=5))

def generar_email():
    return ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"

def generar_direccion():
    return "Street " + str(random.randint(1, 100))

# 1. Configurar el driver
driver = webdriver.Chrome()
driver.maximize_window()

# 2. Abrir la URL
driver.get("https://demoqa.com/text-box")

# 3. Generar datos dinámicos
nombre = generar_nombre()
email = generar_email()
direccion1 = generar_direccion()
direccion2 = generar_direccion()

# 4. Llenar formulario
driver.find_element(By.ID, "userName").send_keys(nombre)
driver.find_element(By.ID, "userEmail").send_keys(email)
driver.find_element(By.ID, "currentAddress").send_keys(direccion1)
driver.find_element(By.ID, "permanentAddress").send_keys(direccion2)

# 5. Enviar formulario
driver.find_element(By.ID, "submit").send_keys(Keys.ENTER)
time.sleep(1)  # Pequeña espera para que cargue el resultado

# 6. Assertions para validar resultados
assert nombre in driver.find_element(By.ID, "name").text
assert email in driver.find_element(By.ID, "email").text
assert direccion1 in driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
assert direccion2 in driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text

print("✅ Test pasado correctamente con datos dinámicos")

# 7. Cerrar navegador
driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random
import string

def generar_nombre():
    return "User_" + ''.join(random.choices(string.ascii_letters, k=5))

def generar_email():
    return ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"

def generar_direccion():
    return "Street " + str(random.randint(1, 100))

# Configuración para GitHub Actions (modo headless)
options = Options()
options.add_argument("--headless")  
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 1. Configurar el driver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# 2. Abrir la URL
driver.get("https://demoqa.com/text-box")

# 3. Generar datos dinámicos
nombre = generar_nombre()
email = generar_email()
direccion1 = generar_direccion()
direccion2 = generar_direccion()

# 4. Llenar formulario
driver.find_element(By.ID, "userName").send_keys(nombre)
driver.find_element(By.ID, "userEmail").send_keys(email)
driver.find_element(By.ID, "currentAddress").send_keys(direccion1)
driver.find_element(By.ID, "permanentAddress").send_keys(direccion2)

# 5. Enviar formulario
driver.find_element(By.ID, "submit").send_keys(Keys.ENTER)
time.sleep(1)

# 6. Assertions para validar resultados
assert nombre in driver.find_element(By.ID, "name").text
assert email in driver.find_element(By.ID, "email").text
assert direccion1 in driver.find_element(By.XPATH, "//p[@id='currentAddress']").text
assert direccion2 in driver.find_element(By.XPATH, "//p[@id='permanentAddress']").text

print("✅ Test pasado correctamente con datos dinámicos")

# 7. Cerrar navegador
driver.quit()
