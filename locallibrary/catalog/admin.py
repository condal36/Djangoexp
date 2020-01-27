from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance
'''
注意：如果你在上一章節最後有接受挑戰並建立一個書本的「語言模型」 (查看模型教學文章)，你必需也要導入並註冊該模型！
'''




admin.site.register(Genre)
#admin.site.register(Book)
#admin.site.register(BookInstance)
# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

#admin.site.register(Author)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ( 'first_name','last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)