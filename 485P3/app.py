from flask import Flask, render_template

from extensions import mysql
import controllers
import api

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Initialize MySQL database connector
#app.config['MYSQL_USER'] = 'group36'
#app.config['MYSQL_PASSWORD'] = 'eeee517bcfeb456b9d21'
#app.config['MYSQL_DB'] = 'group36pa3'
#mysql.init_app(app)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'group36pa1'
mysql.init_app(app)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# Register the controllers
url_pre = '/eeee517bcfeb456b9d21/pa3'
app.register_blueprint(controllers.album, url_prefix=url_pre)
app.register_blueprint(controllers.albums, url_prefix=url_pre)
app.register_blueprint(controllers.pic, url_prefix=url_pre)
app.register_blueprint(controllers.main, url_prefix=url_pre)
app.register_blueprint(controllers.user, url_prefix=url_pre)
app.register_blueprint(controllers.login_bp, url_prefix=url_pre)
app.register_blueprint(api.user_api, url_prefix=url_pre)
app.register_blueprint(api.login_api, url_prefix=url_pre)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden(e):
	return render_template('403.html'), 403

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)
