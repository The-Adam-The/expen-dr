from flask import Flask, render_template
from flask import Blueprint

import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route('/tags')
def tags():
    tags = tag_repository.select_all()
    return render_template('tags/index.html', tags=tags)

@tags_blueprint.route('/tags/<id>')
def show(id):
    tag = tag_repository.select(id)
    return render_template('tags/show.html', tag=tag)