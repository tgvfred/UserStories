import random
import time
from hotdog.BasePage import HotDogBasePage
from hotdog.FindEither import FindEither
from selenium.webdriver import ActionChains
from webium import Find
import webium

webium.settings.implicit_timeout = 5


class CBCWebBase(HotDogBasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def back(self):
        self.driver.execute_script("window.history.go(-1)");
