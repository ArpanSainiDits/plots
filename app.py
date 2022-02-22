from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/plots'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

if __name__ == '__main__':
    app.run(debug=True)
