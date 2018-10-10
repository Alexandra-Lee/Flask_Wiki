from flask import Flask
# from .main.apis import blueprint as api
from .main.apis import api
from .main import create_app

app = create_app('dev')
# app.register_blueprint(api, url_prefix='/api')
api.init_app(app)

app.run(debug=True)