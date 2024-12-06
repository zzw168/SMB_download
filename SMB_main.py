import subprocess
import sys

import yaml
from PySide6 import QtCore
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableWidgetItem

from SMB_ui import Ui_MainWindow
from tool_unit import *

import os
import shutil
import smbclient  # pip install smbprotocol


def smb_download_and_overwrite(remote_host, share_name, username, password, remote_path, local_path):
    """
    使用 smbclient 从共享文件夹下载内容并覆盖本地文件夹。

    :param remote_host: 远程主机地址（IP 或主机名）
    :param share_name: 共享文件夹名称
    :param username: 登录用户名
    :param password: 登录密码
    :param remote_path: 远程共享文件夹中的路径（从共享根目录开始）
    :param local_path: 本地文件夹路径
    """
    try:
        # 设置 SMB 连接的认证信息
        smbclient.register_session(remote_host, username=username, password=password)

        # 删除本地文件夹并重新创建
        # if os.path.exists(local_path):
        #     shutil.rmtree(local_path)
        # os.makedirs(local_path)

        # 递归下载函数
        def download_directory(remote_dir, local_dir):
            os.makedirs(local_dir, exist_ok=True)

            # 列出远程目录的内容
            for entry in smbclient.scandir(remote_dir):
                remote_item = os.path.join(remote_dir, entry.name).replace("\\", "/")
                local_item = os.path.join(local_dir, entry.name)

                if entry.is_dir():
                    # 如果是文件夹，递归下载
                    download_directory(remote_item, local_item)
                else:
                    # 如果是文件，下载到本地
                    with smbclient.open_file(remote_item, mode="rb") as remote_file:
                        with open(local_item, "wb") as local_file:
                            shutil.copyfileobj(remote_file, local_file)

        # 构建远程路径并开始下载
        remote_start_path = f"\\\\{remote_host}\\{share_name}\\{remote_path}".replace("\\", "/")
        ui.textBrowser.append(succeed('正在从 %s 升级。。。' % remote_start_path))
        download_directory(remote_start_path, local_path)
        ui.textBrowser.append(succeed("成功将网络共享文件夹 %s 的内容覆盖到本地文件夹 %s" % (remote_path, local_path)))

        print(f"成功将网络共享文件夹 {remote_path} 的内容覆盖到本地文件夹 {local_path}")

    except Exception as e:
        ui.textBrowser.append(fail(f"发生错误: {e}"))
        print(f"发生错误: {e}")


def table_change():
    global config_list
    global config_all
    tb_camera = ui.tableWidget_camera
    row = tb_camera.currentRow()
    col = tb_camera.currentColumn()
    try:
        if tb_camera.item(row, col) and not is_natural_num(tb_camera.item(row, col).text()):
            tb_camera.item(row, col).setText(config_list[row][col])
        else:
            config_list[row][col] = tb_camera.item(row, col).text()
            key = list(config_all.keys())[row]
            if col == 1:
                item = 'num'
            else:
                item = 'flip'
            config_all[key][item] = int(tb_camera.item(row, col).text())
    except:
        print("数据表操作出错！")


def save_config():
    global config_all

    file = "cameraPositionConfig.txt"
    if os.path.exists(file):
        try:
            with open(file, "w", encoding="utf-8") as f:
                f.write(str(config_all))
            ui.textBrowser.append(succeed('镜头设置成功！'))
        except:
            ui.textBrowser.append(fail('镜头设置错误！'))


def load_config():
    global config_all
    global config_list
    file = "cameraPositionConfig.txt"
    if os.path.exists(file):
        f = open(file, 'r', encoding='utf-8')
        config_all = eval(f.read())
        f.close()
        tb_camera = ui.tableWidget_camera
        tb_camera.setRowCount(len(config_all.keys()))
        for index, key in enumerate(config_all.keys()):
            item = QTableWidgetItem(str(key))
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemFlag(Qt.ItemIsSelectable | Qt.ItemIsEnabled))  # 单元格不可编辑
            tb_camera.setItem(index, 0, item)
            item_num = QTableWidgetItem(str(config_all[key]['num']))
            item_num.setTextAlignment(Qt.AlignCenter)
            tb_camera.setItem(index, 1, item_num)
            item_flip = QTableWidgetItem(str(config_all[key]['flip']))
            item_flip.setTextAlignment(Qt.AlignCenter)
            tb_camera.setItem(index, 2, item_flip)
            config_list.append([str(key), str(config_all[key]['num']), str(config_all[key]['flip'])])


def update_button():
    save_main_yaml()
    update_file()
    start_program()


def start_program():
    current_working_dir = os.getcwd()
    subprocess.Popen(
        [r"%s\start_recognition.bat" % current_working_dir],
        shell=True)
    print(r"%s\start_recognition.bat" % current_working_dir)


def update_file():
    remote_host = ui.lineEdit_remote_host.text()
    share_name = ui.lineEdit_share_name.text()
    username = ui.lineEdit_username.text()
    password = ui.lineEdit_password.text()
    remote_path = ui.lineEdit_remote_path.text()
    local_path = ui.lineEdit_local_path.text()

    smb_download_and_overwrite(remote_host, share_name, username, password, remote_path, local_path)


def save_main_yaml():
    global main_all
    file = "main_config.yml"
    if os.path.exists(file):
        main_all['remote_host'] = ui.lineEdit_remote_host.text()
        main_all['share_name'] = ui.lineEdit_share_name.text()
        main_all['username'] = ui.lineEdit_username.text()
        main_all['password'] = ui.lineEdit_password.text()
        main_all['remote_path'] = ui.lineEdit_remote_path.text()
        main_all['local_path'] = ui.lineEdit_local_path.text()
        try:
            with open(file, "w", encoding="utf-8") as f:
                yaml.dump(main_all, f, allow_unicode=True)
            ui.textBrowser.append(succeed('升级设置保存：成功'))
        except:
            ui.textBrowser.append(fail('升级设置保存：失败'))


def load_main_yaml():
    global main_all
    file = "main_config.yml"
    if os.path.exists(file):
        f = open(file, 'r', encoding='utf-8')
        main_all = yaml.safe_load(f)
        f.close()

        ui.lineEdit_remote_host.setText(main_all['remote_host'])
        ui.lineEdit_share_name.setText(main_all['share_name'])
        ui.lineEdit_username.setText(main_all['username'])
        ui.lineEdit_password.setText(main_all['password'])
        ui.lineEdit_remote_path.setText(main_all['remote_path'])
        ui.lineEdit_local_path.setText(main_all['local_path'])


class ZUi(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, z_window):
        super().setupUi(z_window)
        tb_camera = self.tableWidget_camera
        tb_camera.horizontalHeader().setStyleSheet("QHeaderView::section{background:rgb(245,245,245);}")
        tb_camera.verticalHeader().setStyleSheet("QHeaderView::section{background:rgb(245,245,245);}")


class ZMainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口图标
        self.setWindowIcon(QIcon("./icon.ico"))

    def closeEvent(self, event):
        # 创建确认对话框
        reply = QMessageBox.question(
            self,
            "退出",
            "您确定要退出程序吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        # 检查用户的响应
        if reply == QMessageBox.Yes:
            event.accept()  # 接受关闭事件，程序退出
        else:
            event.ignore()  # 忽略关闭事件，程序继续运行


class ZApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.aboutToQuit.connect(self.onAboutToQuit)

    @Slot()
    def onAboutToQuit(self):
        print("Exiting the application.")
        try:
            # 停止所有服务线程
            self.stop_all_threads()

        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Stopping application.")

        finally:
            print("Waiting for all threads to exit...")
            self.join_all_threads()
            print("All servers are closed. Exiting.")

    def stop_all_threads(self):
        """停止所有线程的函数。"""
        try:
            pass
        except Exception as e:
            print(f"Error stopping threads: {e}")

    def join_all_threads(self):
        """等待所有线程退出。"""
        try:
            pass
        except Exception as e:
            print(f"Error waiting threads: {e}")


if __name__ == '__main__':
    app = ZApp(sys.argv)

    z_window = ZMainwindow()
    ui = ZUi()
    ui.setupUi(z_window)
    z_window.show()

    main_all = []  # 总体设置
    config_list = []  # 镜头设置列表
    config_all = {}  # 镜头设置

    load_main_yaml()
    load_config()

    ui.tableWidget_camera.itemChanged.connect(table_change)
    ui.pushButton_camera_save.clicked.connect(save_config)
    ui.pushButton_update.clicked.connect(update_button)
    ui.pushButton_start.clicked.connect(start_program)

    sys.exit(app.exec())
