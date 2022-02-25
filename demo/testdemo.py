from config import setting
import pytest
import os
import sys
from lib import readexcle
from db_fixture import apitest_data
from demo.sendRequests import sendrequests
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

Apidata = readexcle.Readexcel(setting.TARGET_FILE).read_data()


class TestCase:
    def setup_class(self):
        apitest_data.init_data()

    def teardown_class(self):
        print("测试结束")

    @pytest.mark.parametrize("arg", Apidata)
    def test_001(self, arg):
        try:
            re = sendrequests(arg)
            code = re.status_code
            assert code == int(200)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    pytest.main("-vs")
