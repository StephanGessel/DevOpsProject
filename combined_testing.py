from backend_testing import *
from frontend_testing import *
import db_connector

def combined_test(id, name):

    try:
        post_test(id, name)
        get_test(id)
        db_connector.get_table()
        front_test(id)

    except Exception as e:
        print("Combined test failed")
        print(e)

combined_test('543', 'Jamie')
