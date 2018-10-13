from flask_restplus import Api
# from flask import Blueprint

from ..controller.user_controller import api as user_ns
from ..controller.article_controller import api as article_ns
from ..controller.auth_controller import api as auth_ns

# blueprint = Blueprint('api', __name__)

api = Api(
          title='Alexandra\'s FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='This is a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(article_ns, path='/article')
api.add_namespace(auth_ns)