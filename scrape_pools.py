from selenium import webdriver
from selenium.webdriver.common.by import By

import pandas as pd

df = pd.DataFrame(columns=[
    'POOL_NAME',
    'POOL_ADDRESS'
])

print('scraping started')

driver = webdriver.Chrome()

# op = webdriver.ChromeOptions()
# op.add_argument('headless')
# driver = webdriver.Chrome(options=op)

# AVALANCHE
# driver.get('https://app.sushi.com/analytics/pools?chainId=43114') 

# BSC
driver.get('https://app.sushi.com/analytics/pools?chainId=56') 

# GET NUMBER OF POOLS
# pools_span = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/main/div/div/div[2]/div[4]/div[1]/span[2]")
# pools = int(pools_span.text.split()[-1])

# AVALANCHE
# pools = 306

# BSC
pools = 1617
print(pools)

i = 0
while i<pools :
    # GET ALL ROWS IN THE PAGE
    rows = driver.find_elements(By.XPATH, "//tr[@class='hover:bg-dark-900/40 hover:cursor-pointer']")
    i+= len(rows)

    # ITERATE THROUGH ROWS
    for row in rows :

        pool_name = (row.find_element(By.XPATH, ".//td[@class='py-3 border-t border-dark-900 flex items-center pl-4 justify-start']")).text
        href = row.get_attribute('href')
        pool_address = (href.split('?')[0]).split('/')[-1]

        # APPEND TO DATAFRAME
        df.loc[len(df.index)] = [pool_name, pool_address] 

    # FIND AND CLICK NEXT BUTTON

    try :
        nextButton = driver.find_element(By.XPATH, "//div[@class='flex-grow p-3 text-right text-high-emphesis cursor-pointer']")
        nextButton.click()
    except : 
        print('No Button')

    # if i>0: 
    #     break


df.to_csv('out.csv')
driver.close()
print('scraping done')


