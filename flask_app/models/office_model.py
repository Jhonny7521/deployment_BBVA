from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Office:
  def __init__(self, data):
    self.id_office = data['id_office']
    self.name_office = data['name_office']
    self.capacity_number = data['capacity_number']
    self.id_district = data['id_district']
    self.name_district = data['name_district']
    self.latitud_office = data['latitud_office']
    self.longitud_office = data['longitud_office']
    self.id_city = data['id_city']
    self.name_city = data['name_city']

  @classmethod
  def get_all_offices(cls):
    query = "SELECT C.name_city, D.name_district, O.name_office, O.capacity_number FROM tb_city AS C INNER JOIN tb_district D ON C.id_city = D.id_city INNER JOIN tb_office O ON D.id_district = O.id_district;"
    results = connectToMySQL('db_hackathon').query_db(query)
    print('---------')
    print(results)
    print('---------')
    return results

  @classmethod
  def get_all_offices_by_locations(cls):
    query = "SELECT O.id_office, o.name_office, o.latitud_office, o.longitud_office ,d.id_district, d.name_district, c.id_city, c.name_city FROM tb_office as O INNER JOIN tb_district D ON O.id_district = D.id_district INNER JOIN tb_city C ON D.id_city = C.id_city;"
    results = connectToMySQL('db_hackathon').query_db(query)
    print('---------')
    print(results)
    print('---------')
    return results

