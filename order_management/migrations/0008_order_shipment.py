

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shipment_management', '0001_initial'),
        ('order_management', '0007_remove_order_shipment_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipment',
            field=models.ManyToManyField(to='Shipment_management.Shipment'),
        ),
    ]

