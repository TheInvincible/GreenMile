def create_app(config_name):
    
    from green import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .authent import auth as auth_blueprint
    app.register_blueprint(authent_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app