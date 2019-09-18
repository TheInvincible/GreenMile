def create_app(config_name):
    
    from green import models

    from .admins import admins as admins_blueprint
    app.register_blueprint(admins_blueprint, url_prefix='/admin')

    from .authent import authent as authent_blueprint
    app.register_blueprint(authent_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app