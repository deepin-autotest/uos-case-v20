from youqu3 import sleep

from case.base_case import BaseCase
from method.dde_dock_method import DdeDockMethod
import pylinuxauto


class TestDfm(BaseCase):

    def test_dfm_1159151(self, gui, sleep, cmd):
        """任务栏启动文管"""
        gui.ctrl_alt_t()
        sleep(2)
        cmd.run("ls")
        # DdeDockMethod().right_click_dde_file_manager_on_dock_by_attr()
        # DdeDockMethod().click_open_in_right_menu_by_mk()
        # sleep(2)
        # self.assert_process_exist("dde-file-manager")

    # def teardown_method(self):
    #     DdeDockMethod.kill_process("dde-file-manager")
