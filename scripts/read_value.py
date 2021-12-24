# reads directly from the rinkeby bloackchain from a contract that has already been deployed
from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1] #get most recent contract
    # ABI
    # Address
    print(simple_storage.retrieve())

def main():
    read_contract()