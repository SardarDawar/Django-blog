# Generated by Django 2.2 on 2019-04-25 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0020_blogreply'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='reply',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blogs.BlogComment'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BlogReply',
        ),
    ]
