import marimo

__generated_with = "0.5.2"
app = marimo.App()


@app.cell
def __():
    from web3 import Web3
    import json
    from uniswap import Uniswap
    import decimal
    return Uniswap, Web3, decimal, json


@app.cell
def __(Web3):
    # HTTPProvider:
    rpc = 'https://mainnet.infura.io/v3/c1b94bff90754066a81d195ddc337ff3'
    w3 = Web3(Web3.HTTPProvider(rpc))
    return rpc, w3


@app.cell
def __(Uniswap, rpc):
    # constants
    version = 3                       # specify which version of Uniswap to use
    uniswap = Uniswap(address='',private_key='',provider=rpc, version = version)
    ether = "0x0000000000000000000000000000000000000000"
    osqth = "0xf1B99e3E573A1a9C5E6B2Ce818b617F0E664E86B"
    usdc= "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

    controlleraddress= '0x64187ae08781B09368e6253F9E94951243A493D5'
    quoteraddress    = '0xC8d3a4e6BB4952E3658CCA5081c358e6935Efa43'
    shortpowerperpaddress     = '0xa653e22A963ff0026292Cc8B67941c0ba7863a38'
    return (
        controlleraddress,
        ether,
        osqth,
        quoteraddress,
        shortpowerperpaddress,
        uniswap,
        usdc,
        version,
    )


@app.cell
def __():
    numberofvaults = 420
    return numberofvaults,


@app.cell
def __(json):
    f = open('controller.abi')

    # returns JSON object as 
    # a dictionary
    abi = json.load(f)
    return abi, f


@app.cell
def __(abi, controlleraddress, w3):
    controller = w3.eth.contract(address=controlleraddress,abi=abi)
    return controller,


@app.cell
def __(controller, decimal):
    norm = decimal.Decimal(controller.functions.normalizationFactor().call()/10**18)
    norm
    return norm,


@app.cell
def __():
    '''
    returns
    Vault{
        Operator:         vault.Operator,
        NftCollateralId:  vault.NftCollateralId,
        CollateralAmount: vault.CollateralAmount,
        ShortAmount:      vault.ShortAmount
    }

    '''
    return


@app.cell
def __(controller, numberofvaults):
    state=[]
    first = 0# 250 # 0
    last  =  numberofvaults # 300
    for v in range(first,last):
        state.append(controller.functions.vaults(v).call())
    state
    return first, last, state, v


@app.cell
def __(state, w3):
    ps = [] #pretty state
    for s in state:
        ps.append([
            s[0],
            s[1],
            round(w3.from_wei(s[2],'ether'),4),
            round(w3.from_wei(s[3],'ether'),4)
            ])
    ps
    return ps, s


@app.cell
def __(ps):
    def hasNFT(l: list):
        result=[]
        for s in l:
            if s[1] != 0:
                result.append(s)
                print(f'vault {ps.index(s)}: {s}')
        return result

    nfts=hasNFT(ps)
    return hasNFT, nfts


@app.cell
def __(decimal, ether, osqth, uniswap):
    price_squeeth_weth = decimal.Decimal(uniswap.get_price_input(osqth, ether, 1*10**18, fee=3000)/10**18)
    price_squeeth_weth
    return price_squeeth_weth,


@app.cell
def __(decimal, ether, uniswap, usdc):
    price_usdc = decimal.Decimal(uniswap.get_price_input(ether, usdc, 1*10**18, fee=3000)/10**6)
    price_usdc
    return price_usdc,


@app.cell
def __(price_squeeth_weth, price_usdc):
    price_squeeth= price_squeeth_weth * price_usdc
    price_squeeth
    return price_squeeth,


@app.cell
def __(norm, price_squeeth):
    def ratio(v):
        r = v[3] * price_squeeth * norm/v[2]
        return r

    return ratio,


@app.cell
def __(ps, ratio):
    def hasdebt(l: list):
        result=[]
        
        for s in l:
            if s[3] != 0:
                result.append(s)
                cr = ratio(s)
                print(f'vault {ps.index(s)}: Coll. ratio {cr:.2f} {s}')
        return result

    vaults=hasdebt(ps)
    return hasdebt, vaults


@app.cell
def __():
    crabv1=70  #vault of crab v1.
    crab=286 #vault of crab v2
    threshold = 1.5 #150%
    return crab, crabv1, threshold


@app.cell
def __(crab, ratio, state, w3):
    bal = w3.from_wei(state[crab][2],'ether')
    debt= w3.from_wei(state[crab][3],'ether')
    print(f'The Crab strategy has {bal:.2f} ETH of collateral \nand {debt:.2f} SQUEETH of debt!')
    print(f'This brings its collateral ratio to {ratio(state[crab]):.2f}.')
    return bal, debt


@app.cell
def __(norm, price_squeeth, price_usdc):
    p2 = price_usdc*price_usdc
    diff = (10000*price_squeeth/norm-p2)/p2
    100*diff
    print(f'The current diff between Squeeth and ETH^2 is {100*diff:.2f}%.')

    return diff, p2


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
