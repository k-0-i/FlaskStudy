from flask import Blueprint

scanner_bp = Blueprint('scanner',__name__,template_folder='templates')

from app.scanner import routes