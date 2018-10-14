from .. import db
import datetime
class Article(db.Model):
    """ Article Model for storing article text """
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(30), nullable=False)
    written_date = db.Column(db.DateTime, nullable=True)
    content = db.Column(db.Text, nullable=False)    
    registered_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)      

    def __init__(self):
        self.articles = []

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
        
    def __repr__(self):
        return "<Article '{}'>".format(self.id, self.title, self.author, self.written_date, 
        self.content, self.registered_on)
