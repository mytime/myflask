CSRF_ENABLED = True
SECRET_KEY = 'mysecretkeyisnotquessit'

import os
base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir,'app.db')
