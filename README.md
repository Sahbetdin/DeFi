# DeFi
There is a liquidity pool pipeline A->B->C->D->E->A. Calculate max first coin to get into the pool in such a way that after a circle we have more coins than before.

For inputs use `config.py`. All pairs of liquidity pools are listed in `lps` variable.
`p` is fee which is currnetly set to 0.3%.  
Run `python defi.py`. This prints coins of A which is the answer to problem. As a reminder, the problem is to find the number of coins A which, in case of inserted in "circle", maximes their value.
