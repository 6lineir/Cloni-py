# Generated by Django 3.1.7 on 2021-02-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reffrall',
            field=models.CharField(default='e340shfygf', editable=False, max_length=10, unique=True, verbose_name='کد بازاریابی'),
        ),
    ]
