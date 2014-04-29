#----------------------------------------------------------------------------#
# Imports.
#----------------------------------------------------------------------------#

from flask import *  # do not use '*'; actually input the dependencies.
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf import Form
from sqlalchemy.orm import load_only
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.ext.sqlalchemy.orm import model_form
import logging
from logging import Formatter, FileHandler
from wtforms.widgets import TextArea
import models

#----------------------------------------------------------------------------#
# Helpers
#----------------------------------------------------------------------------#

def all_books():
    return models.Item.query

#----------------------------------------------------------------------------#
# Forms
#----------------------------------------------------------------------------#

PostForm = model_form(models.Post, Form, field_args={
    'description': {'widget': TextArea()},
    'books': {'widget': QuerySelectField('book_list', query_factory=all_books(),
                                         get_label='description', allow_blank=True)}
})

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/create/posting', methods=['GET', 'POST'])
def create_posting():
    form = PostForm()
    if request.method == 'POST' and form.validate():
        redirect('/')
    return render_template('pages/create_post.html', form=form)


@app.route('/get_all_books')
def get_all_books():
    books = models.db_session.query(models.Item)
    # books = models.Item.query.all()
    return Response([i.json for i in books], mimetype='application/json')

# Error handlers.

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def internal_error(error):
    return render_template('errors/404.html'), 404


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '
                                        '[in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''