# Generated by Django 2.2.6 on 2019-11-15 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('administrator_id', models.AutoField(primary_key=True, serialize=False)),
                ('administrator_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.BigIntegerField(unique=True)),
                ('Address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('no_booksverified', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=10)),
                ('semester', models.CharField(max_length=1)),
                ('price', models.SmallIntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.BigIntegerField(unique=True)),
                ('Address', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('books_bought', models.SmallIntegerField()),
                ('books_on_sale', models.SmallIntegerField()),
                ('books_sold', models.SmallIntegerField()),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Customer')),
                ('payment_method_1', models.CharField(max_length=1)),
                ('payment_method_2', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='websitelogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Books_buying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('paymentmethod_selected', models.CharField(max_length=1)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Books')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Customer')),
                ('seller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Sellers')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Sellers'),
        ),
    ]
