# Generated by Django 4.0.2 on 2022-04-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haysite', '0005_data_person_questions_remove_order_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='response',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
