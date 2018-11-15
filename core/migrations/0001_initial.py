# Generated by Django 2.1.3 on 2018-11-10 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enderecos', '0001_initial'),
        ('atracao', '0001_initial'),
        ('avaliacao', '0001_initial'),
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('aprovado', models.BooleanField(default=False)),
                ('atracao', models.ManyToManyField(to='atracao.Atracao')),
                ('avaliacao', models.ManyToManyField(to='avaliacao.Avaliacao')),
                ('comentarios', models.ManyToManyField(to='comentarios.Comentarios')),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.Enderecos')),
            ],
        ),
    ]
