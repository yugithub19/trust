# Generated by Django 3.1.1 on 2020-10-03 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rope', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cow',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rope.milk'),
        ),
        migrations.CreateModel(
            name='Buffalo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rope.milk')),
            ],
        ),
    ]
