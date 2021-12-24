from brownie import accounts, config,SimpleStorage, network

def deploy_simple_storage():
    # account = accounts[0] Development accounts
    # account = accounts.load('local-account')
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from" : account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from":account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    return accounts.add(config['wallets']["from_key"])

def main():
    deploy_simple_storage()


# local account: 0x9031e7b28B90cC37aDD7Ef914b1d5132FB0d51DF