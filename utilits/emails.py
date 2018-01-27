from django.template.loader import get_template
from django.core.mail import EmailMessage
from test_project.settings import FROM_EMAIL
from django.forms.models import model_to_dict
from emails.models import *
from django.template.loader import render_to_string


class SetingEmail(object):

    from_email= FROM_EMAIL
    replay_to_email=[from_email]
    target_emails=[]
    bcc_emails=[]

    vars=dict()


    def sending_email(self,type_id):
        if type_id==1:
            subject="Новая новость"
            message=render_to_string('emails_template/new.html')


        msg=EmailMessage(subject,message,reply_to=self.replay_to_email)
        msg.content_subtype='html'
        msg.mixed_subtype= 'related'
        msg.send()


        # kwargs={
        #     "type":type_id,
        #
        #
        # }