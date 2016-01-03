import BaseHTTPServer
import json
from model import generate_model
from diagnose import diagnose_from_keywords

HOST_NAME = 'localhost'
PORT_NUMBER = 8000
DICTIONARY_PATH = 'short-diagnoses.txt'

# Create a wrapper for the request handler in order to pass some
# initialization arguments.
def WrapRequestHandler(diagnosis_model, diagnosis_dictionary):
  class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(request):
      varLen = int(request.headers.get('Content-Length'))
      search_keywords = request.rfile.read(varLen);

      response_code = 200
      top_ten_diagnoses_response = diagnose_from_keywords(diagnosis_model, diagnosis_dictionary, search_keywords)

      request.send_response(response_code)
      request.send_header("Content-type", "application/json")
      request.send_header("Access-Control-Allow-Origin", "*")
      request.end_headers()
      if top_ten_diagnoses_response:
        request.wfile.write(json.dumps(top_ten_diagnoses_response))
      return

  return RequestHandler


if __name__ == '__main__':
  # The model is generated on the server before it starts running the service.
  #
  # Note: Model generation would normally happen in a completely separate
  #       environment than the webserver.
  diagnosis_dictionary =  open(DICTIONARY_PATH).read().splitlines()
  diagnosis_model = generate_model(diagnosis_dictionary)

  server_class = BaseHTTPServer.HTTPServer;
  HandlerClass = WrapRequestHandler(diagnosis_model, diagnosis_dictionary)
  httpd = server_class((HOST_NAME, PORT_NUMBER), HandlerClass)

  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  else:
    print "Unexpected server exception occurred."
  finally:
    httpd.server_close()
