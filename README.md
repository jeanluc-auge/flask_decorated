# FLASK DECORATED with meta programming

- automates the creation of Flask endpoints
- alternative to jinja templating

**This is the full version with code inspection**

With the following modules:
- Flask server with meta programming in flask_restplus_server.py 
- The macros functions are implemented in macros.py
- The definition of endpoints and macros to expose in cep.py
- The code inspection to build the data model in generate_endpoints.py

Automates the creation of Flask endpoints in a dynamic way with meta programming:
- build data model with code inspection
- dynamic class creation with *type*
- dynamic decoration of class with Flask decorators

## use
pip3 install -rrequirements.txt
python3 python3 flask_restplus_server.py

You can add or remove macros to expose in cep.py
