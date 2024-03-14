# Generated by Django 4.2.9 on 2024-03-12 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.UUIDField()),
                ('token', models.CharField(max_length=255, unique=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='SiteSupportService',
            fields=[
                ('thirdparty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='third_party.thirdparty')),
                ('type', models.CharField(choices=[('Goftino', 'Goftino'), ('Crisp', 'Crisp')], max_length=25)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('third_party.thirdparty',),
        ),
        migrations.CreateModel(
            name='SMSService',
            fields=[
                ('thirdparty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='third_party.thirdparty')),
                ('type', models.CharField(choices=[('Kavenegar', 'Kavenegar')], max_length=25)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('third_party.thirdparty',),
        ),
    ]