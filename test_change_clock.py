# ******************************************************************************
#
# Copyright (c) 2016 Microsoft Corporation. All rights reserved.
#
# This code is licensed under the MIT License (MIT).
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ******************************************************************************

import unittest

from appium import webdriver
from selenium.webdriver.common.keys import Keys


class TestChangeClock(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(self):
        desired_caps = {"app": "Root"}
        self.driver = webdriver.Remote(
            command_executor='http://192.168.56.102:4723',
            desired_capabilities=desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # def getresults(self):
    #     displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
    #     displaytext = displaytext.strip("표시는 ")
    #     displaytext = displaytext.rstrip(' ')
    #     displaytext = displaytext.lstrip(' ')
    #     return displaytext

    def test_initialize(self):
        commands = {
            'sync_datetime': 'W32tm /resync /force',
            'change_day': 'Set-Date -Date (Get-Date).AddDays({})'
        }

        self.driver.find_element_by_name("시작").click()
        self.driver.find_element_by_name("검색 상자").send_keys("Powershell")
        self.driver.find_element_by_name("검색 상자").send_keys(Keys.ENTER)
        auto_clock = self.driver.find_element_by_name("자동으로 시간 설정")
        if auto_clock.is_enabled():
            print('자동으로 시간 설정 비활성화')
            auto_clock.send_keys(Keys.SPACE)


if __name__ == '__main__':
    TestChangeClock().run()
