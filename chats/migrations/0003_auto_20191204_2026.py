# Generated by Django 2.2.5 on 2019-12-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20191107_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='type',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='url',
            field=models.FileField(upload_to='attachments/'),
        ),
    ]