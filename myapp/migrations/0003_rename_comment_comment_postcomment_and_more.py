
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_rename_username_post_post_remove_comment_username_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment", old_name="comment", new_name="postcomment",
        ),
        migrations.RenameField(
            model_name="post", old_name="post", new_name="userpost",
        ),
    ]
