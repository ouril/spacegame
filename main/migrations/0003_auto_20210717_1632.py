# Generated by Django 3.2.5 on 2021-07-17 16:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200502_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameprofile',
            name='current_order',
        ),
        migrations.RemoveField(
            model_name='gameprofile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='gameprofile',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='gameprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='region',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='region',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='spacemap',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='spacemap',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='current_params',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='params',
        ),
        migrations.AddField(
            model_name='game',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('a23a4ad9-bbf9-452f-b141-660b2dad047f'), primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='game',
            name='is_in_archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='is_in_process',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameprofile',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('f33c375e-1145-4ced-b1d8-6c664d95db97'), primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='spacemap',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('16eff900-30db-4b4e-845c-2afbbe17e8eb'), primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='unit',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='unitparams',
            name='current',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unitparams',
            name='unit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='params', to='main.unit'),
        ),
        migrations.AlterField(
            model_name='ability',
            name='unit',
            field=models.ManyToManyField(related_name='abil', to='main.Unit'),
        ),
        migrations.AlterField(
            model_name='action',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='game',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.game'),
        ),
        migrations.AlterField(
            model_name='action',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='economicunit',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='economicunit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='economicunit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='unit',
            field=models.ManyToManyField(related_name='equip', to='main.Unit'),
        ),
        migrations.AlterField(
            model_name='game',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_map',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='game', to='main.spacemap'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(blank=True, default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='gameprofile',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='gameprofile',
            name='game',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.game'),
        ),
        migrations.AlterField(
            model_name='gameprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordererror',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordererror',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='spacemap',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='unit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='location', to='main.region'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='target_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='target_location', to='main.region'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='game',
            unique_together={('name', 'id', 'game_map', 'is_in_process', 'created_on')},
        ),
        migrations.RemoveField(
            model_name='game',
            name='updated_at',
        ),
    ]