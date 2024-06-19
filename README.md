# TS10-HCM-Crawler
Crawler for TS10-HCM entrance exam.
To reuse, consider some following thing:

Api Link: https[://]s6.tuoitre.vn/api/diem-thi-lop-10.htm 

Origin: https[://]tuoitre.vn

SBD from 9001 to 9438 and 90000 to 192007

x = 2024

Link work for each contestant's data as follow: https[://]s6.tuoitre.vn/api/diem-thi-lop-10.htm? keywords=SBD & year=x & sitename=tuoitre.vn (with no space in between)
*remove the square bracket for working link

# Response format:
```
"data": [
        {
            "id": "XXX",
            "Id": "XXX",
            "TinhId": XX,
            "NGAY_SINH": "dd\/mm\/yyyy",
            "file_name": "",
            "modified_date": "2024-06-19T08:21:27.861320",
            "NAM": "202x",
            "KY_THI": "LOP10",
            "SBD": "XXXXXX",
            "HO_TEN": "Nguyen Van A",
            "TINH": "HCM",
            "TOAN": X.XX,
            "VAN": X.XX,
            "NGOAI_NGU": X.XX,
            "CHUYEN": X or -1,
            "TONGDIEM": X.XX,
            "SOBAODANH": "XXX",
            "LI": "",
            "HOA": "",
            "SU": "",
            "DIA": "",
            "NN": X,
            "GDCN": ""
        }
```
