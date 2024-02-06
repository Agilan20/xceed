from brownie import accounts, config, SimpleStorage, network
import os

def deploy_simple_storage():
    # account = accounts[0]
    # print(account)

    # account = accounts.load("agilan-account")
    # print(account)

    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(account)

    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    # We cann directly import the contract using its name

    # account = accounts[0]
    account = get_account()
    simpleStorage = SimpleStorage.deploy({"from":account})
    print(simpleStorage)
    #transact
    #call

    stored_value = simpleStorage.retrieve()
    print(stored_value)

    transaction = simpleStorage.store(15, {"from": account})

    transaction.wait(1) # 1 -> no of blocks to be wait

    updated_stored_value = simpleStorage.retrieve()
    print(updated_stored_value)



    # account = get_account()
    # simple_storage = SimpleStorage.deploy({"from": account})
    # stored_value = simple_storage.retrieve()
    # print(stored_value)
    # transaction = simple_storage.store(15, {"from": account})
    # transaction.wait(1)
    # updated_stored_value = simple_storage.retrieve()
    # print(updated_stored_value)


def get_account():
    if(network.show_active() == "development"):
        return accounts[0]
    
    else:
        return accounts.add(config["wallets"]["from_key"])
    # if network.show_active() == "development":
    #     return accounts[0]
    # else:
    #     return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()