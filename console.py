import pdb

from models.merchant import Merchant


import repositories.merchant_repository as merchant_repository

merchant1 = Merchant('Tesco')
merchant_repository.save(merchant1)

results = merchant_repository.select_all()

for result in results:
    print(result.__dict__)