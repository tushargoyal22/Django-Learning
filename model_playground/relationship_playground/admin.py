from django.contrib import admin

# Register your models here.

from relationship_playground import models


admin.site.register([
    models.Article,
    models.Author
])