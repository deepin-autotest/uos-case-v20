from funnylog.conf import setting
from youqu3 import log
from youqu3.dogtail import Dogtail

setting.CLASS_NAME_ENDSWITH = "Method"


@log
class DdeFileManagerMethod:

    @property
    def dfm(self):
        return Dogtail(name="dde-file-manager")

    def click_desktop_dir_in_left_view_by_attr(self):
        """点击左侧侧边栏的桌面目录"""
        self.dfm.ele("side_bar_view").child("桌面").click()


if __name__ == '__main__':
    DdeFileManagerMethod().click_desktop_dir_in_left_view_by_attr()
