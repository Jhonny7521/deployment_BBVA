from flask import request, jsonify
from flask_app import app
from flask_app.models.office_model import Office
from flask_app.models.tickets_model import Ticket 

@app.route("/api/office")
def get_offices():
  offices = Office.get_all_offices()
  return jsonify(offices)

@app.route("/api/office/tickets")
def get_tickets_offices():
  tickets = Ticket.get_tickets_by_office()
  return jsonify(tickets)

@app.route("/api/office/location")
def Get_Offices_By_Locations():
  offices = Office.get_all_offices_by_locations()
  return jsonify(offices)

# @app.route("/api/<int:id>")
# def get_operation(id):

#   data_operation = {
#       "id": id
#     }
#   operation = Operation.get_operations_by_id(data_operation)

#   return jsonify(operation)