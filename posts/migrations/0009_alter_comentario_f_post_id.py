# Generated by Django 4.0.4 on 2022-05-18 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_rename_f_post_comentario_f_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='f_post_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.post'),
        ),
    ]