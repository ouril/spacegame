# Generated by Django 3.2.5 on 2021-07-17 16:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210717_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameprofile',
            name='name',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('d260bf8c-015d-40d2-bc37-2d2452315268'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gameprofile',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('9c228ee1-963c-4c2b-bfa9-7c17d847910c'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spacemap',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('943946f9-9970-4f26-8d7d-b91fad486c33'), primary_key=True, serialize=False),
        ),
    ]
