from django.contrib import admin

# Register your models here.
from catalog.models import Book, Author, Genre, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book


# Define the admin class
# class AuthorAdmin(admin.ModelAdmin):
#     pass

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name','last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

admin.site.register(Book, BookAdmin)


#Register the Admin classes for BookInstance using the decorator
# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     pass
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    #list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

