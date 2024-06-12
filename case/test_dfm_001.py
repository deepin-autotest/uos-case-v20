from youqu3.dogtail import Dogtail


class TestDfm:

    def test_dfm_001(self):
        """任务栏启动文管"""
        location = Dogtail().ele("Btn_文件管理器").click()
        print(location)
        assert location
