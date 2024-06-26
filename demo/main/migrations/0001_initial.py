# Generated by Django 4.2.3 on 2023-07-14 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='launch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_time', models.DateTimeField()),
                ('reentry_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('launched', 'Launched'), ('postponed', 'Postponed'), ('ready', 'Ready'), ('development', 'Maintainance')], max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Launches',
            },
        ),
        migrations.CreateModel(
            name='rocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('model', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('development', 'Development'), ('integration', 'Integration'), ('testing', 'Testing'), ('ready', 'Ready'), ('development', 'Maintainance')], max_length=255)),
                ('build_start', models.DateTimeField()),
                ('build_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='payload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('weight', models.FloatField(help_text='in Tonnes')),
                ('launch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.launch')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer')),
            ],
        ),
        migrations.AddField(
            model_name='launch',
            name='rockets',
            field=models.ManyToManyField(blank=True, to='main.rocket'),
        ),
    ]
