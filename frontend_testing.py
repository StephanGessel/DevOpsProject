import time
from selenium import webdriver


def front_test(id):
    try:

        # Start Selenium Web Driver Session
        driver = webdriver.Chrome(executable_path="/users/sgessel/Downloads/chromedriver")
        driver.get(f"http://127.0.0.1:5001/users/get_user_data/{id}")

        print(driver.find_element_by_id("user").text)

    except Exception as e:
        print('Test failed')
        print(e)

    finally:
        time.sleep(2)
        driver.quit()