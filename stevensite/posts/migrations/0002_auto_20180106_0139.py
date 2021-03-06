# Generated by Django 2.0.1 on 2018-01-06 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('name_text', models.CharField(default='name', max_length=20, primary_key=True, serialize=False)),
                ('title_text', models.CharField(default='title', max_length=200)),
                ('subtitle_text', models.CharField(default='subtitle', max_length=200)),
                ('author_text', models.CharField(default='author_name', max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
