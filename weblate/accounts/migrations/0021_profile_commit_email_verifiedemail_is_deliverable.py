# Generated by Django 4.1.3 on 2022-12-07 11:56

from django.db import migrations, models

import weblate.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0020_anonymous_auditlog"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="commit_email",
            field=weblate.utils.fields.EmailField(
                blank=True, max_length=190, verbose_name="Commit e-mail"
            ),
        ),
        migrations.AddField(
            model_name="verifiedemail",
            name="is_deliverable",
            field=models.BooleanField(default=True),
        ),
    ]
