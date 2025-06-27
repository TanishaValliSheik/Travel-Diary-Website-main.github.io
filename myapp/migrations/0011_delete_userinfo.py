
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0010_comment_user_alter_comment_time_alter_post_time_and_more"),
    ]

    operations = [
        migrations.DeleteModel(name="UserInfo",),
    ]
