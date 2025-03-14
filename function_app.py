import azure.functions as func
import logging
import json
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="Configuration")
def Configuration(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    version = req.params.get('version')
    if not version:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            version = req_body.get('version')

    if version:
        newVersion =  os.getenv('BKEA_Version')
        response = {
                "version": newVersion,
                "backendUrl": os.getenv('BKEA_BackendUrl')        
        }
        
        return func.HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a version in the query string or in the request body to get a resposne.",
             status_code=200
        )