# Generated by Django 4.0.4 on 2022-05-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_alter_filmwork_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personfilmwork',
            name='role',
            field=models.CharField(choices=[('producer', 'Producer'), ('actor', 'Actor'), ('screenwriter', 'Screenwriter')], max_length=15, null=True, verbose_name='role'),
        ),
        migrations.AddIndex(
            model_name='filmwork',
            index=models.Index(fields=['title'], name='title_idx'),
        ),
        migrations.AddIndex(
            model_name='filmwork',
            index=models.Index(fields=['rating'], name='rating_idx'),
        ),
        migrations.AddIndex(
            model_name='filmwork',
            index=models.Index(fields=['type'], name='type_idx'),
        ),
        migrations.AddIndex(
            model_name='genre',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['full_name'], name='full_name_idx'),
        ),
    ]
