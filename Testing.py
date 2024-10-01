import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
import multiprocessing as multiprocess

username_field_names = ['login', 'username', 'login_field', 'user', 'user_name']
password_field_names = ['password', 'pass', 'passwd', 'password_field']

def logIn(username, password,url,user_name_id,password_id,queue):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(executable_path="F:/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(5)
    try:
        username_field = driver.find_element(By.)

# def setUp():
    # driver = webdriver.Chrome()
    # driver.get('https://github.com/login')
    # driver.maximize_window()
    # time.sleep(5) # Let the user actually see something!
    # def login():
    #     try:
            # username = "BhavaniKrishna0011"
            # email = "sumith143@gmail.com"
            # password = "Dotan@110714458"
    #         username_field = driver.find_element(By.ID,'login_field')
    #         username_field.send_keys(username)
    #         time.sleep(1)
    #         # email_field = driver.find_element(By.ID,'email')
    #         # email_field.send_keys(email)
    #         # time.sleep(1)        
    #         password_field = driver.find_element(By.ID,'password')
    #         password_field.send_keys(password)
    #         time.sleep(1)
    #         submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    #         submit_button.click()
    #         success_element = driver.find_element(By.ID,"")
    #         time.sleep(2)
    #         time.sleep(5) # Let the user actually see something!   
    # login()
    # driver.quit()

# setUp()