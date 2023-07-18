from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class TestSomething():
    def test_title(self):
        options = webdriver.ChromeOptions()
        driver =  webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            options=options,
        )

        driver.get('https://www.julo.co.id/')
        assert 'Aplikasi Kredit Digital Cepat Cair dan Aman | Julo' in driver.title
        
        time.sleep(400)
        driver.quit()
