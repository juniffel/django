# Generated by Django 5.1.1 on 2024-10-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('regdate', models.DateTimeField(auto_now=True)),
                ('readcount', models.IntegerField(default=0)),
            ],
        ),
    ]
