from flask import Flask, render_template
from flask import Blueprint

import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint('merchants', __name__)

@merchants_blueprint.route('/merchants')
def merchants():
    merchants = merchant_repository.select_all()
    return render_template('merchants/index.html', merchants=merchants)

@merchants_blueprint.route('/merchants/<id>')
def show(id):
    merchant = merchant_repository.select(id)
    return render_template('merchants/show.html', merchant=merchant)