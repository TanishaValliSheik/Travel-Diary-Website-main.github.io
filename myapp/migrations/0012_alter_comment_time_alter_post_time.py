
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0011_delete_userinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="time",
            field=models.CharField(blank=True, default="09 May 2023", max_length=100),
        ),
        migrations.AlterField(
            model_name="post",
            name="time",
            field=models.CharField(blank=True, default="09 May 2023", max_length=100),
        ),
    ]
