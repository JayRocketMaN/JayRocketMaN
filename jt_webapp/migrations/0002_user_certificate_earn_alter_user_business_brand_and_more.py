# Generated by Django 5.1.4 on 2024-12-11 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jt_webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='certificate_earn',
            field=models.ImageField(default='company', upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='business_brand',
            field=models.CharField(default='intern', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='business_name',
            field=models.CharField(default='intern', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='tech_school_you_graduated_from',
            field=models.CharField(default='company', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='tech_skill',
            field=models.CharField(default='company', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='what_can_we_offer',
            field=models.CharField(default='intern', max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='why_should_we_onboard_you',
            field=models.CharField(default='company', max_length=300),
        ),
    ]
