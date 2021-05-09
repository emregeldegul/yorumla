from flask_mail import Message
from flask import render_template, current_app as app

from app import mail


class EmailService():
    @staticmethod
    def _send_email(subject, sender, recipients, text_body, html_body):
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = text_body
        msg.html = html_body
        mail.send(msg)

    def send_password_reset_email(self, user):
        token = user.get_reset_password_token()
        self._send_email('Reset Your Password',
                         sender=app.config['ADMINS'][0],
                         recipients=[user.email],
                         text_body=render_template('assets/reset_password.txt',
                                                   user=user, token=token),
                         html_body=render_template('assets/reset_password.html',
                                                   user=user, token=token))
