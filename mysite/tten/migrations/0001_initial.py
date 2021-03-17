# Generated by Django 2.2.7 on 2019-11-11 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=200)),
                ('played', models.IntegerField()),
                ('won', models.IntegerField()),
                ('draw', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('dept_id', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('run', models.IntegerField()),
                ('wicket', models.IntegerField()),
                ('played', models.IntegerField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tten.Team')),
            ],
        ),
    ]
