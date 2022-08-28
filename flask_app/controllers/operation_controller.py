from flask import request, jsonify
from flask_app import app 

from flask_app.models.operation_model import Operation
from flask_app.models.office_model import Office 

@app.route("/api/")
def get_all_operations():
  operations = Operation.get_operations()
  return jsonify(operations)

@app.route("/api/<int:id>")
def get_operation(id):

  data_operation = {
      "id": id
    }
  operation = Operation.get_operations_by_id(data_operation)

  return jsonify(operation)


# @app.route("/api/office")
# def Get_All_Office_By_Operations():
#   offices = Office.get_all_offices_by_locations()
#   return jsonify(offices)




