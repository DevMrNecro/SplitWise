# Generated by Django 4.2.7 on 2024-01-02 11:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricityBill',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('bill_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expense_type', models.CharField(blank=True, max_length=10, null=True)),
                ('remaining_ammount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('deadline', models.DateField(blank=True, unique=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('room_no', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseParticipants',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('expense_type', models.CharField(choices=[('EXACT', 'EXACT'), ('EQUAL', 'EQUAL'), ('EQUAL', 'EQUAL')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deadline_to_payees', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('electricity_bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.electricitybill')),
                ('participant', models.ManyToManyField(related_name='participants', to='core.user')),
                ('payee_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payee', to='core.user')),
            ],
        ),
        migrations.AddField(
            model_name='electricitybill',
            name='paid_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
        migrations.AddField(
            model_name='electricitybill',
            name='payees',
            field=models.ManyToManyField(related_name='payees', to='core.user'),
        ),
        migrations.AddField(
            model_name='electricitybill',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.room'),
        ),
        migrations.AddField(
            model_name='electricitybill',
            name='splited_amongst',
            field=models.ManyToManyField(blank=True, related_name='splited_amongst', to='core.user'),
        ),
    ]
