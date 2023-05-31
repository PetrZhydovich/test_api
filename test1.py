from testpage2 import OperationsHelper
import logging
import time


"""Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета.
 Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert  Вывести текст alert.text """


def test_step1(browser):
    
    logging.info('Test Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('NatGlu')
    testpage.enter_pass('db2d28bf9f')
    testpage.click_login_button()
    #assert testpage.get_error_text() == "401"
    testpage.click_contact_button()
    time.sleep(3)
    testpage.enter_name('Glushko Natalya')
    testpage.enter_email('test@mail.ru')
    testpage.enter_content('Test information')
    time.sleep(3)
    testpage.click_contact_us_button()
    time.sleep(3)
    assert testpage.alert() == 'Form successfully submitted'