import sys
import platform
import os
import time


def test_environment():
    print("Python Environment Test")
    print("=" * 30)

    # 检查 Python 版本
    print(f"Python Version: {sys.version}")

    # 检查操作系统
    print(f"Operating System: {platform.system()} {platform.release()}")

    # 检查 Python 的安装路径
    print(f"Python Path: {sys.executable}")

    # 检查当前工作目录
    print(f"Current Working Directory: {os.getcwd()}")

    # 检查系统环境变量
    print("Environment Variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

    # 检查 Python 的模块搜索路径
    print("Python Module Search Path:")
    for path in sys.path:
        print(f"- {path}")

    # 检查脚本运行时间
    start_time = time.time()
    # 在这里添加您要测试的代码
    time.sleep(1)  # 延迟 1 秒进行测试
    end_time = time.time()
    print(f"Script Runtime: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    test_environment()
