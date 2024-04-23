# send_gmail.py：

import smtplib
import ssl
from email.mime.text import MIMEText

try:
    # 自分のgmailアドレス
    gmail_account = "herentongkegu087@gmail.com"

    # 自分のGoogleアカウントのパスワード
    gmail_password = "KirigayaMikkisanhaaho"

    # メールの送信先
    mail_to = "herentongkegu087@gmail.com"

    # メールデータ(MIME)の作成

    # 件名
    subject = "Test"

    # 本文
    body = "ここに本文を入力します。"

    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["To"] = mail_to
    msg["From"] = gmail_account

    # Gmailに接続
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
                              context=ssl.create_default_context())
    server.login(gmail_account, gmail_password)
    server.send_message(msg)  # メールの送信
    print("送信完了しました。")

except Exception as e:
    print(e)

finally:
    print("処理が終了しました。")
