
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("myapp", "0009_alter_comment_time_alter_post_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.CharField(blank=True, default="23 April 2023", max_length=100),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.CharField(blank=True, default="23 April 2023", max_length=100),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/profile"),
        ),
    ]
