import threading

from django.core.mail import EmailMultiAlternatives


class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list,
                 fail_silently, html_message=None):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html_message
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email,
                                     self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
        msg.send(self.fail_silently)


def send_mail(subject, body, from_email, recipient_list, fail_silently=False,
              html_message=None, *args, **kwargs):
    obj = EmailThread(subject, body, from_email, recipient_list, fail_silently=fail_silently,
                      html_message=html_message)
    obj.start()
