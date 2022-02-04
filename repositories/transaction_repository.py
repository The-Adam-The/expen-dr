from db.run_sql import run_sql

from models.transaction import Transaction

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository



def save(transaction):
    sql = "INSERT INTO transactions (date, merchant_id, tag_id, amount) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.date, transaction.merchant.id, transaction.tag.id, transaction.amount]
    results  = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction


def select_all():

    transactions = []

    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    
    if results is not None:
        for row in results:
            merchant = merchant_repository.select(row['merchant_id'])
            tag = tag_repository.select(row['tag_id'])
            transaction = Transaction(row['date'], merchant, tag, row['amount'], row['id'])
            transactions.append(transaction)
        return transactions

