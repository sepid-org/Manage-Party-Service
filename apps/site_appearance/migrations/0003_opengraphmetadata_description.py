# Generated by Django 4.2.9 on 2024-02-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_appearance', '0002_headerdata_opengraphmetadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='opengraphmetadata',
            name='description',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]