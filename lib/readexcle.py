import xlrd
import pprint
from config import setting


class Readexcel():
    def __init__(self, filename, SheetName="Sheet1"):
        self.data = xlrd.open_workbook(filename)
        self.table = self.data.sheet_by_name(SheetName)

        self.nrows = self.table.nrows
        self.ncols = self.table.ncols

    def read_data(self):
        if self.nrows > 1:
            keys = self.table.row_values(0)
            listApiData = []
            for col in range(1, self.nrows):
                values = self.table.row_values(col)
                # keys values组合转为字典
                api_dict = dict(zip(keys, values))
                listApiData.append(api_dict)
            return listApiData
        else:
            print("表格是空数据")
            return None


if __name__ == '__main__':
    pprint.pprint(Readexcel(setting.SOURCE_FILE).read_data())
