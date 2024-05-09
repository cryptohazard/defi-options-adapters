import marimo

__generated_with = "0.5.0"
app = marimo.App()


@app.cell
def __():
    from web3 import Web3
    import json
    return Web3, json


@app.cell
def __(Web3):
    # HTTPProvider:
    rpc = 'https://mainnet.infura.io/v3/c1b94bff90754066a81d195ddc337ff3'
    w3 = Web3(Web3.HTTPProvider(rpc))

    return rpc, w3


@app.cell
def __(w3):
    dir(w3)
    return


@app.cell
def __():
    # constants
    usdcaddress      ='0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'
    wethaddress      ='0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
    squeethaddress   = '0xf1B99e3E573A1a9C5E6B2Ce818b617F0E664E86B'
    controlleraddress= '0x64187ae08781B09368e6253F9E94951243A493D5'
    quoteraddress    = '0xC8d3a4e6BB4952E3658CCA5081c358e6935Efa43'
    shortpowerperpaddress     = '0xa653e22A963ff0026292Cc8B67941c0ba7863a38'
    return (
        controlleraddress,
        quoteraddress,
        shortpowerperpaddress,
        squeethaddress,
        usdcaddress,
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
    dir(controller.functions)
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


@app.cell(disabled=True)
def __(controller, numberofvaults):
    safe=[]
    for v in range(0,numberofvaults):
        safe.append(controller.functions.isVaultSafe(v).call())
    safe
    return safe, v


@app.cell
def __(controller):
    controller.functions.vaults(419).call()
    return


@app.cell
def __():
    a=range(0,10)
    print(*a, sep='\n')
    return a,


@app.cell
def __(controller, numberofvaults):
    state=[]
    for vv in range(0,numberofvaults):
        state.append(controller.functions.vaults(vv).call())
    state
    return state, vv


@app.cell
def __(state):
    def hasNFT(l: list):
        result=[]
        for s in l:
            if s[1] != 0:
                result.append(s)
                print(f'vault {state.index(s)}: {s}')
        return result

    nfts=hasNFT(state)
    return hasNFT, nfts


@app.cell
def __(state):
    def hasdebt(l: list):
        result=[]
        for s in l:
            if s[3] != 0:
                result.append(s)
                print(f'vault {state.index(s)}: {s}')
        return result

    vaults=hasdebt(state)
    return hasdebt, vaults


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
