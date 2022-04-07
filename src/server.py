from flask import Flask, request, jsonify
from ipca import Ipca
from invalid_date import InvalidDate

class Server:
    def __init__(self, name):
        self.app = Flask(name)

        self.ipca_data = Ipca()

        @self.app.route('/')
        def __index():
            return self.index()

        @self.app.route('/ipca', methods=['GET'])
        def __ipca():
            return self.ipca()

        @self.app.errorhandler(InvalidDate)
        def __handle_invalid_date(error):
            response = jsonify(error.to_dict())
            response.status_code = error.status_code
            return response

    def index(self):
        return """
        'Usage: localhost/ipca?start-date={}$end-date={}'
         Date format: dd-mm-yyyy
        """

    def ipca(self):
        
        args = request.args
        start_date = args['start-date']
        end_date = args['end-date']
        accumulated_tax = self.ipca_data.accumulated_tax(start_date=start_date, end_date=end_date) 
        return jsonify(accumulated_tax) 

    def run(self, host, port):
        self.app.run(host=host, port=port)
