#app/routes/main_routes.py

from flask import Blueprint, render_template_string

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Bem-vindo</title>
        </head>
        <body>
            <h1>Bem-vindo à API!</h1>
            <p>Esta é uma página de saudação.</p>
        </body>
        </html>
    """)
