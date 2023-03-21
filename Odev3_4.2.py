from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class TestSource:
    
    # Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
    def emptyUsernameAndPassword(self):
        
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(2)
        
        error = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        sleep(2)
        
        testResult = error.text == "Epic sadface: Username is required"
        return print(f"Test Result: {testResult}")
        
    # Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
    def emptyPassword(self):
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        
        userNAme = driver.find_element(By.ID, "user-name")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        
        userNAme.send_keys("standart_user")
        sleep(2)
        
        loginButton.click()
        sleep(2)
        
        error = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        sleep(2)
        
        testResult = error.text == "Epic sadface: Password is required"
        return print(f"Test Result: {testResult}")
        
    # Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
    def lockedOut(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        
        userNAme = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        
        userNAme.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        sleep(2)
        
        loginButton.click()
        sleep(2)
        
        error = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        sleep(2)
        
        testResult = error.text == "Epic sadface: Sorry, this user has been locked out."
        return print(f"Test Result: {testResult}")
    
    # Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
    # Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
    def blankIconX(self):
        situation1 = False
        situation2 = True
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        
        searchBox = driver.find_element(By.ID,"user-name")
        searchBox.clear()
        searchBox = driver.find_element(By.ID,"password")
        searchBox.clear()
        driver.find_element(By.ID,"login-button").click()
        sleep(2)
        
        
        icon1 = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        situation1 = str(icon1.size)=="{'height': 18, 'width': 18}"
        icon2 = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        situation1=str(icon2.size)=="{'height': 18, 'width': 18}"
        driver.find_element(By.CLASS_NAME,"error-button").click()
        sleep(2)
        
        try:
            icon1 = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
            if(str(icon1.size)=="{'height': 18, 'width': 18}"):
                situation2= False
        except Exception:
            pass
        try:
            icon2 = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
            if(str(icon2.size)=="{'height': 18, 'width': 18}"):
                situation2= False
        except Exception:
            pass
        print(f"Blank Icon X Situation 1 Test Result: {situation1}, \nBlank Icon X Situation 2 Test Result: {situation2}")
    
    # Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
    def inventoryHtml(self):
        situation = False
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        
        userNAme = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        loginButton = driver.find_element(By.ID, "login-button")
        sleep(2)
        
        userNAme.send_keys("standart_user")
        password.send_keys("secret_sauce")
        sleep(2)
        
        loginButton.click()
        sleep(2)
        
        if(driver.current_url=="https://www.saucedemo.com/inventory.html"):
            situation=True
        print(f"Standard User Inventory Test Result: {situation}")
        
    # Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
    def numberOfProducts(self):
        situation = False
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        
        user_name = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        login_btn = driver.find_element(By.ID,"login-button")
        sleep(2)
        
        user_name.send_keys("problem_user")
        password.send_keys("secret_sauce")
        sleep(2)
        
        login_btn.click()
        sleep(2)
        
        products = driver.find_elements(By.CLASS_NAME,"inventory_item")
        
        if(len(products)==6):
            situation = True
            print(f"Number of Items Test Result: {situation}") 




testClass = TestSource()
testClass.emptyUsernameAndPassword()
testClass.emptyPassword()
testClass.lockedOut()
testClass.blankIconX()
testClass.inventoryHtml()
testClass.numberOfProducts()