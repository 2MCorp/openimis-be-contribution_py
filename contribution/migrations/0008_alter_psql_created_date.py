from django.db import migrations, models
from django.conf import settings

from datetime import datetime


class Migration(migrations.Migration):
    dependencies = [
        ('contribution', '0007_add_missing_fields_not_mssql'),
    ]
    operations = []
    # For MSSQL These changes were added through raw sql, to keep consistency with existing databases it couldn't be
    # changed in postgres sql script.
    
    if not settings.MSSQL:
        operations.append(
            migrations.AlterField(
                model_name='premium',
                name='created_date',
                field=models.DateTimeField(db_column='CreatedDate', default=datetime.now()),
            ))
        
