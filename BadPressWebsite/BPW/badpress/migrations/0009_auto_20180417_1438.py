# Generated by Django 2.0.3 on 2018-04-17 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badpress', '0008_auto_20180417_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={},
        ),
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.State'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='position',
            field=models.CharField(blank=True, choices=[('r', 'Republican'), ('d', 'Democrat'), ('i', 'Independent')], max_length=1),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='badpress.State'),
        ),
    ]
