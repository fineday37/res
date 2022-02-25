import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
# print(BASE_DIR)

TEST_CONFIG = os.path.join(BASE_DIR, "database", "config.ini")

# 模板文件
SOURCE_FILE = os.path.join(BASE_DIR, "DemoAPITestCase.xlsx")

# 结果文件
TARGET_FILE = os.path.join(BASE_DIR, "test.xls")

