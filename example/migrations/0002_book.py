# Generated by Django 4.1.6 on 2023-02-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('thumbnail', models.ImageField(upload_to='book_thumbnails')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('categories', models.CharField(choices=[('DEVEVELOPPEMENT_PERSONNEL', 'développement personnel'), ('PHILOSOPHIE', 'philosophie'), ('FINANCE', 'finance'), ('BUISNESS', 'buisness')], max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
                ('amazon_link', models.URLField()),
                ('youtube_link', models.URLField()),
                ('notes', models.TextField()),
            ],
        ),
    ]
