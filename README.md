# TS10-HCM-Crawler
Crawler for TS10-HCM entrance exam.
To reuse, consider some following thing:

Api Link: #https://s6.tuoitre.vn/api/diem-thi-lop-10.htm
Origin: #https://tuoitre.vn
SBD from 9001 to 9438 and 90000 to 192007
x = 2024

Link work for each contestant's data as follow: #https://s6.tuoitre.vn/api/diem-thi-lop-10.htm? keywords=SBD & year=x & sitename=tuoitre.vn (with no space in between)

Response format:
```
"data": [
        {
            "id": "120000",
            "Id": "120000",
            "TinhId": 12,
            "NGAY_SINH": "12\/14\/2009",
            "file_name": "",
            "modified_date": "2024-06-19T08:21:27.861320",
            "NAM": "2024",
            "KY_THI": "LOP10",
            "SBD": "120000",
            "HO_TEN": "Phan Qu\u1ed1c C\u01b0\u1eddng",
            "TINH": "HCM",
            "TOAN": 3.25,
            "VAN": 4.25,
            "NGOAI_NGU": 2,
            "CHUYEN": -1,
            "TONGDIEM": 9.5,
            "SOBAODANH": "120000",
            "LI": "",
            "HOA": "",
            "SU": "",
            "DIA": "",
            "NN": 2,
            "GDCN": ""
        }
```
