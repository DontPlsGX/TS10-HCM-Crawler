import pandas as pd
from openpyxl import Workbook

frames = ["ketqua1.csv","ketqua2.csv","ketqua3.csv","ketqua4.csv","ketqua5.csv"]
result = pd.concat(map(pd.read_csv, ["ketqua1.csv","ketqua2.csv","ketqua3.csv","ketqua4.csv","ketqua5.csv"]), ignore_index=True)
result = result.set_index("SBD").sort_index()
result["Chuyên"] = result["Chuyên"].map( lambda x: max(0,x))
result.to_csv('ketqua.csv')
result.to_excel('ketqua.xlsx')

print(result)
print(result["Toán"].value_counts())