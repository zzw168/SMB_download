import os
import shutil
import smbclient    # pip install smbprotocol

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
        download_directory(remote_start_path, local_path)

        print(f"成功将网络共享文件夹 {remote_path} 的内容覆盖到本地文件夹 {local_path}")

    except Exception as e:
        print(f"发生错误: {e}")

# 使用示例
remote_host = "192.168.0.80"  # 共享文件夹所在主机的 IP 或主机名
share_name = "img"   # 共享文件夹名称
username = "administrator"
password = ""
remote_path = "01_秋名山_赛道/"      # 共享文件夹内的路径
local_path = "./local_folder"  # 本地文件夹路径

smb_download_and_overwrite(remote_host, share_name, username, password, remote_path, local_path)
