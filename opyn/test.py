import marimo

__generated_with = "0.5.2"
app = marimo.App()


@app.cell
def __():
    from web3 import Web3
    import json
    from uniswap import Uniswap

    return Uniswap, Web3, json


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
    eth = "0x0000000000000000000000000000000000000000"
    weth = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    osqth = "0xf1B99e3E573A1a9C5E6B2Ce818b617F0E664E86B"
    usdc= "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

    usdcaddress      ='0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
    wethaddress      ='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    squeethaddress   = '0xf1B99e3E573A1a9C5E6B2Ce818b617F0E664E86B'
    controlleraddress= '0x64187ae08781B09368e6253F9E94951243A493D5'
    quoteraddress    = '0xC8d3a4e6BB4952E3658CCA5081c358e6935Efa43'
    shortpowerperpaddress     = '0xa653e22A963ff0026292Cc8B67941c0ba7863a38'
    return (
        controlleraddress,
        eth,
        osqth,
        quoteraddress,
        shortpowerperpaddress,
        squeethaddress,
        uniswap,
        usdc,
        usdcaddress,
        version,
        weth,
        wethaddress,
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
def __(controller):
    controller.functions.vaults(389).call()
    return


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
def __():
    crabv1=70  #vault of crab v1.
    crab=286 #vault of crab v2
    return crab, crabv1


@app.cell
def __(crab, state, w3):
    bal = w3.from_wei(state[crab][2],'ether')
    debt= w3.from_wei(state[crab][3],'ether')
    print(f'The Crab strategy has {bal} ETH of collateral and {debt} SQUEETH of debt!')
    return bal, debt


@app.cell
def __(ps):
    type(ps)
    return


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
def __(ps):
    def hasdebt(l: list):
        result=[]
        for s in l:
            if s[3] != 0:
                result.append(s)
                print(f'vault {ps.index(s)}: {s}')
        return result

    vaults=hasdebt(ps)
    return hasdebt, vaults


@app.cell
def __(eth, osqth, uniswap):
    uniswap.get_price_input(eth, osqth, 1*10**18, fee=3000)/10**18
    return


@app.cell
def __(eth, uniswap, usdc):
    uniswap.get_price_input(eth, usdc, 1*10**18, fee=3000)/10**6

    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
