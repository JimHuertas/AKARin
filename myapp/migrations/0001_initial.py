# Generated by Django 3.0.8 on 2020-07-18 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('tipo', models.CharField(max_length=20)),
                ('loaded', models.DateTimeField(auto_now_add=True)),
                ('tag', models.CharField(max_length=20)),
                ('doc', models.FileField(upload_to='myapp/uploads/')),
            ],
            options={
                'verbose_name': 'documento',
                'verbose_name_plural': 'documentos',
            },
        ),
    ]
