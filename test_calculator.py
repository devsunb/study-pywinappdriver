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


class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.driver = webdriver.Remote(
            command_executor='http://192.168.56.102:4723',
            desired_capabilities=desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def getresults(self):
        displaytext = self.driver.find_element_by_accessibility_id("CalculatorResults").text
        displaytext = displaytext.strip("표시는 ")
        displaytext = displaytext.rstrip(' ')
        displaytext = displaytext.lstrip(' ')
        return displaytext

    def test_initialize(self):
        self.driver.find_element_by_name("지우기").click()
        self.driver.find_element_by_name("7").click()
        self.assertEqual(self.getresults(), "7")
        self.driver.find_element_by_name("지우기").click()

    def test_addition(self):
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("더하기").click()
        self.driver.find_element_by_name("7").click()
        self.driver.find_element_by_name("같음").click()
        self.assertEqual(self.getresults(), "8")

    def test_combination(self):
        self.driver.find_element_by_name("7").click()
        self.driver.find_element_by_name("곱하기").click()
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("더하기").click()
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("같음").click()
        self.driver.find_element_by_name("나누기").click()
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("같음").click()
        self.assertEqual(self.getresults(), "8")

    def test_division(self):
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("8").click()
        self.driver.find_element_by_name("나누기").click()
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("같음").click()
        self.assertEqual(self.getresults(), "8")

    def test_multiplication(self):
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("곱하기").click()
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("같음").click()
        self.assertEqual(self.getresults(), "81")

    def test_subtraction(self):
        self.driver.find_element_by_name("9").click()
        self.driver.find_element_by_name("빼기").click()
        self.driver.find_element_by_name("1").click()
        self.driver.find_element_by_name("같음").click()
        self.assertEqual(self.getresults(), "8")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=2).run(suite)
