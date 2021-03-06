# Generated by Django 4.0.5 on 2022-07-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avaiable',
            new_name='available',
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(choices=[('bagerhat', 'Bagerhat'), ('bandarban', 'Bandarban'), ('barguna', 'Barguna'), ('barisal', 'Barisal'), ('bhola', 'Bhola'), ('bogura', 'Bogura'), ('brahmanbaria', 'Brahmanbaria'), ('chandpur', 'Chandpur'), ('chapainawabganj', 'Chapainawabganj'), ('chattogram', 'Chattogram'), ('chuadanga', 'Chuadanga'), ("cox's bazar", "Cox's Bazar"), ('cumilla', 'Cumilla'), ('dhaka', 'Dhaka'), ('dinajpur', 'Dinajpur'), ('faridpur', 'Faridpur'), ('feni', 'Feni'), ('gaibandha', 'Gaibandha'), ('gazipur', 'Gazipur'), ('gopalganj', 'Gopalganj'), ('habiganj', 'Habiganj'), ('jamalpur', 'Jamalpur'), ('jessore', 'Jessore'), ('jhalokati', 'Jhalokati'), ('jhenaidah', 'Jhenaidah'), ('joypurhat', 'Joypurhat'), ('khagrachhari', 'Khagrachhari'), ('khulna', 'Khulna'), ('kishoreganj', 'Kishoreganj'), ('kurigram', 'Kurigram'), ('kushtia', 'Kushtia'), ('lakshmipur', 'Lakshmipur'), ('lalmonirhat', 'Lalmonirhat'), ('madaripur', 'Madaripur'), ('magura', 'Magura'), ('manikganj', 'Manikganj'), ('meherpur', 'Meherpur'), ('moulvibazar', 'Moulvibazar'), ('munshiganj', 'Munshiganj'), ('mymensingh', 'Mymensingh'), ('naogaon', 'Naogaon'), ('narail', 'Narail'), ('narayanganj', 'Narayanganj'), ('narsingdi', 'Narsingdi'), ('natore', 'Natore'), ('netrokona', 'Netrokona'), ('nilphamari', 'Nilphamari'), ('noakhali', 'Noakhali'), ('pabna', 'Pabna'), ('panchagarh', 'Panchagarh'), ('patuakhali', 'Patuakhali'), ('pirojpur', 'Pirojpur'), ('rajbari', 'Rajbari'), ('rajshahi', 'Rajshahi'), ('rangamati', 'Rangamati'), ('rangpur', 'Rangpur'), ('satkhira', 'Satkhira'), ('shariatpur', 'Shariatpur'), ('sherpur', 'Sherpur'), ('sirajganj', 'Sirajganj'), ('sunamganj', 'Sunamganj'), ('sylhet', 'Sylhet'), ('tangail', 'Tangail'), ('thakurgaon', 'Thakurgaon')], max_length=20),
        ),
    ]
