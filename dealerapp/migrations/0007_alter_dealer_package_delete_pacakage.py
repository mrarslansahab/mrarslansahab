# Generated by Django 4.0 on 2022-05-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealerapp', '0006_pacakage_created_by_alter_dealer_deleted_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='package',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.DeleteModel(
            name='pacakage',
        ),
    ]
