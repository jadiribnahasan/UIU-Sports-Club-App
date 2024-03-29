# Generated by Django 2.2.7 on 2019-11-12 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tten', '0006_auto_20191112_0607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchTime', models.CharField(default='none', max_length=200)),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamone', to='tten.Team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamtwo', to='tten.Team')),
            ],
        ),
        migrations.DeleteModel(
            name='InningsData',
        ),
    ]
