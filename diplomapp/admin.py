from django.contrib import admin
from diplomapp.models import User, Product, Order, Category, SubCategory, Unit, Status


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'price']
    ordering = ['price']
    list_filter = ['price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    """Отдельный продукт."""
    fields = ['name', 'description', 'price', 'unit', 'sub_category', 'foto']


class UserAdmin(admin.ModelAdmin):
    """Список пользователей."""
    list_display = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Имя (name)'
    """Отдельный пользователь."""
    fields = ['name', 'email', 'phone_number']


class UnitAdmin(admin.ModelAdmin):
    """Список единиц измерения."""
    list_display = ['unit_of_measurement']
    search_fields = ['unit_of_measurement']
    search_help_text = 'Поиск по полю Название (unit_of_measurement)'
    """Отдельный единица измерения."""
    fields = ['unit_of_measurement']


class CategoryAdmin(admin.ModelAdmin):
    """Список категорий."""
    list_display = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Название (name)'
    """Отдельный категория."""
    fields = ['name', 'picture']


class SubCategoryAdmin(admin.ModelAdmin):
    """Список дочерних категорий."""
    list_display = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю Название (name)'
    """Отдельный дочерняя категория."""
    fields = ['name', 'picture', 'category']


class StatusAdmin(admin.ModelAdmin):
    """Список статусов."""
    list_display = ['status']
    search_fields = ['status']
    search_help_text = 'Поиск по полю Название (status)'
    """Отдельный статус."""
    fields = ['status']


class OrderAdmin(admin.ModelAdmin):
    """Список заказов."""
    list_display = ['pk', 'order_number', 'date', 'time', 'total_price', 'user']
    ordering = ['-total_price']
    list_filter = ['user', 'total_price', 'order_number']
    """Отдельный заказ."""
    fields = ['order_number', 'total_price', 'user', 'products', 'status']
    readonly_fields = ['date', 'time']


admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Status, StatusAdmin)

