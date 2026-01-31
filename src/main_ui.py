from PySide2.QtGui import QIcon
from subpage_imformations_ui import SubpageInformationUI
from qfluentwidgets import NavigationItemPosition, FluentWindow
from qfluentwidgets import FluentIcon as FIF


class MainWindow(FluentWindow):
    """应用程序主窗口，继承自FluentWindow"""

    def __init__(self):
        """初始化主窗口"""
        super().__init__()

        # 初始化窗口设置
        self.initWindow()

        # 导入子页面
        self.subpage_information = SubpageInformationUI(self)
        self.subpage_information.setObjectName("subpage_information")

        # 初始化导航栏
        self.initNavigation()

    def initNavigation(self):
        """初始化导航栏，添加各个子界面"""
        # 添加子界面
        self.addSubInterface(
            self.subpage_information, FIF.INFO, "信息", NavigationItemPosition.BOTTOM
        )

    def initWindow(self):
        """初始化窗口设置"""
        # 设置窗口大小
        self.resize(1080, 768)
        # 设置窗口图标
        self.setWindowIcon(QIcon("../assets/icon/appico.png"))  # type: ignore
        # 设置窗口标题
        self.setWindowTitle("祈福Sankteco - dev")
