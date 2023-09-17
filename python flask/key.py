from flask import 

def create_app ():
    app = flask (_name_)
    app.config ["secret key"] = "pdjj5646po"
    

    
    from . views import views 
    from .auth import auth 
    
    app . register_blueprint(views, url_prefix='/')
    app . register_blueprint(auth, url_prefix='/')
    return app 
    

