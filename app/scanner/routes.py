from flask import render_template

from app.scanner import scanner_bp
from flask_login import login_required


@login_required
@scanner_bp.route('/')
def scanner():
    return render_template('scanner/scanner.html')