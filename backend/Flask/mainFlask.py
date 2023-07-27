from flask import Flask, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

print('Flask app created!')
########### SQL CONNECTION ###########

# Connection
print('checking database')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pollancre@localhost/stats1'
print('succeed!')
db = SQLAlchemy(app)

# Database definition

class Data(db.Model):
    __tablename__ = 'embassaments_data'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.DateTime)
    station = db.Column(db.String(120))
    absolut_volume = db.Column(db.Float)
    stored_volume_pct = db.Column(db.Float)
    stored_volume_hm3 = db.Column(db.Float)

############## VIEW ROUTES #############

@app.route('/')
def root_view():
    return '<a href="/data"><button> Go to data </button></a>'

@app.route('/data')
def data_view():
    data = Data.query.all()
    return render_template('data.html', data = data)


######## CROS ORIGIN RESOURCE SHARING #########

CORS(app)


# Ensures that the app is run only when the script is executed directly (not imported as a module) and starts the dev server with debug mode enabled
if __name__ == '__main__':
    app.run(debug=True)

