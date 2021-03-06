# Generated by Django 4.0 on 2022-04-16 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=64, null=True)),
                ('l_name', models.CharField(max_length=64, null=True)),
                ('contact', models.CharField(max_length=64, null=True)),
                ('cvrno', models.CharField(max_length=64, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=64, null=True)),
                ('postal_code', models.CharField(max_length=64, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('Telephone', models.CharField(max_length=100, null=True)),
                ('dealer_type', models.CharField(max_length=64, null=True)),
                ('approved', models.CharField(max_length=64, null=True)),
                ('is_deleted', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='pacakage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True)),
                ('price', models.IntegerField(null=True)),
                ('limit', models.CharField(max_length=64, null=True)),
                ('is_deleted', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
