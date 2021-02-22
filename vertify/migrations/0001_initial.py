# Generated by Django 3.1.7 on 2021-02-22 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=16)),
                ('telphone', models.CharField(max_length=16)),
                ('reffrall', models.CharField(default='klzlcbsadv', editable=False, max_length=16, unique=True)),
                ('imageAcc', models.ImageField(blank=True, upload_to='Users/%Y/%m/')),
                ('imageCode', models.ImageField(blank=True, upload_to='Users/%Y/%m/')),
                ('activeAcc', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]