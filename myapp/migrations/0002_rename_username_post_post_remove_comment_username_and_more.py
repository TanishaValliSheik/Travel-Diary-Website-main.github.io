
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post", old_name="username", new_name="post",
        ),
        migrations.RemoveField(model_name="comment", name="username",),
        migrations.AddField(
            model_name="comment",
            name="comment",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="myapp.post"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.CharField(max_length=100000),
        ),
    ]
