# Generated by Django 4.2.7 on 2024-03-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marja', models.DecimalField(decimal_places=2, max_digits=10)),
                ('package_code', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]