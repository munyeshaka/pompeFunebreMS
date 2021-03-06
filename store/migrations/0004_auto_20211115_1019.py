# Generated by Django 3.2.8 on 2021-11-15 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20211110_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=150)),
                ('phoneClient', models.CharField(max_length=50)),
                ('feu', models.CharField(max_length=150)),
                ('ne', models.DateField(null=True)),
                ('decede', models.DateField(null=True)),
                ('dateCeremony', models.DateField(null=True)),
                ('morge', models.CharField(blank=True, default='', max_length=50)),
                ('total_amt', models.FloatField()),
                ('total_rest', models.FloatField()),
                ('paid_status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': '4. Les Commandes',
            },
        ),
        migrations.CreateModel(
            name='CartOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=150)),
                ('item', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=150)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cartorder')),
            ],
            options={
                'verbose_name_plural': '5. Les élément de commande',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '2. Categories'},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name_plural': '1. Caisier'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': '3. Produits'},
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='cartorder',
            name='caisier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer'),
        ),
    ]
