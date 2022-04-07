class InvalidDate(Exception):
    def __init__(self, message, name):
        Exception.__init__(self)
        self.messsage = message
        self.status_code = 400
        self.payload = {
            "code": 404,
            "name": name,
            "message": message
        }

    def to_dict(self):
        rv = dict(self.payload or ())
        return rv
       