# Generated by Django 4.0.4 on 2022-05-18 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_rename_f_post_id_comentario_idpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='idPost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
        ),
    ]
