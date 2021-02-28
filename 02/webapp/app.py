from flask import Flask, request
from flask_restful import Resource, Api
import logging



app = Flask(__name__)
api = Api(app)


class Search(Resource):
    def get(self):
        msg = request.args.get('message')
        if not msg:
            return ""
        elif len(msg) > 1:
            count = 1
            tmp = ""
            msg_str = ""

            for idx,val in enumerate(msg):

              if tmp != val:
                  if count != 1:
                      msg_str = msg_str + str(count)

                  msg_str = msg_str + val
                  tmp = val
                  count = 1
              else:
                  count += 1
              if idx == len(msg)-1 and count != 1:
                  msg_str = msg_str + str(count)

            msg = msg_str

        return msg

if __name__ == '__main__':
    api.add_resource(Search, '/search/')
    logging.basicConfig(filename='webapp.log', level=logging.DEBUG)
    app.run(host="0.0.0.0", port=8080)

