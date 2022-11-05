from django.db import models

# Create your models here.
class BotUsers(models.Model):
    full_name = models.CharField(max_length=100,help_text="Enter fullname",verbose_name="Fullname")
    telegram_id = models.CharField(max_length=20,unique=True,help_text="Enter Chat Id",verbose_name="User ID")
    language = models.CharField(max_length=10,default='uz',help_text="Enter Language",verbose_name="Language")
    def __str__(self):
        return self.full_name
    class Meta:
        db_table = "Bot Foydalanuvchilari"
        verbose_name = "Bot User "
        verbose_name_plural = "Bot Users "
class Image(models.Model):
    image = models.ImageField(upload_to ='images')
    def __str__(self):
        return 'Image'