from flask_restplus import Namespace, Resource, fields


class ArticleRes:
    api = Namespace('article', description='article related operations')
    article = api.model('article', {
        'title': fields.String(required=True, description='title of article'),
        'author': fields.String(required=True, description='author of article'),
        'written_date': fields.DateTime(dt_format='rfc822', required=False, description='date article was written'),
        'content': fields.String(required=True, description='the text of article'),
        'registered_on': fields.DateTime(dt_format='rfc822', description='date article submitted on wiki'),
    })