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

    def __repr__(self):
        return "<Article '{}'>".format(self.id, self.title, self.author, self.written_date, 
        self.content, self.registered_on)
