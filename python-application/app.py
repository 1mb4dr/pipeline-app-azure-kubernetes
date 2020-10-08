from flask import Flask
import epsagon

epsagon.init(
    token='f41b1713-e48b-4685-a88b-34db5b3b0c55',
    app_name='pipeline-azure-aks',
    metadata_only=False
)

app = Flask(__name__)
epsagon.flask_wrapper(app)

@app.route('/')
def hello():
    return "Stay inside, stay safe and keep social distancing."

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    app.run(host='0.0.0.0') 
