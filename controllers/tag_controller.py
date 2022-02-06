from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.tag import Tag

import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

#Create
@tags_blueprint.route('/tags/new')
def new_tag():
    return render_template("tags/new.html")

@tags_blueprint.route('/tags', methods=['POST'])
def add_tag():
    name = request.form['name'].capitalize()
    tag = Tag(name)
    tag_repository.save(tag)
    return redirect('/tags')


#Read all
@tags_blueprint.route('/tags')
def tags():
    tags = tag_repository.select_all()
    return render_template('tags/index.html', tags=tags)

#Read one
@tags_blueprint.route('/tags/<id>')
def show(id):
    tag = tag_repository.select(id)
    return render_template('tags/show.html', tag=tag)


#Update

#Delete
