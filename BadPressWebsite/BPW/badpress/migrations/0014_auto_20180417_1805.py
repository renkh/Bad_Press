# Generated by Django 2.0.3 on 2018-04-17 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badpress', '0013_auto_20180417_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.State'),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the article', max_length=5000),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.State'),
        ),
    ]
