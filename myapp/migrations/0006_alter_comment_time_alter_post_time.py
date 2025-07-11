
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_alter_comment_time_alter_post_likes_alter_post_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 4, 22, 17, 47, 53, 666251)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 4, 22, 17, 47, 53, 666251)
            ),
        ),
    ]
