from  selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

class Baidu1(unittest.TestCase):
    '''百度搜索测试'''

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_baidu_search1(self):
        '''百度搜索关键字HTMLTestRunner'''
        driver = self.driver
        driver.get("https://www.baidu.com")
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        #断言：搜索结果也没的title是否等于HTMLTestRunner_百度搜索
        title=driver.title
        self.assertEquals(title,"HTMLTestRunner_百度搜索")


    def tearDown(self):
        self.driver.quit()


class Baidu2(unittest.TestCase):
    '''百度搜索测试2'''

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_baidu_search2(self):
        '''百度搜索关键字为空'''
        driver = self.driver
        driver.get("https://www.baidu.com")
        #driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        #断言：搜索结果也没的title是否等于HTMLTestRunner_百度搜索
        title=driver.title
        self.assertEquals(title,"百度一下，你就知道")


    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":

    testunit=unittest.TestSuite()
    testunit.addTest(Baidu1("test_baidu_search1"))
    testunit.addTest(Baidu2("test_baidu_search2"))
    now=time.strftime("%Y-%m-%d %Hh%Mm%Ss")

    fp = open("E:\\TestReport\\BaiduReport"+now+".html",'wb')
    runner=HTMLTestRunner(stream=fp,title="百度搜索测试报告",description="用例执行情况：")

    runner.run(testunit)
    fp.close()
