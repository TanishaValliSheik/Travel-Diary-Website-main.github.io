
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_comment_time_alter_post_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('email', models.EmailField(max_length=600)),
                ('subject', models.CharField(max_length=1000)),
                ('message', models.CharField(blank=True, max_length=10000)),
            ],
        ),
    ]
