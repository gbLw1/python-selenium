# Python selenium test

## Description

The project is a automation for the game [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) using the selenium library.

## Requirements

- [Selenium](https://pypi.org/project/selenium/)
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable)

## How to run

Add the path to the chromedriver in the `main.py` file.

ps: If you are using Windows, you need to add the `.exe` extension to the path, you can put the chromedriver in the same directory as the project and use the following code:

```python
driver = webdriver.Chrome(executable_path="path/to/chromedriver")
```

Then run the following command:

```bash
python main.py
```

## Deploy

When deploying web scraping applications, it is important to consider using a headless browser to avoid issues like IP blocking and CAPTCHA, it is recommended to use a proxy service like [Bright Data](https://brightdata.com/).
