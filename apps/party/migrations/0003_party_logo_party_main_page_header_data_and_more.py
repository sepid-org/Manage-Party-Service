# Generated by Django 4.2.9 on 2024-02-20 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_appearance', '0002_headerdata_opengraphmetadata'),
        ('party', '0002_partydomain'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='logo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='party', to='site_appearance.logo'),
        ),
        migrations.AddField(
            model_name='party',
            name='main_page_header_data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='party', to='site_appearance.headerdata'),
        ),
        migrations.AddField(
            model_name='party',
            name='main_page_og_metadata',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='party', to='site_appearance.opengraphmetadata'),
        ),
    ]
