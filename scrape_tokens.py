from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd

df = pd.DataFrame(
    columns=[
    'POOL_NAME',
    'POOL_ADDRESS',
    'TOKEN1_ADDRESS',
    'TOKEN2_ADDRESS'
])

# AVALANCHE
# chain_id = 43114
# pool_df = pd.read_csv('out/avalanche_pools.csv')

# BSC
chain_id = 56
pool_df = pd.read_csv('out/bsc_pools.csv')

print('scraping started')

# driver = webdriver.Chrome()
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
wait = WebDriverWait(driver, 20)

i=0
for pool in pool_df.iterrows() : 

    pool_name = pool[1].POOL_NAME
    pool_address = pool[1].POOL_ADDRESS
    token1 = None
    token2 = None

    i+=1
    if i%10 == 0:
        print(i)

    driver.get('https://app.sushi.com/analytics/pools/'+pool_address+'?chainId='+str(chain_id))

    try : 
        addresses = wait.until(EC.visibility_of_all_elements_located((By.XPATH, ".//td[@class='pl-4 border-t border-dark-900']")))
        # addresses = driver.find_elements(By.XPATH, "//td[@class='pl-4 border-t border-dark-900']")
        token1 = addresses[1].text
        token2 = addresses[2].text
        # print('')

        # APPEND TO DATAFRAME

    except TimeoutException:
        print(pool_address)
    except: 
        print('new problem')
        print(pool_address)

    df.loc[len(df.index)] = [pool_name, pool_address, token1, token2] 


driver.close()

df.to_csv('out.csv')

print('scraping ended')

