from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.rokomari.com/book")

driver.find_element_by_id("js--search").send_keys("programming")
driver.find_element_by_xpath("//button[@class='btn']").submit()

# select first book
time.sleep(5)
driver.find_element_by_xpath("//div[@class='col-4 col-xl-3']/div/a").click()

driver.find_element_by_xpath("//a[@class='btn details-cart-btn js--add-to-cart js--add-to-cart-desc']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='js--details-btn-area']/a[2]").click()  # go to cart
driver.find_element_by_xpath("//a[@class='btn cart-btn shipping-btn']").click()  # go to shiping page

# Submit form
driver.find_element_by_id("name").send_keys("ikhtiar")
driver.find_element_by_id("phone").send_keys("01521201837")
driver.find_element_by_xpath("//select[@id='js--country']/option[text()='বাংলাদেশ']").click()
driver.find_element_by_xpath("//select[@id='js--city']/option[text()='ঢাকা']").click()
time.sleep(3)
driver.find_element_by_xpath("//select[@id='js--area']/option[text()='আদাবর']").click()
driver.find_element_by_id("email").send_keys("ikhtiar6124@gmail.com")
driver.find_element_by_id("address").send_keys("70, khaje dewan, Lalbagh, dhaka-1211")

driver.find_element_by_xpath("//button[@id='js--continue-to-payment']").click()
time.sleep(3)
driver.find_element_by_css_selector("label[for='cod']").click()
time.sleep(3)
driver.find_element_by_xpath("//a[@class='btn payment-btn']").click()
time.sleep(10)
driver.close()