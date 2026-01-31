"""
本文件是储存项目常量与变量标准值的文件
"""

import gettext


_ = gettext.gettext


class BasicString:
    """项目基础信息字符串类"""

    NONE_TEXT = ""

    # 项目本体信息
    APP_NAME = "Sankteco"
    APP_FULL_NAME = "祈福Sankteco"
    APP_VERSION = "Version Dev"
    APP_VERSION_TYPE = "Dev"
    APP_COPYTYPE = "Copyleft, 2023~2026, HXES.As is."


class InfoUIString:
    """信息 界面字符串，仅包含 subpage_imformations_ui.py 相关字符串，不包含隶属于主程序多UI交互的字符串"""

    # 信息板 部分
    INFOBODCARD_TITLE = _("信息板")

    # 支持 部分
    SUPPTCARD_TITLE = _("支持")
    SUPPTCARD_OFFLINEDOCBUTTON = _("查看")
    SUPPTCARD_ONLINEDOCBUTTON = _("查看")
    SUPPTCARD_OFFLINEDOCGROUPTITLE = _("离线帮助文档")
    SUPPTCARD_OFFLINEDOCGROUPCONTEXT = _("查看保存于本地的帮助文档，如果有的话")
    SUPPTCARD_ONLINEDOCGROUPTITLE = _("在线帮助文档")
    SUPPTCARD_ONLINEDOCGROUPCONTEXT = _("访问项目官网获取在线帮助文档")

    # 语言 部分
    LANGCARD_TITLE = _("语言")
    LANGCARD_LANGCARD_TITLE = _("语言选项")
    LANGCARD_LANGCARD_DETAIL = _("从此处更改界面语言")
    LANGCARD_LANGCARD_COMBO_ZHCN = "简体中文"
    LANGCARD_LANGCARD_COMBO_IE = "Esperanto"

    # 更新 部分
    UPDATECARD_TITLE = _("更新")
    UPDATECARD_PIPE_RELEASE = _("正式版")
    UPDATECARD_PIPE_BETA = _("测试版")
    UPDATECARD_UPDATESTATUS = _("检查更新")
    UPDATECARD_PIPEGROUP_TITLE = _("更新通道")
    UPDATECARD_PIPEGROUP_DETAIL = _("选择项目从何通道进行更新")
    UPDATECARD_VERSTATUSGROUP_TITLE = _("当前版本已是最新版本")
    UPDATECARD_VERNOWGROUP_TITLE = _("当前版本")
