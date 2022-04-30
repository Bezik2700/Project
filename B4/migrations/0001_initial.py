# Generated by Django 3.0.8 on 2021-08-09 05:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultDeductions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('house', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Жильё')),
                ('travel', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Проезд')),
                ('phone', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Телефон')),
                ('food', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Еда')),
            ],
            options={
                'verbose_name': 'Стандартные вычеты',
                'verbose_name_plural': 'Стандартные вычеты',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('image', models.ImageField(blank=True, null=True, upload_to='foto/%Y/%m/%d', verbose_name='Фотоверсия')),
            ],
            options={
                'verbose_name': 'Заметки',
                'verbose_name_plural': 'Заметки',
                'ordering': ['-created_at', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Название плана')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'План',
                'verbose_name_plural': 'Планы',
                'ordering': ['-created_at', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('name', models.CharField(max_length=255, verbose_name='Название раздела')),
                ('is_active', models.BooleanField(verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
                'ordering': ['is_active', '-created_at', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_ready', models.BooleanField(verbose_name='Выполнено')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='B4.Plan', verbose_name='План')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='B4.Section', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'ordering': ['-created_at', '-id'],
            },
        ),
        migrations.CreateModel(
            name='DefaultTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_ready', models.BooleanField(verbose_name='Выполнено')),
                ('is_default', models.BooleanField(verbose_name='Задача по умолчанию')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='B4.Plan', verbose_name='План')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='B4.Section', verbose_name='Секция')),
            ],
            options={
                'verbose_name': 'Задача по умолчанию',
                'verbose_name_plural': 'Задачи по умолчанию',
                'ordering': ['is_default', '-created_at', '-id'],
            },
        ),
    ]
