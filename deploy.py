from solcx import compile_standard, install_solc
import json
from web3 import Web3

install_solc("0.6.0")

with open("./SimpleStorage.sol", "r") as file:
 simple_storage_file = file.read()

compiled_sol = compile_standard(
 {
  "language": "Solidity",
  "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
  "settings": {
   "outputSelection": {
    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
   }
  }
 },
 solc_version="0.6.0"
)

with open("compiled_code.json", "w") as file:
 json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 5777
my_address = '0xcbE486dE01E07488eC2F682Bb4f0E513fB873126'
private_key = '0xb05ea85e4601e633e6ac55c3b6fb3e192bf8577c2fb120d515dcf8462b1c98b6'

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)