from flask import Flask

def create_app(config=None):
   app = Flask(__name__)
    
   if config is not None:
      app.config.update(config)
    
   from application.views.main_view import main_bp
   from application.views.result_view import result_bp

   app.register_blueprint(main_bp)
   app.register_blueprint(result_bp)

   return app

if __name__ == "__main__":
    app.run(debug=True)