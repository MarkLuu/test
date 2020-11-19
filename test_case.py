# -*- coding: utf-8 -*-

import time,os,pytest
import allure

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ttime = time.strftime("%Y%m%d_%H%M%S",time.localtime())

base ='https://www.baidu.com/'

@pytest.mark.last
@allure.story('测试-最后执行')
@allure.title("测试-最后执行")
def test_endtest():
    pass

@allure.story('测试套')
@allure.title("测试套")
class Test_case():
    @allure.story('测试-加')
    @allure.title("测试-加")
    @allure.severity('Blocker'.lower())
    def test_c1(self):
        # print(a,b)
        allure.attach('测试数据','测试数据')
        pass
        # return a + b


# @allure.feature('车辆监控')
# class Test_statisticalForms():
#     # def setup_class(self):
#     #     print('类 前运行')

#     # def teardown_class(self):
#     #     print('\n类执行后,运行;')
#     #     # 检查点: 错误示例
#     #     # assert 1+1 == 3

#     @allure.story('车辆单日运行统计')
#     @allure.title("车辆单日运行统计")
#     @allure.severity('Blocker'.lower())
#     def test_vehicleOperation(self,driver):
#         '''
#         车辆单日运行统计
#             选择车型,查询
#             翻页到第2页
#             输入1,查询vin列表,选择第1个vin,查询
#         '''
#         driver.get(base + "/rvmSystem/statisticalForms/vehicleOperation")# 进入页面
#         # time.sleep(2)
#         # sc(driver,'vehicleOperation')
#         febx(driver,u'//i[@class="el-select__caret el-input__icon el-icon-arrow-up"]').click()
#         febx(driver,u'//*[text()="AS24"] | //ul[@class="el-scrollbar__view el-select-dropdown__list"]/li[4]').click()
#         febx(driver,u'//*[text()="查询"]').click()
#         # time.sleep(2)
#         # sc(driver,'vehicleOperation')
#         try:
#             febx(driver,u'//ul[@class="tablepage ivu-page mini"]/li[3]/a').click()
#             # time.sleep(2)
#         except Exception as e:
#             print(e)

#         febx(driver,u'//i[@class="el-select__caret el-input__icon el-icon-arrow-up"]').click()
#         febx(driver,u'//div[@class="input"]//input[@class="ivu-input ivu-input-default"]').send_keys('1')
#         febx(driver,u'//div[@class="ivu-select-dropdown d-menu"]//li[1]').click()
#         febx(driver,u'//*[text()="查询"]',3).click()
#         time.sleep(2)
#         # sc(driver,'vehicleOperation')


if __name__ == '__main__':
    fn = os.path.basename(__file__)
    # tt =time.strftime("%Y%m%d_%H%M%S",time.localtime())
    # tt = time.strftime("%Y%m%d",time.localtime())
    # allureRP = 'D:/think/Documents/OneDrive/tools/allure-2.13.5/bin/allure.bat'
    # ospath = './out/tmp/'
    # if os.path.exists(ospath) and os.path.isdir(ospath):
    #     print(ospath)
    #     # os.system(f'pytest -v {fn} --alluredir {ospath}')
    # else:
    #     os.makedirs(ospath)
    #     print('创建目录：',ospath)
    # os.system(f'pytest -v {fn} --alluredir {ospath}')
    pytest.main(['-v', f'{fn}','--alluredir=report'])
    # pytest.main(['-vs','--tb=short',f'{fn}','--reruns','5'])
    # pytest.main(['-vs','--tb=short',f'{fn}',])
    # pytest.main(['-vs','--lf','--tb=short',f'{fn}',])
    # os.system(f'pytest -vs {fn} --html=out/report/PyTest_{time.strftime("%Y%m%d_%H%M%S",time.localtime())}.html --alluredir {ospath}')
    # os.system(f'pytest -v {fn} --alluredir {ospath}')
    # os.system(f'{allureRP} generate --clean {ospath} -o out/report')
    # os.system(f'{allureRP} open -h 127.0.0.1 -p 8082 out/report')
    # os.system(f'{allureRP} serve -h 127.0.0.1 {ospath}')