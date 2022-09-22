# Generated by Django 3.2.12 on 2022-09-22 10:46

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_alter_takencourse_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('url', embed_video.fields.EmbedVideoField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='article.article', verbose_name='Article')),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
