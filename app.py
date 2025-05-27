from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from api.db.database import init_db
from api.routes.routes import register_routes

app = Flask(__name__)
CORS(app)
Swagger(app)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  
app.config['MYSQL_DB'] = 'ferramas'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

init_db(app)
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
