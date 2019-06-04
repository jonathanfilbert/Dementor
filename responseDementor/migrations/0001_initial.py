# Generated by Django 2.0.2 on 2019-06-04 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortofolioData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Design', 'Design'), ('Development', 'Development'), ('Social', 'Social'), ('Leadership', 'Leadership')], max_length=100)),
                ('short_description', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]