from flask import Flask

def create_app(test_config=None):
    # create and configure app as desired
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        ...
    )

    # check whether testing and for instance folder
    ...

    # importing and initializing other blueprints and views
    ...

    # import site blueprint, views, and functionality
    from . import site
    app.register_blueprint(site.bp)
    app.add_url_rule('/', endpoint='index')

    # Extensions
    # import cache functionality
    from .cache import cache
    cache.init_app(app)

    return app