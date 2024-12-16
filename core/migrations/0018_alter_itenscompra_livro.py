# Generated by Django 5.1.4 on 2024-12-16 12:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_compra_tipo_pagamento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itenscompra",
            name="livro",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="itens_compra", to="core.livro"
            ),
        ),
    ]
