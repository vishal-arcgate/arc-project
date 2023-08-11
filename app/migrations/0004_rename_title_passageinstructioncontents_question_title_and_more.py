# Generated by Django 4.1.4 on 2023-01-25 06:22

import app.utility.question_module_functions
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20230106_0710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passageinstructioncontents',
            old_name='title',
            new_name='question_title',
        ),
        migrations.RenameField(
            model_name='subjectivequestions',
            old_name='question',
            new_name='question_title',
        ),
        migrations.RemoveField(
            model_name='excelquestions',
            name='excel_title',
        ),
        migrations.AddField(
            model_name='excelquestions',
            name='question_title',
            field=models.CharField(default=1, max_length=200, validators=[app.utility.question_module_functions.validate_check_null]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='excelquestions',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, validators=[app.utility.question_module_functions.validate_check_null]),
        ),
        migrations.AlterField(
            model_name='excelquestions',
            name='description',
            field=models.CharField(max_length=500, validators=[app.utility.question_module_functions.validate_check_null]),
        ),
        migrations.AlterField(
            model_name='excelquestions',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.allquestions', validators=[app.utility.question_module_functions.validate_check_null]),
        ),
        migrations.AlterField(
            model_name='excelquestions',
            name='sheet_id',
            field=models.CharField(max_length=1000, validators=[app.utility.question_module_functions.validate_check_null]),
        ),
        migrations.AlterField(
            model_name='excelquestions',
            name='type',
            field=models.CharField(default='Excel', max_length=50, validators=[app.utility.question_module_functions.validate_check_null]),
        ),
    ]
