from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

df = pd.DataFrame(columns=[
    'POOL_NAME',
    'POOL_ADDRESS'
])

print('scraping started')

# driver = webdriver.Chrome()
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

# AVALANCHE
driver.get('http://127.0.0.1:5500/kashi_avax.html') 

# BSC
# driver.get('http://127.0.0.1:5500/kashi_bsc.html') 


# GET ALL ROWS IN THE PAGE
rows = driver.find_elements(By.CLASS_NAME,"rio")

for row in rows :
    pool = row.text
    pool_name = pool.split('\n')[0]
    href = row.get_attribute('href')
    pool_address = href.split('/')[-1]

    df.loc[len(df.index)] = [pool_name, pool_address] 

# df.to_csv('kashi_bsc.csv')
df.to_csv('kashi_avax.csv')
driver.close()
print('scraping done')


