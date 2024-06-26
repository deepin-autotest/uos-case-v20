
from youqu3.rpc.rpc_dogtail import RPCDogtail

from config import config
class RemoteMethod:

    def __init__(self, user, ip, password):
        self.user = user
        self.ip = ip
        self.password = password

    @property
    def rpc_dogtail(self):
        return RPCDogtail(
            user=self.user,
            ip=self.ip,
            password=self.password,
            project_abspath=config.ROOTDIR,
        )
    def click_dde_file_manager_by_attr(self):
        self.rpc_dogtail.ele_click("Btn_文件管理器")

if __name__ == '__main__':
    RemoteMethod(user="uos", ip="10.8.7.55", password="1").click_dde_file_manager_by_attr()