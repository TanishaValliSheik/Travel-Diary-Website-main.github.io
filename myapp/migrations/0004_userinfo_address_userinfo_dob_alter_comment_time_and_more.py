

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_rename_comment_comment_postcomment_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="address",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userinfo",
            name="dob",
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 4, 22, 17, 43, 44, 866459)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 4, 22, 17, 43, 44, 865459)
            ),
        ),
    ]
