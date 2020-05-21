# class locators:
#
#     #test_locators = [{"WTClick":"", "WLC":""}]
#     @staticmethod
#     def getTestData():
#         import openpyxl
#         book = openpyxl.load_workbook("C:\\Users\\Srinath\\Desktop\\PythonDemo.xlsx")
#         sheet = book.active
#         Dict = {}
#         for i in range(1, sheet.max_row):
#             # if sheet.cell(row=i, column=1).value=="WomenPageExpandOptions":
#             for j in range(1, sheet.max_column):
#                 Dict[sheet.cell(row=i + 1, column=j).value] = sheet.cell(row=i + 1, column=j + 1).value
#
#         return [Dict]
#         # print(Dict["WomenLabelCheck"])

class Locators:

    test_Locators = [{"WomenTabClick":"//a[text()='Women']"}]