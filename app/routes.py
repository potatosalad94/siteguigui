from flask import render_template, url_for
from app import app

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
   return render_template(page_name)
