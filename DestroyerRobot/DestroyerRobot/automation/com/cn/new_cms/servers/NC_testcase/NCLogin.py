from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from DestroyerRobot.automation.com.cn.new_cms.servers.NCLoing.NCLogin import MPLoing

class NCLogin():
    def __init__(self,driver):
        self.page=BasePage(driver)

    MPLoing().input_mobile()
    MPLoing().input_password()
    MPLoing().input_click()
    MPLoing().get_current_url()





