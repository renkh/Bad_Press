# Generated by Django 2.0.4 on 2018-04-15 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badpress', '0005_auto_20180415_1648'),
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