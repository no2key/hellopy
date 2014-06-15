"""use Google SMTP send mail
"""

from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail():
    def __init__(self, user, password, smtp_server='smtp.gmail.com', port=587):
        self.user = user
        self.password = password
        #SMTP服务器地址
        self.smtp_server = smtp_server
        #服务器端口号：可选465 或 587
        self.port = port
        self.server = self.connect_server()

    def connect_server(self):
        """连接服务器
        """
        server = SMTP(self.smtp_server, self.port)
        server.ehlo()
        server.starttls()
        server.login(self.user, self.password)
        return server

    def send(self, to_mail, subject, message):
        """发送
        需要给出接受方、主题和邮件正文(支持html格式)
        """
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = self.user
        msg['To'] = to_mail

        part = MIMEText(message, 'html')
        msg.attach(part)

        self.server.sendmail(self.user, to_mail, msg.as_string())
        self.server.quit()


if __name__ == '__main__':
    mail = Mail('输入邮箱', '输入密码')

    html = """
    <html>
        <head>
        </head>
        <body>
            <h1>这是一个测试标题</h1>
            <a href="http://www.example.com">点击测试</a>
            <img src="https://0.gravatar.com/avatar/fae208aecd254ae2ef6145a3590dc822?d=https%3A%2F%2Fidenticons.github.com%2Fbca7f5f683d42833aab7f1a9c26d58fa.png&r=x&s=440">
        </body>
    </html>
    """

    mail.send('xxxx@xxx.com', '测试一下', html)