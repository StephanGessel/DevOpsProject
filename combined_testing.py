import backend_testing
import frontend_testing
import db_connector

def combined_test(id, name):

    try:
        backend_testing.post_test(id, name)
        backend_testing.get_test(id)
        db_connector.get_table()
        frontend_testing.front_test(id)

    except Exception as e:
        print("Combined test failed")
        print(e)


# print('COMBINED TESTING')
# print('##############')
id = input('Enter ID: ')
name = input('Enter Name: ')
combined_test(id, name)
