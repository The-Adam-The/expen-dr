import pdb

from models.merchant import Merchant


import repositories.merchant_repository as merchant_repository

merchant1 = Merchant('Tesco')
merchant_repository.save(merchant1)

merchant2 = Merchant('Amazon')
merchant_repository.save(merchant2)

results = merchant_repository.select_all()

for result in results:
    print(result.__dict__)

single_select_result = merchant_repository.select(5)

print(single_select_result.__dict__)