from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__, static_url_path='')

user_list = []

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route('/search', methods=['GET'])
def search_items():

    # Retrieve parameters from the URL
    # keyword = request.args.get('keywords')
    # entries_per_page = request.args.get('paginationInput.entriesPerPage')
    # max_price = request.args.get('itemFilter(0).value')

    # You can perform further processing with these parameters
    # For now, let's just return them as a JSON response
    # response_data = {
    #     'keyword': keyword,
    #     'entries_per_page': entries_per_page,
    #     'max_price': max_price
    # }

    result = requests.get("https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsAdvanced&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=ChiTingH-firstApp-PRD-672bbdc3d-c7a8127b&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&keywords=iphone&paginationInput.entriesPerPage=10&sortOrder=BestMatch&itemFilter(0).name=MaxPrice&itemFilter(0).value=25&itemFilter(0).paramName=Currency&itemFilter(0).paramValue=USD")
    # print(result.json())
    #get_json_data = json.loads(trending_movies.text)
    # response_data = {'message' : 'Hello, API'}
    response_data = result.json()
    return response_data

# @app.route('/user/<string:username>', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def user(username):
#     if request.method == 'GET':
#         for user in user_list:
#             if user['username'] == username:
#                 return jsonify(user)
#         return jsonify({'username': None}), 404

#     elif request.method == 'POST':
#         user_data = {
#             'username': username,
#             'email': request.get_json().get('email')
#         }
#         user_list.append(user_data)
#         return jsonify(user_data), 201

#     elif request.method == 'PUT':
#         for user in user_list:
#             if user['username'] == username:
#                 user['email'] = request.get_json().get('email')
#                 return jsonify(user)
#         return jsonify({'message': 'User not found'}), 404

#     elif request.method == 'DELETE':
#         for ind, user in enumerate(user_list):
#             if user['username'] == username:
#                 deleted_user = user_list.pop(ind)
#                 return jsonify({'message': 'Successfully deleted'})
#         return jsonify({'message': 'User not found'}), 404

# @app.route('/users', methods=['GET'])
# def user_list_route():
#     return jsonify({'user_list': user_list})

if __name__ == "__main__":
    app.run()
