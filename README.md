# FLASK DECORATED with meta programming

- automates the creation of Flask endpoints
- alternative to jinja templating

**This is the manual simple version**

With the following modules:
- Flask server with meta programming in flask_restplus_server.py
- The macros functions are implemented in macros.py
- The definition of endpoints and macros to expose in cep.py
 
automates the creation of Flask endpoints in a dynamic way with meta programming:
- dynamic class creation with *type*
- dynamic decoration of class with Flask decorators

## use
pip3 install -rrequirements.txt
python3 python3 flask_restplus_server.py
