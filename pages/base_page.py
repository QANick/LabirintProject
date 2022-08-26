from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, app):
        self.app = app

    def _find_element(self, locator, wait_time=20):
        """
        Find element. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element


    def move_to_element(self, locator, wait_time=20):
        """
        Find element. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return perform move to element action
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        move = ActionChains(self.app.driver).move_to_element(element)
        return move.perform()

    def _find_elements(self, locator, wait_time=20):
        """
        Find elements. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return selenium elements
        """

        elements = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return elements

    def list_of_all_elements(self, locator, wait_time=20):
        """
        Find elements. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        create list of all found elements using cycle "for"
        :return: return list
        """
        all = self._find_elements(locator, wait_time)
        list = []
        for i in range(len(all)):
            list.append(i)
        return list

    def click_element(self, locator, wait_time=20):
        """
        Click element.
        """
        element = self._find_element(locator, wait_time)
        element.click()

    def confirm_action(self, wait_time=20):
        """
        Confirm action. Use Explicit wait
        """
        element = WebDriverWait(self.app.driver, wait_time).until(EC.alert_is_present())
        element.accept()

    def fill(self, locator, value: str, wait_time=20):
        """
        Fill element (fill == send_keys)
        :param locator: locator like (By.ID, 'name')
        :param value: string to fill
        :param wait_time: wait time
        """
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def move_to_end_page(self, locator, wait_time=20):
        """
        move to end page using Keys
        """
        element = self._find_element(locator, wait_time)
        element.send_keys(Keys.END)

    def text(self, locator, wait_time=20) -> str:
        """
        Get element text.
        """
        element = self._find_element(locator, wait_time)
        return element.text

    def open_page(self, url: str):
        """
        Open page.
        """
        self.app.driver.get(url)

    def clear(self, locator, wait_time=20):
        """
        Clear element.
        """
        element = self._find_element(locator, wait_time)
        element.clear()


