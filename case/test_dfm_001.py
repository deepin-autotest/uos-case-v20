from youqu_dogtail import DogtailUtils
class TestDfm:


    def test_dfm_001(self):
        """任务栏启动文管"""
        location = DogtailUtils().element_center("Btn_文件管理器")
        print(location)
        assert location