# Generated by Django 4.2.6 on 2023-10-15 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_profile_createdat_profile_updatedat"),
        ("records", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="profile",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="profiles.profile",
            ),
            preserve_default=False,
        ),
    ]