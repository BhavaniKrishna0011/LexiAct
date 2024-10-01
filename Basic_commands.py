import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
import multiprocessing as mp
import sqlite3 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the list of potential field names
username_field_names = ['login', 'username', 'login_field', 'user', 'user_name']
password_field_names = ['password', 'pass', 'passwd', 'password_field']

# Function to perform login
def attempt_login(url, username, password, username_field_name, password_field_name, queue):
    # Initialize headless Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Create a Service object for the ChromeDriver
    service = Service(executable_path="F:/chromedriver_win32/chromedriver.exe")  # Adjust the path accordingly

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(url)  # Replace with your login URL
        # Wait until the page is loaded
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Try to find the username field and enter the username
        for _ in range(3):  # Retry up to 3 times
            # try:
                username_field = driver.find_element(By.NAME, username_field_name)
                username_field.send_keys(username)
                break
            # except (NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException):
            #     time.sleep(1)  # Small wait before retrying
        
        # Try to find the password field and enter the password
        for _ in range(3):  # Retry up to 3 times
            # try:
                password_field = driver.find_element(By.NAME, password_field_name)
                password_field.send_keys(password)
                break
            # except (NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException):
            #     time.sleep(1)  # Small wait before retrying
        
        # Submit the form
        for _ in range(3):  # Retry up to 3 times
            try:
                submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
                submit_button.click()
                time.sleep(3)  # Wait for the page to load after submission
                break
            except (NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException):
                time.sleep(1)  # Small wait before retrying

        # Check if login was successful
        for _ in range(3):  # Retry up to 3 times
            # try:
                if driver.find_element(By.ID, "main_page"):  # Check for the main_page element
                    queue.put(("Success", username_field_name, password_field_name))
                    return  # Return after success
            # except (NoSuchElementException, StaleElementReferenceException):
            #     time.sleep(1)  # Small wait before retrying
        queue.put(("Fail", username_field_name, password_field_name))  # If not successful

    except Exception as e:
        queue.put(("Error", str(e)))
    finally:
        driver.quit()

# Function to save login information in the database if successful
def save_login_info(db_file, url, username_id, password_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Insert the login information into the table
    cursor.execute('''
        INSERT INTO login_credentials (url, username_id, password_id)
        VALUES (?, ?, ?)
    ''', (url, username_id, password_id))
    
    conn.commit()  # Commit the changes
    conn.close()

# Main function to run multiple login attempts
def main():
    db_file = 'login_info.db'  # Database file
    username = "BhavaniKrishna0011"
    password = "Dotan@110714458"
    # url = 'http://127.0.0.1:5500/Loginpage_testing.html'
    url = "https://github.com/login"

    processes = []
    queue = mp.Queue()

    # Create a process for each combination of username and password field names
    for uname_field in username_field_names:
        for pass_field in password_field_names:
            p = mp.Process(target=attempt_login, args=(url, username, password, uname_field, pass_field, queue))
            processes.append(p)
            p.start()

    # Wait for the results
    for _ in processes:
        result = queue.get()  # Get results from the queue
        if result[0] == "Success":
            print("Login successful!")
            save_login_info(db_file, url, result[1], result[2])  # Save login info only on success
            print("Login information saved to database.")
            break  # Exit the loop on success
        else:
            print(result)

    # Terminate all processes
    for p in processes:
        p.join()

if __name__ == '__main__':
    main()
