# Generated by Django 3.2.9 on 2021-11-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahorroapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='cuenta_AFP_soles',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='fecha',
            field=models.CharField(max_length=20),
        ),
    ]