# Generated by Django 4.0.4 on 2022-06-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=200)),
                ('data', models.DateField()),
            ],
        ),
    ]
