# Generated by Django 2.0.3 on 2018-05-03 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badpress', '0025_auto_20180503_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.State'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.State'),
        ),
    ]
