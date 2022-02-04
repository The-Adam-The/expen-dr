import pdb

from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

merchant_repository.delete_all()
tag_repository.delete_all()

merchant1 = Merchant('Tesco')
merchant_repository.save(merchant1)

merchant2 = Merchant('Amazon')
merchant_repository.save(merchant2)

tag1 = Tag('Grocery')
tag_repository.save(tag1)

tag2 = Tag('Tax')
tag_repository.save(tag2)


transaction1 = Transaction('2022-01-31', 30.5, merchant1, tag1)
transaction_repository.save(transaction1)

results = transaction_repository.select_all()

for result in results:
    print(result.__dict__)


# results = tag_repository.select_all()

# for result in results:
#     print(result.__dict__)

# single_tag_select = tag_repository.select(4)

# print(single_tag_select.__dict__)


# results = merchant_repository.select_all()

# for result in results:
#     print(result.__dict__)

# single_select_result = merchant_repository.select(5)

# print(single_select_result.__dict__)