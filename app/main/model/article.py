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
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self):
        self.title = title
        self.author = author
        self.written_date = written_date
        self.content = content
        self.registered_on = registered_on    

    def __repr__(self):
        return "<Article '{}'>".format(self.title, self.author, self.written_date, 
        self.content, self.registered_on)
