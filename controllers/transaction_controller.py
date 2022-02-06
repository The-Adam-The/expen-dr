from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository

transaction_blueprint = Blueprint("transaction", __name__)



#Create 
@transaction_blueprint.route('/transactions/new')
def new_transaction():
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template('transactions/new.html', tags=tags, merchants=merchants)

@transaction_blueprint.route('/transactions', methods=['POST'])
def add_transaction():    
    date = request.form['date']
    amount = request.form['amount']
    merchant_id = request.form['merchant']
    tag_id = request.form['tag']

    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)

    transaction = Transaction(date, amount, merchant, tag)
    transaction_repository.save(transaction)
    return redirect('/transactions')

#Read All
@transaction_blueprint.route('/transactions')
def transactions():
    transactions = transaction_repository.select_all()
    return render_template('transactions/index.html', transactions=transactions)

#Read One
@transaction_blueprint.route('/transactions/<id>')
def show(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/show.html', transaction=transaction)

#Update

#Delete