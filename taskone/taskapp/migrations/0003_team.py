# Generated by Django 4.1.7 on 2023-03-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_rename_foodcollection_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=250)),
                ('t_img', models.ImageField(upload_to='teampics')),
                ('t_desc', models.TextField()),
            ],
        ),
    ]
