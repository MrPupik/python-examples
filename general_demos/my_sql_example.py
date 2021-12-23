import pymysql.cursors
from TaxiStation.customer import Customer, CustomerType
from TaxiStation.recipts import ReciptType

connection = None


def connect():
    global connection
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='0000',
                                 database='my_schema',
                                 cursorclass=pymysql.cursors.DictCursor)


def disconnect():
    global connection
    connection.close()


def save_customer(cust: Customer):
    query = f"INSERT INTO customers (Type, num_of_pass, distance, recipt_type) values('{cust.type}', {cust.num_of_passengers}, {cust.distance},'{cust.recipt_type}')"
    _execute_query(query)


def _execute_query(query: str):
    global connection
    with connection.cursor() as cursor:
        # Create a new record
        cursor.execute(query)
        result = cursor.fetchone()
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    return result


def get_cutomer(id):

   # Read a single record
    sql = f"SELECT * from customers WHERE `id`={id}"
    return _execute_query(sql)


connect()
save_customer(Customer(CustomerType.buisness, 4, 14, ReciptType.TEXT))
disconnect()
