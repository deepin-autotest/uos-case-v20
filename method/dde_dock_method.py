from funnylog2.config import config as log_config
from youqu3 import log
from youqu3.gui import pylinuxauto
from youqu3.cmd import Cmd

log_config.CLASS_NAME_ENDSWITH = "Method"


@log
class DdeDockMethod(Cmd):


    def click_dde_file_manager_on_dock_by_attr(self):
        """在任务栏点击文件管理器"""
        pylinuxauto.find_element_by_attr_path("/dde-dock/Btn_文件管理器").click()

    def right_click_dde_file_manager_on_dock_by_attr(self):
        """在任务栏右键点击文件管理器"""
        pylinuxauto.find_element_by_attr_path("/dde-dock/Btn_文件管理器").right_click()

    def click_open_in_right_menu_by_mk(self):
        """点击右键菜单中【打开】"""
        pylinuxauto.select_menu(1)


if __name__ == '__main__':
    DdeDockMethod().right_click_dde_file_manager_on_dock_by_attr()
    DdeDockMethod().click_open_in_right_menu_by_mk()

