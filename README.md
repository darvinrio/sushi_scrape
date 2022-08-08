This is a quickly thrown together readme and project

The requirements are `pandas` and `selenium` 

1. Start with the `scrape_pools.py`.
This will scrape the *`https://app.sushi.com/analytics/pools?chainId=<chain_id>`* for all Pools deployed 

2. Now run the `scrape_tokens.py`. This will scrape *`https://app.sushi.com/analytics/pools/<pool_address>?chainId=<chain_id>`* for each Pool, the tokens involved. 
3. Now run the `scrape_decimals.py`. This will scrape *`https://<blockchain_explorer_url>/token/<token_address>`* for a given Tokens decimals. This script will also merge all the data to emit the final list of Pools.  
4. You will need to copy and make barebone of the Kashi HTML from *`https://app.sushi.com/kashi?view=lend&chainId=<chain_id>`*. The latest barebone is available in the `html` folder
5. Running `scrape_kashi.py` will scrape the Kashi Deployment data from the barebone HTML
6. Running `make_kashi.py` will use the previously generated Token Data from the Pool database to find the Addresses and Decimals of the Kashi Pair Tokens

> NOTE : 
Since the project was put-together in a short time frame, the git repository requires the user to go through the code and make necessary changes and file movements to get the code running. The necessary changes meanwhile are being made by the owner
