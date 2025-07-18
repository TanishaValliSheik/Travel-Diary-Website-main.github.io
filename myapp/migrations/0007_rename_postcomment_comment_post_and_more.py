

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0006_alter_comment_time_alter_post_time"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="postcomment", new_name="post",
        ),
        migrations.RenameField(
            model_name="post", old_name="userpost", new_name="user",
        ),
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 4, 22, 17, 49, 13, 782667)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 4, 22, 17, 49, 13, 782667)
            ),
        ),
    ]
