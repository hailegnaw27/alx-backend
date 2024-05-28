#!/usr/bin/env python3
"""
This module contains a basic Flask application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> str:
    """
    The index route that renders an HTML template with a welcome message.

    Returns:
        str: The rendered HTML template as a string.
    """
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run()

