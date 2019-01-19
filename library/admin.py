from django.contrib import admin

# Register your models here.

from library.models import Book, Copy, Loan, Configuration

admin.site.register(Book)
admin.site.register(Copy)
admin.site.register(Loan)
admin.site.register(Configuration)
