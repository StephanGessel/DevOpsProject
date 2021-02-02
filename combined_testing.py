from backend_testing import post_test, get_test
from frontend_testing import front_test
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

if __name__ == '__main__':
    combined_test('543', 'Jamie')
