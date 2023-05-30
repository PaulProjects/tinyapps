# TinyApps

Small python scrips I write from time to time

## Preparation

- Install Python 3 from the official website: https://www.python.org/downloads/


## TrainSpeed - Mac only

TrainSpeed is a Python application that displays the current speed of a german ICE train using data from the ICE Portal website. The application uses the Selenium library to scrape the website and display the speed in the macOS menu bar.

### Dependencies

- Python 3
- rumps
- selenium
- ChromeDriver

### Installation

1. Install Python 3 from the official website: https://www.python.org/downloads/
2. Install the required Python packages by running the following command in your terminal: `pip install rumps selenium`
3. Download the [trainspeed.py](trainspeed.py) file
4. Download ChromeDriver from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads
5. Add the ChromeDriver executable to the same folder where you placed the [trainspeed.py](trainspeed.py) file

### Usage

1. Open a terminal and navigate to the directory where the `trainspeed.py` file is located.
2. Run the following command: `python trainspeed.py`
3. The application will start and display the current ICE speed in the macOS menu bar.

## License

This project is licensed under the Mozilla Public License Version 2.0 - see the [LICENSE](LICENSE) file for details.