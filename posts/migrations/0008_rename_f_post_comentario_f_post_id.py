# Generated by Django 4.0.4 on 2022-05-18 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_comentario_fechacomentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='f_post',
            new_name='f_post_id',
        ),
    ]
