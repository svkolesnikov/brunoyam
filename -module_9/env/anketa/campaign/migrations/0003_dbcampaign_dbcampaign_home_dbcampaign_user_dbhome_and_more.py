# Generated by Django 4.2.2 on 2023-08-09 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_rename_bdcompany_dbcompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Кампания',
                'verbose_name_plural': 'Кампании',
            },
        ),
        migrations.CreateModel(
            name='DBCampaign_home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Связь',
                'verbose_name_plural': 'Связь Кампании с домом',
            },
        ),
        migrations.CreateModel(
            name='DBCampaign_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Связь',
                'verbose_name_plural': 'Связь Кампании с пользователем',
            },
        ),
        migrations.CreateModel(
            name='DBHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
        ),
        migrations.CreateModel(
            name='DBState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Реакция',
                'verbose_name_plural': 'Реакции жильцов',
            },
        ),
        migrations.RenameModel(
            old_name='DbCompany',
            new_name='DBAnketa',
        ),
        migrations.AlterModelOptions(
            name='dbanketa',
            options={'verbose_name': 'Анкета', 'verbose_name_plural': 'Анкеты'},
        ),
    ]
