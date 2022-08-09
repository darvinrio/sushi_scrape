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
    'TOKEN1_NAME',
    'TOKEN2_NAME',
    'TOKEN1_ADDRESS',
    'TOKEN2_ADDRESS',
    'TOKEN1_DECIMALS',
    'TOKEN2_DECIMALS'
])

# pool_df = pd.read_csv('out/avalanche_pool_tokens.csv')
pool_df = pd.read_csv('out/bsc_pool_tokens.csv')

# decimal_df = pd.read_csv('avalanche_snowtrace_decimals.csv')
decimal_df = pd.read_csv('bsc_scan_decimals.csv')
available_token_data = decimal_df.TOKEN_ADDRESS

print('scraping started')

# driver = webdriver.Chrome()
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
wait = WebDriverWait(driver, 10)

# PREPARE UNIQUE TOKENS
token1s = pool_df.TOKEN1_ADDRESS
token2s = pool_df.TOKEN2_ADDRESS

tokenList = (pd.concat([token1s, token2s], ignore_index=True)).unique()
print(len(tokenList))

i = 0

for token in tokenList:

    if (available_token_data.isin([token])).sum() > 0:
        # if pd.isnull((available_token_data.loc[available_token_data['TOKEN_ADDRESS'] == token]).DECIMALS) :
            # pass 
        # else:
        print(token)
        print('skip')
        continue 
    else:
        # print(token)
        # print(skip)
        pass

    i+=1
    if i%10 == 0:
        print(i)

    # driver.get('https://snowtrace.io/token/'+token)
    driver.get('https://bscscan.com/token/'+str(token))
    try:
        decimal_div = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div[4]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]")))
        decimals = decimal_div.text
    except TimeoutException: 
        decimals = None
    except: 
        print('new error')
        print(token)

    decimal_df.loc[len(decimal_df.index)] = [token, decimals] 

    # if i==50 :
        # break

driver.close()
# decimal_df.to_csv('avalanche_snowtrace_decimals.csv')
decimal_df.to_csv('bsc_scan_decimals.csv',index=False)


for pool in pool_df.iterrows() : 

    pool_name = pool[1].POOL_NAME
    pool_address = pool[1].POOL_ADDRESS
    token1_name = pool_name.split('/')[0]
    token2_name = pool_name.split('/')[1]
    token1_address = pool[1].TOKEN1_ADDRESS
    token2_address = pool[1].TOKEN2_ADDRESS

    # print(decimal_df[decimal_df['TOKEN_ADDRESS']==token1_address].reset_index().DECIMALS[0])
    try:
        token1_decimal = decimal_df[decimal_df['TOKEN_ADDRESS']==token1_address].reset_index().DECIMALS[0]
        token2_decimal = decimal_df[decimal_df['TOKEN_ADDRESS']==token2_address].reset_index().DECIMALS[0]
    except:
        token1_decimal = None
        token2_decimal = None

    # APPEND TO DATAFRAME
    df.loc[len(df.index)] = [pool_name, pool_address, token1_name, token2_name, token1_address, token2_address, token1_decimal, token2_decimal] 


# df.to_csv('avalanche_final.csv')
df.to_csv('bsc_final.csv')

print('scraping ended')

