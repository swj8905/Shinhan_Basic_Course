import openpyxl
import smtplib
from email.mime.text import MIMEText

naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
naver_server.login("talingpython", "q1w2e3!@#")

book = openpyxl.load_workbook("./list.xlsx")
# sheet = book["sheet_name"]
sheet = book.active
cnt = 0
for row in sheet.rows:
    if row[4].value == "X":
        continue
    date = row[0].value
    name = row[1].value
    your_mail = row[2].value
    product = row[3].value
    title = f"안녕하세요. {name} 님 XX 쇼핑몰입니다."
    content = f"""
결제 완료 안내 메일입니다.
성함 : {name}
날짜 : {date}
제품 : {product}"""

    msg = MIMEText(content, _charset="euc-kr")
    msg["From"] = "talingpython@naver.com"
    msg["To"] = your_mail
    # msg["Cc"] = ["aaa@naver.com", "bbb@naver.com"]
    msg["Subject"] = title
    naver_server.sendmail("talingpython@naver.com",
                          your_mail, msg.as_string())
    print(f"{name}님께 메일을 보냈습니다.")
    cnt += 1
    if cnt % 20 == 0:
        naver_server.quit()
        naver_server = smtplib.SMTP_SSL("smtp.naver.com", 465)
        naver_server.login("talingpython", "q1w2e3!@#")
