# Generated by Django 4.1.7 on 2023-03-05 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=True, null=True, upload_to='capas_livros')),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=30)),
                ('categoria', models.CharField(choices=[('ROMANCE', 'Romance'), ('FICÇÃO', 'Ficção'), ('AUTOAJUDA', 'Autoajuda'), ('CIENTÍFICO', 'Científico'), ('RELIGIÃO', 'Religião')], max_length=30)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.perfil')),
            ],
        ),
    ]
