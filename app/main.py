'''
@module: API framework
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/leomaurodesenv/data-science-api-framework GitHub
@license: MIT License
@copyright: 2020 Leonardo Mauro
@access: public
'''

#-- Imports
import flask
import api
from flask import request, jsonify

#-- API predefinitions
app = flask.Flask('ds-api')
app.config['DEBUG'] = False
app.config['ENV'] = 'production'
api.init()


#-- Home page
@app.route('/')
def home():
    return "<h2>Data Science API Framework</h2>\
    <p>This API is running - <a href=\"http://{0}/api/\">http://{0}/api/</a>.</p>".format(request.host)


#-- API url
@app.route('/api/', methods=['GET'])
def apiRun():
    response = api.run(request.args)
    return jsonify(response)


#-- Publishing app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)