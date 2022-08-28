from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Ticket:
  def __init__(self, data):
    self.id_ticket = data['id_ticket']
    self.type_service_ticket = data['type_service_ticket']
    self.status_ticket = data['status_ticket']
    self.id_office = data['id_office']
    self.id_client = data['id_client']

  @classmethod
  def get_tickets_by_office(cls):
    query = """SELECT C.name_city, D.name_district, O.name_office, COUNT(T.id_office) FROM tb_ticket AS T
                INNER JOIN tb_office O ON T.id_office = O.id_office
                INNER JOIN tb_district D ON O.id_district = D.id_district
                INNER JOIN tb_city C ON D.id_city = C.id_city
                GROUP BY O.id_office;"""
    results = connectToMySQL('db_hackathon').query_db(query)
    print(results)
    return results