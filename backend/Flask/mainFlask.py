from flask import Flask, render_template, jsonify
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
    return render_template('main.html')

@app.route('/data')
def data_view():
    data = Data.query.all()
    return render_template('data.html', data = data)

@app.route('/api/data')
def api_data():
    data = Data.query.all()

    # Convert SQLAlchemy instances to dictionaries
    data_list = []
    for item in data:
        data_dict = {
            'id': item.id,
            'day': item.day,
            'station': item.station,
            'absolut_volume': item.absolut_volume,
            'stored_volume_pct': item.stored_volume_pct,
            'stored_volume_hm3': item.stored_volume_hm3
        }
        data_list.append(data_dict)

    # Return the data list as JSON
    return jsonify(data_list)



######## CROS ORIGIN RESOURCE SHARING #########

CORS(app)


# Ensures that the app is run only when the script is executed directly (not imported as a module) and starts the dev server with debug mode enabled
if __name__ == '__main__':
    app.run(debug=True)

