from win32com import client

# Outlookアプリケーションをインスタンス化
outlook = client.Dispatch("Outlook.Application")

# メールオブジェクトの作成
mail = outlook.CreateItem(0) # 0:メール

mail.to = "herentongkegu087@gmail.com"
mail.subject = 'テストメール'
mail.bodyFormat = 1
mail.body = """各位
お疲れ様です。（ここに本文を入力）よろしくお願いいたします。
"""

# 送信前に確認（Outlookが起動）
#mail.display(1)

# メール送信
mail.Send()