#!/usr/bin/env python
from app import app

app.run(
    host=app.config.get('HOST'),
    port=app.config.get('PORT'),
    debug=app.config.get('DEBUG')
)
