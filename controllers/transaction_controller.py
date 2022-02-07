from flask import Flask, render_template, request, redirect
from flask import Blueprint
import datetime

from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository


transaction_blueprint = Blueprint("transaction", __name__)

trans_last_output= []

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
    today_date = datetime.date.today()
    first_of_month = today_date.replace(day=1)
    
    # transactions = transaction_repository.select_all()
    transactions = transaction_repository.select_by_date(first_of_month, today_date)
    total_spent = Transaction.total_spending(transactions)

@transaction_blueprint.route('/transaction/<start_date>/<end_date', methods=['POST'])
def change_date_transactions(start_date, end_date):
    pass

    

    return render_template('transactions/index.html', transactions=transactions, total_spent=total_spent, today_date=today_date, first_of_month=first_of_month)

#Read One
@transaction_blueprint.route('/transactions/<id>')
def show(id):
    transaction = transaction_repository.select(id)
    return render_template('transactions/show.html', transaction=transaction)

#Update
@transaction_blueprint.route('/transactions/<id>/edit')
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    tags = tag_repository.select_all()
    merchants = merchant_repository.select_all()
    return render_template('transactions/edit.html', transaction=transaction, merchants=merchants, tags=tags)


@transaction_blueprint.route('/transactions/<id>', methods=['POST'])
def update_transaction(id):
    date = request.form['date']
    amount = request.form['amount']
    merchant_id = request.form['merchant']
    tag_id = request.form['tag']

    trans_last_output = [date, amount, merchant_id, tag_id, id]

    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)

    transaction = Transaction(date, amount, merchant, tag, id)
    transaction_repository.update_transaction(transaction)
    return redirect('/transactions')


#Delete
@transaction_blueprint.route('/transactions/<id>/delete', methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')
