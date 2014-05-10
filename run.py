#----------------------------------------------------------------------------#
# Imports.
#----------------------------------------------------------------------------#
import uuid

from flask import *  # do not use '*'; actually input the dependencies.
from flask.ext.sqlalchemy import SQLAlchemy
from flask_wtf import Form
from sqlalchemy.orm import load_only
from wtforms.ext.sqlalchemy.orm import model_form
import logging
from logging import Formatter, FileHandler
from wtforms.widgets import TextArea
import models
from serializers import ItemsSerializer
#----------------------------------------------------------------------------#
# Helpers
#----------------------------------------------------------------------------#
user = models.User.query.first()


def all_books():
    return models.Item.query

#----------------------------------------------------------------------------#
# Forms
#----------------------------------------------------------------------------#

PostForm = model_form(models.Post, Form, field_args={
    'description': {'widget': TextArea()}
})

ItemForm = model_form(models.Item, Form)
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
    data = models.db_session.query(models.Post).join(models.Item)
    for i in data:
        print i.description
    return render_template('pages/home.html', posts=data)


@app.route('/create/posting', methods=['GET', 'POST'])
def create_posting():
    form = PostForm()
    itemForm = ItemForm()
    if request.method == 'POST':

        if request.data:
            data = json.loads(request.data)
            new_post = models.Post(
                int(data['book_item']),
                data['description'],
                user.id,
                price=data['price'],
                type='SellerPost',
                book_condition=data['book_condition'],
                condition_description=data['condition_description']
            )
            models.db_session.add(new_post)
            models.db_session.commit()

        return redirect(url_for('home'))

    return render_template('pages/create_post.html', form=form, itemForm=itemForm)

@app.route('/delete/posting/<id>', methods=['DELETE'])
def delete_posting(id):
    to_delete = models.db_session.query(models.Post).filter(models.Post.id == id).first()
    models.db_session.delete(to_delete)
    models.db_session.commit()
    return ""

@app.route('/create/item', methods=['POST'])
def create_book():
    posted_data = request.data

    if posted_data:
        data = json.loads(posted_data)
        new_item = models.Item(
            str(uuid.uuid4()),
            title=data['title'],
            authors=data['authors'],
            edition=data['edition'],
            img_url=data['img_url']
        )
        models.db_session.add(new_item)
        models.db_session.commit()
        return ""


@app.route('/get_all_books')
def get_all_books():
    # books = models.db_session.query(models.Item).all()
    books = models.Item.query.all()
    print books
    return jsonify({"items": ItemsSerializer(books, many=True).data})
    # return Response([i.json for i in books], mimetype='application/json')


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