from flask import request
from flask_restplus import Resource

from ..apis.article_namespace import ArticleRes
from ..service.article_service import save_new_article, get_all_articles, get_article, delete_article, save_changes

api = ArticleRes.api
_article = ArticleRes.article


@api.route('/')
class ArticleList(Resource):
    @api.doc('list_of_submitted_articles')
    @api.marshal_list_with(_article, envelope='data')
    def get(self):
        """List all submitted articles"""
        return get_all_articles()

    @api.response(201, 'Article successfully submitted.')
    @api.doc('add a new article')
    @api.expect(_article, validate=True)
    def post(self):
        """Creates a new Article """
        data = request.json
        return save_new_article(data=data)

@api.route('/<int:id>')
@api.param('id', 'The Article identifier')
@api.response(404, 'Article not found.')
class Article(Resource):
    @api.doc('get article')
    @api.marshal_with(_article)
    def get(self, id):
        """get article given its identifier"""       
        article = get_article(id)
        if not article:
            api.abort(404)
        else:
            return article

    @api.doc('delete_article')
    @api.response(204, 'Article deleted')
    def delete(self, id):
        """Delete article given its identifier"""
        article.delete(id)
        return '', 204

    @api.expect(_article)
    @api.marshal_with(_article)
    def put(self, id):
        """Update article given its identifier"""
        return article.update(id, api.payload)
