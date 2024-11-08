# from app.models import User
from flask_migrate import Migrate

from app import myapp, db

app = myapp()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
# from flask import Flask
#
# app = Flask(__name__)
# app.run()
