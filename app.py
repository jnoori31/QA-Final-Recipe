from application import app

# Check basic setup is complete and server is responding
# @app.route('/')
# def hello_internet():
#     return "Hello Internet!"
# Jenkins webhook test
# Jenkins webhook test 2
# Docker swarm sever log in and github webhook test 3
#Jenkins Webhook test 4
if __name__=='__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)