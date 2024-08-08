import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
driver = None #declaration of the driver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver #the driver is global in the entire file
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        service_obj = Service("/WebDrivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        #firefox invocation GECKO DRIVER
        service_obj = Service("/WebDrivers/geckodriver32.exe")
        driver = webdriver.Firefox(service=service_obj, options=options)
    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://qaclickacademy.github.io/protocommerce/")
    driver.maximize_window()
    request.cls.driver = driver
    yield #will be executed at the end
    print("Printed at the end")
    driver.close()



@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

