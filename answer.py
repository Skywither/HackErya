# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from lxml import etree
from selenium import webdriver

# url
course_url = ''
driver = webdriver.Chrome(executable_path='webDriver/chromedriver')


class hackErya(object):
    """docstring for hackErya"""
    def __init__(self, driver):
        super(hackErya, self).__init__()
        self.driver = driver

    def login(self):
        self.driver.get('http://passport2.chaoxing.com/login?fid=430&refer=')
        self.driver.find_element_by_id("unameId").send_keys("")  # username
        self.driver.find_element_by_id("passwordId").send_keys("")  # password
        time.sleep(7)
        # self.driver.find_element_by_class_name("zl_btn_right").click()  # login buttion
        self.driver.get(course_url)
        time.sleep(1)
        html = etree.HTML(self.driver.page_source)
        hrml_rsp = html.xpath("//em[@class='orange']/../../span[@class='articlename']//@href")
        return hrml_rsp

    def func(self):
        self.driver.switch_to.frame(self.driver.find_element_by_id("iframe"))
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.driver.switch_to.frame(self.driver.find_element_by_id("frame_content"))

    def run(self, course_list):
        for cl in course_list:
            link = 'https://mooc1-1.chaoxing.com' + cl.replace('amp;', '')
            print(link)
            self.driver.get(link)
            time.sleep(5)
            try:
                if "dct3" in self.driver.page_source:
                    self.driver.find_element_by_id("dct3").click()
                else:
                    self.driver.find_element_by_id("dct2").click()
            except Exception as e:
                pass
            finally:
                time.sleep(5)
                self.func()
                self.driver.execute_script("document.getElementsByClassName('Btn_blue_1 marleft10')[0].click()")
                time.sleep(5)
                self.driver.execute_script("document.getElementsByClassName('bluebtn')[0].click()")
                time.sleep(120)


if __name__ == '__main__':
    erya = hackErya(driver)
    login = erya.login()
    erya.run(login)