# Generated by Django 5.0.7 on 2024-07-29 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_baocaodoanhthu_options_alter_ca_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('gmail', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'mail',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='chitietbaocao',
            name='mabaocao',
        ),
        migrations.DeleteModel(
            name='Ca',
        ),
        migrations.DeleteModel(
            name='Chitietdichvu',
        ),
        migrations.DeleteModel(
            name='ChitietDvThanhtoan',
        ),
        migrations.DeleteModel(
            name='Chitietmonan',
        ),
        migrations.DeleteModel(
            name='Chucvu',
        ),
        migrations.DeleteModel(
            name='Congviec',
        ),
        migrations.DeleteModel(
            name='Dichvu',
        ),
        migrations.DeleteModel(
            name='Hoadon',
        ),
        migrations.DeleteModel(
            name='Loaimonan',
        ),
        migrations.DeleteModel(
            name='Loaisanh',
        ),
        migrations.DeleteModel(
            name='Monan',
        ),
        migrations.DeleteModel(
            name='Nhanvien',
        ),
        migrations.DeleteModel(
            name='Phancong',
        ),
        migrations.DeleteModel(
            name='Phieudattieccuoi',
        ),
        migrations.DeleteModel(
            name='Sanh',
        ),
        migrations.DeleteModel(
            name='Taikhoan',
        ),
        migrations.DeleteModel(
            name='Thamso',
        ),
        migrations.DeleteModel(
            name='Baocaodoanhthu',
        ),
        migrations.DeleteModel(
            name='Chitietbaocao',
        ),
    ]
