import rumps
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SpeedIndicatorApp(rumps.App):
    def __init__(self):
        super(SpeedIndicatorApp, self).__init__("...kmh")
        self.speed = "Loading..."
        self.error = ""
        self.menu = [self.speed]
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://iceportal.de/")
        self.timer = rumps.Timer(self.update_speed, 5)
        self.timer.start()

    def update_speed(self, sender):
        try:
            speed_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "traininfoIntro-speedIndicatorText"))
            )
            speed = speed_element.text.strip()
            self.speed = speed
            self.error = ""
        except Exception as e:
            self.speed = ""
            self.error = f"Error: {str(e)}"
            print(f"Error: {str(e)}")
        self.title = f"{self.speed} {self.error}"

if __name__ == "__main__":
    SpeedIndicatorApp().run()