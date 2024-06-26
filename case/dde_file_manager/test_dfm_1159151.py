from youqu3 import sleep

from case.base_case import BaseCase
from method.dde_dock_method import DdeDockMethod


class TestDfm(BaseCase):

    def test_dfm_1159151(self):
        """任务栏启动文管"""
        DdeDockMethod().right_click_dde_file_manager_on_dock_by_attr()
        DdeDockMethod.select_menu(1)
        sleep(2)
        self.assert_process_status(True, "dde-file-manager")
