#!/usr/bin/env python

from app import app
from database import init_db

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
