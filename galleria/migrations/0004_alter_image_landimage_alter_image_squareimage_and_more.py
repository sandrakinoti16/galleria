# Generated by Django 4.0 on 2022-05-30 11:50

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0003_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='landImage',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_land.jpg', force_format=None, keep_meta=True, quality=75, size=[2878, 1618], upload_to='landscape'),
        ),
        migrations.AlterField(
            model_name='image',
            name='squareImage',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_square.jpg', force_format=None, keep_meta=True, quality=75, size=[1000, 1000], upload_to='square'),
        ),
        migrations.AlterField(
            model_name='image',
            name='tallImage',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_tall.jpg', force_format=None, keep_meta=True, quality=75, size=[1618, 2878], upload_to='tall'),
        ),
    ]
