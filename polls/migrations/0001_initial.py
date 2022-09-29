# Generated by Django 3.2.12 on 2022-09-27 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_date', models.DateTimeField(auto_now=True)),
                ('organization', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Sometimes', 'Sometimes'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=225, verbose_name='Course organizaiton was?')),
                ('contribution', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Sometimes', 'Sometimes'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=225, verbose_name="The instructor's contribution to the course was?")),
                ('course_content', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Sometimes', 'Sometimes'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=225, verbose_name='The course content was?')),
                ('general', models.CharField(choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Sometimes', 'Sometimes'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=225, verbose_name='The course as awhole was?')),
                ('feedback', models.TextField(blank=True, verbose_name='Any other feedback')),
                ('article_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='article.article', verbose_name='course name')),
            ],
            options={
                'verbose_name': 'Poll',
            },
        ),
    ]
