from app import db, myapp
from app.models import User

app = myapp()
with app.app_context():
    user = User(username='st4rry')
    user.set_password('password')
    db.session.add(user)
    db.session.commit()
