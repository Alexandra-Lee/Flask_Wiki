import datetime

from app.main import db
from app.main.model.article import Article


def save_new_article(data):
    article = Article.query.filter_by(title=data['title']).first()
    if not article:
        new_article = Article(
            title=data['title'],
            author=data['author'],
            written_date=data['written_date'],
            content=data['content'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_article)
        response_object = {
            'status': 'success',
            'message': 'Successfully submitted.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Article has not been submitted. Please Log in.',
        }
        return response_object, 409

def get_all_articles():
    return Article.query.all()

def get_article(id):
    return Article.query.filter_by(id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
