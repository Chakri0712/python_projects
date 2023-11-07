import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ilovepdf.com/")
driver.maximize_window()
text = driver.find_element(By.XPATH, "//h1").text

try:
    assert text == "Every tool you need to work with PDFs in one place", "Text does not match the expected value"
except AssertionError as e:
    print("Exception:", e)

driver.find_element(By.XPATH, "//a[text()='Login']").click()
driver.find_element(By.XPATH, "//a[@id='goRegister']").click()

# We can just use keys method and enter our required text while filling the forms
element = driver.find_element(By.XPATH, "//input[@id='name']")
element.send_keys("chakra", Keys.TAB, "chakra@gmail.com", Keys.TAB, "chakra123@!")

# driver.find_element(By.XPATH, "//input[@id='signupEmail']").send_keys("chakra@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='password']").send_keys("chakra123@!")
driver.find_element(By.XPATH, "//button[@id='registerButton']").click()

error_txt = driver.find_element(By.CSS_SELECTOR, ".field-signupEmail  .help-block").text
print(error_txt)

try:
    if error_txt == "This email address has already been taken.":
        driver.find_element(By.ID, "goLogin").click()
except Exception as e:
    print(e)

driver.find_element(By.NAME, "LoginForm[email]").send_keys("chakra@gmail.com")
driver.find_element(By.NAME, "LoginForm[password]").send_keys("chakra123@!")
driver.find_element(By.ID, "loginBtn").click()

# Keep the browser open for n seconds
time.sleep(5)

# Add this line to prevent the browser from closing immediately
input("Press Enter to close the browser")
