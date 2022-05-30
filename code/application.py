from flask import Flask,render_template,flash, request, url_for
from google.cloud import automl
from google.api_core.client_options import ClientOptions
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/rafael_domin6uez/text-classification/bsa-project-349122-b9ce7ae16ab8.json"

def predict(content):
        project_id = "bsa-project-349122"
        model_id = "TCN4652416327166722048"
        options = ClientOptions(api_endpoint='eu-automl.googleapis.com')
        prediction_client = automl.PredictionServiceClient.from_service_account_json("bsa-project-349122-b9ce7ae16ab8.json", client_options=options)
        model_full_id = automl.AutoMlClient.model_path(project_id,'eu',model_id)
        text_snippet = automl.TextSnippet(content=content,mime_type='text/')
        payload = automl.ExamplePayload(text_snippet=text_snippet)
        response = prediction_client.predict(name=model_full_id, payload=payload)
        # print(response)
        return response.payload

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        content = request.form.get("text_to_analyze")
        response = predict(content)
        # print(response)
        return render_template("result.html", data=response, result=content)
    if request.method == 'GET':
        return "<h3> nothing to show </h3>"
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",8080)),host='0.0.0.0',debug=True)