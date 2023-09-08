from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import Select
from time import sleep

def waitingID(driver,id, delayTime):
    wait = WebDriverWait(driver, delayTime)
    wait.until(EC.presence_of_element_located((By.ID, id)))

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://icp.administracionelectronica.gob.es/icpplus/citar?p=9&locale=es")

waitingID(driver, "tramiteGrupo[1]", 10)

select_tramite = driver.find_element(By.ID, "tramiteGrupo[1]")
select = Select(select_tramite)
select.select_by_value("4010")

driver.execute_script(f"window.scrollBy(0, 300);")
btnAccept = driver.find_element(By.ID, "btnAceptar")
btnAccept.click()

driver.execute_script(f"window.scrollBy(0, 500);")
waitingID(driver, "btnEntrar", 10)
btnEnter = driver.find_element(By.ID, "btnEntrar")
btnEnter.click()

waitingID(driver, "rdbTipoDocPas", 10)
btnPas = driver.find_element(By.ID, "rdbTipoDocPas")
btnPas.click()

waitingID(driver, "txtIdCitado", 10)
inputPass = driver.find_element(By.ID, "txtIdCitado")
inputPass.send_keys('Y7909092G')

waitingID(driver, "txtDesCitado", 10)
inputName = driver.find_element(By.ID, "txtDesCitado")
inputName.send_keys('ANNA CHIPAGA')

waitingID(driver, "txtPaisNac", 10)
inputcountry = driver.find_element(By.ID, "txtPaisNac")
select = Select(inputcountry)
select.select_by_value("202")

driver.execute_script(f"window.scrollBy(0, 800);")
waitingID(driver, "btnEnviar", 10)
btnAccept = driver.find_element(By.ID, "btnEnviar")
btnAccept.click()

# waitingID(driver, "btnSubmit", 10)
# btnEnter = driver.find_element(By.ID, "btnSubmit")
# btnEnter.click()

sleep(60)

driver.quit()
