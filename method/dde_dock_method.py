from youqu3.dogtail import Dogtail


class DdeDockMethod():

    @property
    def dock(self):
        return Dogtail(name="dde-dock")

    def click_dde_file_manager_on_dock_by_attr(self):
        """在任务栏点击文件管理器"""
        self.dock.ele("Btn_文件管理器").click()

if __name__ == '__main__':
    DdeDockMethod().click_dde_file_manager_on_dock_by_attr()
