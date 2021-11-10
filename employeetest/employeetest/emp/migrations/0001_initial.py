# Generated by Django 3.2.9 on 2021-11-08 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dept_Name', models.CharField(max_length=100)),
                ('Dept_Id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('DOB', models.DateField()),
                ('DOJ', models.DateField()),
                ('Address', models.CharField(max_length=200)),
                ('MOb_No', models.IntegerField()),
                ('Designation', models.CharField(max_length=100)),
                ('Dept_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp.department')),
            ],
        ),
    ]
