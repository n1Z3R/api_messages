# Generated by Django 4.0.4 on 2022-05-11 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MessageConfirmationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('r', 'review'), ('b', 'blocked'), ('c', 'correct')], default='r', max_length=50)),
                ('message_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messagesapp.messagemodel')),
            ],
        ),
    ]
