from flask import Flask, render_template
from flask import Blueprint

import repositories.transaction_repository as transaction_repository

transaction_blueprint = Blueprint("transaction", __name__)

@transaction_blueprint.route('/transactions')
def transactions():
    transactions = transaction_repository.select_all()
    return render_template('transactions/index.html', transactions=transactions)

    