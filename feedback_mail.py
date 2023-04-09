import email.message
import smtplib

def mail(sender="robot", receiver="klps2146@gmail.com", subject="hi", html_detail="<p>Testing</p>", login_account="tpyemlsend@gmail.com", login_password="klps2146"):
    # must enter a receiver
    msg=email.message.EmailMessage()
    msg["From"]=sender # 寄件人
    msg["TO"]=receiver # 收件人
    msg["Subject"]=str(subject) #主旨
    # 寄送純文字內容
    # msg.set_content("testsss")
    # 件送HTML內容
    msg.add_alternative(html_detail, subtype="html") #內容
    # 連接至SMTP Server
    server=smtplib.SMTP_SSL("smtp.gmail.com", 465) # (主機名稱，SSL通訊埠號)
    server.login(login_account, login_password) # 驗證帳號 (帳號，密碼)
    server.send_message(msg) # 傳送msg中的訊息
    server.close() # 關閉連線
    # time.sleep(2) 

    ######## 無法使用 ########