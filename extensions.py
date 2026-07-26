from flask_mysqldb import MySQL

# Standard Flask "extensions module" pattern for avoiding circular imports; instantiate extensions here without an app so blueprints can import them without importing app.py,
# which would cause circular imports
mysql = MySQL()
