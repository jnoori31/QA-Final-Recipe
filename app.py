from application import app

# Check basic setup is complete and server is responding
# @app.route('/')
# def hello_internet():
#     return "Hello Internet!"
# Jenkins webhook test
# Jenkins webhook test 2
if __name__=='__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)