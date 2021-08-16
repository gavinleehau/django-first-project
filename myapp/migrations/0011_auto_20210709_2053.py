# Generated by Django 3.2.4 on 2021-07-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_abc'),
    ]

    operations = [
        migrations.DeleteModel(
            name='abc',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='timestamp',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterModelTable(
            name='post',
            table=None,
        ),
    ]