# Generated by Django 4.0.5 on 2022-07-01 16:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dp', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='profileImages/avater.jpeg', force_format='JPEG', keep_meta=False, quality=75, scale=None, size=[200, 200], upload_to='profileImages', verbose_name='profile picture')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='contact_mail')),
                ('contact_number', models.CharField(max_length=11)),
                ('city', models.CharField(choices=[('Bagerhat', 'bagerhat'), ('Bandarban', 'bandarban'), ('Barguna', 'barguna'), ('Barisal', 'barisal'), ('Bhola', 'bhola'), ('Bogura', 'bogura'), ('Brahmanbaria', 'brahmanbaria'), ('Chandpur', 'chandpur'), ('Chapainawabganj', 'chapainawabganj'), ('Chattogram', 'chattogram'), ('Chuadanga', 'chuadanga'), ("Cox's Bazar", "cox's bazar"), ('Cumilla', 'cumilla'), ('Dhaka', 'dhaka'), ('Dinajpur', 'dinajpur'), ('Faridpur', 'faridpur'), ('Feni', 'feni'), ('Gaibandha', 'gaibandha'), ('Gazipur', 'gazipur'), ('Gopalganj', 'gopalganj'), ('Habiganj', 'habiganj'), ('Jamalpur', 'jamalpur'), ('Jessore', 'jessore'), ('Jhalokati', 'jhalokati'), ('Jhenaidah', 'jhenaidah'), ('Joypurhat', 'joypurhat'), ('Khagrachhari', 'khagrachhari'), ('Khulna', 'khulna'), ('Kishoreganj', 'kishoreganj'), ('Kurigram', 'kurigram'), ('Kushtia', 'kushtia'), ('Lakshmipur', 'lakshmipur'), ('Lalmonirhat', 'lalmonirhat'), ('Madaripur', 'madaripur'), ('Magura', 'magura'), ('Manikganj', 'manikganj'), ('Meherpur', 'meherpur'), ('Moulvibazar', 'moulvibazar'), ('Munshiganj', 'munshiganj'), ('Mymensingh', 'mymensingh'), ('Naogaon', 'naogaon'), ('Narail', 'narail'), ('Narayanganj', 'narayanganj'), ('Narsingdi', 'narsingdi'), ('Natore', 'natore'), ('Netrokona', 'netrokona'), ('Nilphamari', 'nilphamari'), ('Noakhali', 'noakhali'), ('Pabna', 'pabna'), ('Panchagarh', 'panchagarh'), ('Patuakhali', 'patuakhali'), ('Pirojpur', 'pirojpur'), ('Rajbari', 'rajbari'), ('Rajshahi', 'rajshahi'), ('Rangamati', 'rangamati'), ('Rangpur', 'rangpur'), ('Satkhira', 'satkhira'), ('Shariatpur', 'shariatpur'), ('Sherpur', 'sherpur'), ('Sirajganj', 'sirajganj'), ('Sunamganj', 'sunamganj'), ('Sylhet', 'sylhet'), ('Tangail', 'tangail'), ('Thakurgaon', 'thakurgaon')], max_length=20)),
                ('blood_group', models.CharField(choices=[('a+', 'A(+ve)'), ('a-', 'A(-ve)'), ('b+', 'B(+ve)'), ('b-', 'B(-ve)'), ('ab+', 'AB(+ve)'), ('ab-', 'AB(-ve)'), ('o+', 'O(+ve)'), ('o-', 'O(-ve)')], max_length=8)),
                ('bio', models.CharField(blank=True, max_length=300, null=True)),
                ('fb_profile_link', models.CharField(blank=True, max_length=150, null=True)),
                ('whatsapp_number', models.CharField(blank=True, max_length=11, null=True)),
                ('department', models.CharField(blank=True, max_length=250, null=True)),
                ('last_donated', models.DateTimeField(auto_now_add=True)),
                ('avaiable', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonorProfile',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profiles.profile')),
                ('year', models.CharField(choices=[('1st', 'First Year'), ('2nd', 'Second Year'), ('3rd', 'Third Year'), ('4th', 'Fourth Year'), ('ms', 'Masters'), ('grad', 'Graduated')], max_length=5)),
                ('hobbies', models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[, a-zA-Z]*$', 'Separate with comma.', code='invalid')])),
                ('current_status', models.CharField(choices=[('stu', 'Student'), ('job', 'Job Holder'), ('unemployed', 'Unemployed')], max_length=20)),
                ('job_title', models.CharField(blank=True, max_length=60, null=True)),
                ('job_location', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='donor_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profiles(donor)',
            },
            bases=('profiles.profile',),
        ),
    ]
