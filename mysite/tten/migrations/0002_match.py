# Generated by Django 2.2.7 on 2019-11-11 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tten', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1run', models.IntegerField()),
                ('team1wkt', models.IntegerField()),
                ('team2run', models.IntegerField()),
                ('tea2wkt', models.IntegerField()),
                ('t1b1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tten.Player')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batfirst', to='tten.Team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batlast', to='tten.Team')),
                ('tosswon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tosswon', to='tten.Team')),
            ],
        ),
    ]
