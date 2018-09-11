# Generated by Django 2.1.1 on 2018-09-11 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('created_date', models.DateTimeField(verbose_name='date published')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.Question')),
            ],
        ),
    ]
