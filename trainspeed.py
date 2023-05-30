import rumps
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SpeedIndicatorApp(rumps.App):
    def __init__(self):
        super(SpeedIndicatorApp, self).__init__("...km/h")
        self.speed = "Loading..."
        self.error = ""
        self.menu = [self.speed]
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # use headless browser
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://iceportal.de/")
        self.timer = rumps.Timer(self.update_speed, 0.5)  # update speed more often
        self.timer.start()

    def update_speed(self, sender):
        try:
            speed_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "traininfoIntro-speedIndicatorText"))
            )
            speed = speed_element.text.strip()
            if speed != self.speed:  # only update menu if speed has changed
                self.speed = speed
                self.error = ""
                self.menu.clear()
                self.menu.add(self.speed)
        except Exception as e:
            self.speed = ""
            self.error = f"Error: {str(e)}"
            print(f"Error: {str(e)}")
        self.title = f"{self.speed} {self.error}"

if __name__ == "__main__":
    SpeedIndicatorApp().run()