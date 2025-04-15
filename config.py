import os  # ✅ Required for path handling

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@host.docker.internal:5433/ecommerce'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost:5433/ecommerce
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecretkey'
    UPLOAD_FOLDER = os.path.join(basedir, 'static/uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
