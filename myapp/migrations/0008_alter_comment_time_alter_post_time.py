
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0007_rename_postcomment_comment_post_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 4, 22, 17, 49, 35, 13510)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 4, 22, 17, 49, 35, 12510)
            ),
        ),
    ]
