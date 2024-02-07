"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# POST /member
@app.route('/member', methods=['POST'])
def add_member():
    request_body = request.json
    member = request_body

    jackson_family.add_member(member)
    
    return jsonify({"message": "Miembro agregado correctamente."}, request_body)

# GET /member/id
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)

    return jsonify({"message": "The member is"}, member)


# DELETE /member/id
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    jackson_family.delete_member(id)
    return({"message":"Miembro elimindado"})

# GET /members
@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()


    return jsonify(members), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)


# solution
#  ✗ The Family structure has to be initialized with the 3 members specified in the instructions
#  ✗ Implement method POST /member to add a new member
#  ✓ Method POST /member should return something, NOT EMPTY
#  ✓ Implement method GET /members
#  ✗ Method GET /members should return a list
#  ✗ We added two members using POST /member, when calling the GET /members should get a list of length == 5
#  ✗ Method GET /member/<int:id> should exist
#  ✗ Method GET /member/<int:id> should return a one single family member in a dictionary format
#  ✗ The dictionary returned by GET /member/<int:id> should contain one family member with the keys [name, id, age, lucky_numbers]
#  ✗ Method GET /member/3443 should return Tommy
#  ✗ Implement method DELETE /member/<int:id> to delete a family member
#  ✗ Method DELETE /member/3443 should return dictionary with 'done' key
#  ✗ After deleting the member 3443 we called GET /members and it should return a list with 4 members