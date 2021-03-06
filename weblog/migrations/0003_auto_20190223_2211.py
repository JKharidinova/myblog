# Generated by Django 2.1.5 on 2019-02-23 19:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0002_auto_20190221_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='posts',
            name='blogs',
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
