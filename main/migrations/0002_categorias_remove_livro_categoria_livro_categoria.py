# Generated by Django 4.1.7 on 2023-03-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(choices=[('ROMANCE', 'Romance'), ('FICÇÃO', 'Ficção'), ('AUTOAJUDA', 'Autoajuda'), ('CIENTÍFICO', 'Científico'), ('RELIGIÃO', 'Religião')], max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='livro',
            name='categoria',
        ),
        migrations.AddField(
            model_name='livro',
            name='categoria',
            field=models.ManyToManyField(to='main.categorias'),
        ),
    ]
