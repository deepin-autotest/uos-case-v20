from funnylog.conf import setting as log_setting
from youqu3 import log
from youqu3.dogtail import Dogtail
from youqu3.mousekey import MouseKey

log_setting.CLASS_NAME_ENDSWITH = "Method"


@log
class DdeDockMethod(MouseKey):

    @property
    def dock(self):
        return Dogtail(appname="dde-dock")

    def click_dde_file_manager_on_dock_by_attr(self):
        """在任务栏点击文件管理器"""
        self.dock.ele("Btn_文件管理器").click()

    def right_click_dde_file_manager_on_dock_by_attr(self):
        """在任务栏右键点击文件管理器"""
        self.dock.ele("Btn_文件管理器").right_click()




if __name__ == '__main__':
    DdeDockMethod().click_dde_file_manager_on_dock_by_attr()
