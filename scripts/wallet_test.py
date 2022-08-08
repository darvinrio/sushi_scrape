from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

EXTENSION_PATH = 'metamask.crx'

opt = Options()
opt.add_extension(EXTENSION_PATH)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)

driver.switch_to.window(driver.window_handles[0])
original_window = driver.current_window_handle

# Get Started
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/button"))).click()

# Import Wallet
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button"))).click()

# Donate Data. No thanks!
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[5]/div[1]/footer/button[1]"))).click()

time.sleep(1)

# Seed phrase
driver.find_element(By.ID, "import-srp__srp-word-0").send_keys("ball")
driver.find_element(By.ID, "import-srp__srp-word-1").send_keys("circle")
driver.find_element(By.ID, "import-srp__srp-word-2").send_keys("ramp")
driver.find_element(By.ID, "import-srp__srp-word-3").send_keys("garment")
driver.find_element(By.ID, "import-srp__srp-word-4").send_keys("unaware")
driver.find_element(By.ID, "import-srp__srp-word-5").send_keys("mutual")
driver.find_element(By.ID, "import-srp__srp-word-6").send_keys("burden")
driver.find_element(By.ID, "import-srp__srp-word-7").send_keys("grid")
driver.find_element(By.ID, "import-srp__srp-word-8").send_keys("demand")
driver.find_element(By.ID, "import-srp__srp-word-9").send_keys("rifle")
driver.find_element(By.ID, "import-srp__srp-word-10").send_keys("connect")
driver.find_element(By.ID, "import-srp__srp-word-11").send_keys("truly")

# Passwords
driver.find_element(By.ID, "password").send_keys("password")
driver.find_element(By.ID, "confirm-password").send_keys("password")

# Agree to T&Cs & Submit
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='create-new-vault__terms-checkbox']"))).click()

# Import Button
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div[2]/form/button"))).click()

# Congratulations page
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/button"))).click()

# Intro pop-up box
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popover-content']/div/div/section/div[2]"))).click()

driver.get('https://app.sushi.com/kashi?view=lend&chainId=43114') 
