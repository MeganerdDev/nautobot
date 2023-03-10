# Generated by Django 3.2.18 on 2023-03-10 02:06

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import nautobot.extras.models.mixins
import nautobot.ipam.models
import taggit.managers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0068_rename_model_fields"),
        ("dcim", "0037_ipam__namespaces"),
        ("ipam", "0023_delete_aggregate"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="prefix",
            options={"ordering": ("namespace", "network", "prefix_length"), "verbose_name_plural": "prefixes"},
        ),
        migrations.AlterModelOptions(
            name="vrf",
            options={"ordering": ("namespace", "name"), "verbose_name": "VRF", "verbose_name_plural": "VRFs"},
        ),
        migrations.RemoveField(
            model_name="ipaddress",
            name="vrf",
        ),
        migrations.AlterField(
            model_name="vrf",
            name="rd",
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
        migrations.CreateModel(
            name="VRFPrefixAssignment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "prefix",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="vrf_assignments", to="ipam.prefix"
                    ),
                ),
                (
                    "vrf",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="+", to="ipam.vrf"),
                ),
            ],
            options={
                "unique_together": {("vrf", "prefix")},
            },
        ),
        migrations.CreateModel(
            name="VRFDeviceAssignment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("rd", models.CharField(blank=True, max_length=21, null=True)),
                ("name", models.CharField(blank=True, max_length=100)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="vrf_assignments", to="dcim.device"
                    ),
                ),
                (
                    "vrf",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="device_assignments", to="ipam.vrf"
                    ),
                ),
            ],
            options={
                "unique_together": {("device", "rd", "name"), ("vrf", "device")},
            },
        ),
        migrations.CreateModel(
            name="Namespace",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
                ("description", models.CharField(blank=True, max_length=200)),
                (
                    "location",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="namespaces",
                        to="dcim.location",
                    ),
                ),
                ("tags", taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "abstract": False,
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
        migrations.AddField(
            model_name="prefix",
            name="namespace",
            field=models.ForeignKey(
                default=nautobot.ipam.models.get_default_namespace,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="prefixes",
                to="ipam.namespace",
            ),
        ),
        migrations.AddField(
            model_name="vrf",
            name="devices",
            field=models.ManyToManyField(related_name="vrfs", through="ipam.VRFDeviceAssignment", to="dcim.Device"),
        ),
        migrations.AddField(
            model_name="vrf",
            name="namespace",
            field=models.ForeignKey(
                default=nautobot.ipam.models.get_default_namespace,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="vrfs",
                to="ipam.namespace",
            ),
        ),
        migrations.AddField(
            model_name="vrf",
            name="prefixes",
            field=models.ManyToManyField(related_name="vrfs", through="ipam.VRFPrefixAssignment", to="ipam.Prefix"),
        ),
        migrations.AlterUniqueTogether(
            name="prefix",
            unique_together={("namespace", "network", "prefix_length")},
        ),
        migrations.AlterUniqueTogether(
            name="vrf",
            unique_together={("namespace", "rd"), ("namespace", "name")},
        ),
        migrations.RemoveField(
            model_name="prefix",
            name="vrf",
        ),
    ]
