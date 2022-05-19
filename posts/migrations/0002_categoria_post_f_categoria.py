# Generated by Django 4.0.4 on 2022-05-14 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Tittle')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='f_categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.categoria'),
        ),
    ]
