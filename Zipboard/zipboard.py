from selenium import webdriver
import time


class Zipboard():
    def __init__(self, email, username, password):
        self.email = email
        self.password = password
        self.username = username
        # self.driver = webdriver.Chrome('./chromedriver')
        self.driver = webdriver.Firefox()

    def homepage(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://zipboard.co/")
        print(driver.title)

    def sign_up(self):
        driver = self.driver
        time.sleep(3)
        sign_up_button = driver.find_element_by_xpath(
            "//a[contains(text(),'Sign up Free')]")
        sign_up_button.click()

    def create_account(self):
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_xpath(
            "//span[@id='signup-link']").click()

    def account_form(self):
        driver = self.driver
        time.sleep(5)
        email = driver.find_element_by_xpath("//input[@id='email']")
        time.sleep(2)
        email.send_keys(self.email)
        username = driver.find_element_by_xpath("//input[@id='name']")
        username.send_keys(self.username)
        password = driver.find_element_by_xpath("//input[@id='password']")
        password.send_keys(self.password)
        time.sleep(3)
        button = driver.find_element_by_xpath(
            "//body/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/form[1]/div[2]/input[1]")
        time.sleep(2)
        button.click()

    def login_to(self):
        time.sleep(3)
        driver = self.driver
        login_button = driver.find_element_by_xpath(
            "//a[contains(text(),'Login')]")
        login_button.click()

    def login_form(self):
        driver = self.driver
        time.sleep(3)
        username = driver.find_element_by_xpath(
            "//input[@id='login-username']")
        username.send_keys(self.username)
        password = driver.find_element_by_xpath(
            "//input[@id='login-password']")
        password.send_keys(self.password)
        time.sleep(3)
        submit = driver.find_element_by_xpath("//input[@type='submit']")
        submit.click()


if __name__ == "__main__":
    print("Starting the script....")
    print("Choose action login or signup....")
    credentials = input("Please enter the operation......    ")
    email = input("Enter the email...  ")
    username = input("Enter the username..  ")
    password = input("Enter the password... ")
    print("starting script...")

    if credentials == "login":
        zip = Zipboard(email, username, password)
        zip.homepage()
        zip.login_to()
        zip.login_form()

    elif credentials == "signup":
        zip = Zipboard(email, username, password)
        zip.homepage()
        zip.sign_up()
        zip.create_account()
        zip.account_form()
    else:
        print("not valid credentials..")
