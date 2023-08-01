# Generated by Django 4.2.3 on 2023-08-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Persons', '0003_alter_persons_email_alter_persons_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('has_filled_form', models.BooleanField(default=False)),
            ],
        ),
    ]
