# Generated by Django 3.0.7 on 2020-06-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='statu',
            new_name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
