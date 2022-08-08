import pandas as pd 

kashi_df = pd.read_csv('out/kashi_avax.csv')
pools_df = pd.read_csv('out/avalanche_final.csv')

token1_series = pools_df[['TOKEN1_NAME','TOKEN1_ADDRESS','TOKEN1_DECIMALS']]
token2_series = pools_df[['TOKEN2_NAME','TOKEN2_ADDRESS','TOKEN2_DECIMALS']]
token1_series.columns = ['TOKEN_NAME','ADDRESS','DECIMALS']
token2_series.columns = ['TOKEN_NAME','ADDRESS','DECIMALS']

tokens = pd.concat([token1_series,token2_series])
tokens.loc[len(tokens.index)] = ['WETH','0x49d5c2bdffac6ce2bfdb6640f4f80f226bc10bab', 18]


df = pd.DataFrame(
    columns=[
    'PAIR_NAME',
    'PAIR_ADDRESS',
    'ASSET_NAME',
    'COLLATERAL_NAME',
    'ASSET_ADDRESS',
    'COLLATERAL_ADDRESS',
    'ASSET_DECIMALS',
    'COLLATERAL_DECIMALS'
])

for row in kashi_df.iterrows() : 

    pair_name = row[1].POOL_NAME
    pair_address = row[1].POOL_ADDRESS
    asset_name = pair_name.split('/')[0]
    collateral_name = pair_name.split('/')[1]

    try: 
        asset_info = tokens[tokens['TOKEN_NAME'] == asset_name].reset_index(drop=True).iloc[0]
        collateral_info = tokens[tokens['TOKEN_NAME'] == collateral_name].reset_index(drop=True).iloc[0]

        asset_address= asset_info.ADDRESS   
        collateral_address= collateral_info.ADDRESS   
        asset_decimal= asset_info.DECIMALS
        collateral_decimal= collateral_info.DECIMALS

    except: 
        asset_address= None
        collateral_address= None
        asset_decimal= None
        collateral_decimal= None

    df.loc[len(df.index)] = [pair_name, pair_address, asset_name, collateral_name, asset_address, collateral_address, asset_decimal, collateral_decimal] 

df.to_csv('kashi_avax_final.csv')
