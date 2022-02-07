from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.merchant import Merchant

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

merchants_blueprint = Blueprint('merchants', __name__)


#Create
@merchants_blueprint.route('/merchants/new', methods=['GET'])
def new_merchant():
    return render_template("merchants/new.html")


@merchants_blueprint.route('/merchants', methods=['POST'])
def add_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect('/merchants')


#Read all
@merchants_blueprint.route('/merchants', methods=['GET'])
def merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/index.html', merchants=merchants)


@merchants_blueprint.route('/merchants/<id>', methods=['GET'])
def show(id):
    merchant = merchant_repository.select(id)
    transactions = transaction_repository.select_by_merchant(merchant)
    return render_template('merchants/show.html', merchant=merchant, transactions=transactions)


#Update
@merchants_blueprint.route('/merchants/<id>/edit', methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/edit.html', merchant=merchant)


@merchants_blueprint.route('/merchants/<id>', methods=['POST'])
def update_merchant(id):
    name = request.form['name']
    merchant = Merchant(name, id)
    merchant_repository.update_merchant(merchant)
    return redirect('/merchants')

#Delete 
@merchants_blueprint.route('/merchants/<id>/delete', methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')
