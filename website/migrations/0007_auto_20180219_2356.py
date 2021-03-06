# Generated by Django 2.0 on 2018-02-19 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0006_auto_20180218_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='twoja kategoria', max_length=300, verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=300, verbose_name='usługa')),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20, verbose_name='cena')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_items', to='website.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.AlterField(
            model_name='list',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
