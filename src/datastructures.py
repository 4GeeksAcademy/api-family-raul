
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
    # {
    #     "name": "John Jackson",
    #     "age": 33,
    #     "lucky_numbers": [7, 13, 22]
    # },
    # {
    #     "name": "Jane Jackson",
    #     "age": 35,
    #     "lucky_numbers": [10, 14, 3]
    # },
    # {
    #     "name": "Jimmy Jackson",
    #     "age": 5,
    #     "lucky_numbers": [1]
    # }
]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member or not member["id"]:
            member["id"] = self._generateId()

            self._members.append(member)

    def delete_member(self, id):
        self._members = [ member for member in self._members if member["id"] != id]

    def get_member(self, id):
        show_member = [ member for member in self._members if member["id"] == id]

        return show_member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members



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