import datetime

from app.main import db
from app.main.model.article import Article

def save_new_article(data):
    # counter = 0
    article = Article.query.filter_by(content=data['content']).first()
    if not article:
        if 'written_date' in data:
            new_article = Article(
                # id=counter + 1,
                title=data['title'],
                author=data['author'],
                written_date=data['written_date'],
                content=data['content'],
                registered_on=datetime.datetime.utcnow()
            )
        else:
            new_article = Article(
                # id=counter + 1,
                title=data['title'],
                author=data['author'],
                written_date=None,
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
            'message': 'Article has not been submitted.',
        }
        return response_object, 409

def get_all_articles():
        return Article.query.all()

def get_article(id):
    return Article.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def delete_article(self, title):
    article = self.get(title)
    self.articles.remove(article)     
