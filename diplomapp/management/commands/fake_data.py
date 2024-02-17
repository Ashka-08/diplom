import random
import datetime
from django.core.management.base import BaseCommand
from diplomapp.models import User, Product, Order, Status, SubCategory, Unit

SIMBOLS = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ1234567890'

class Command(BaseCommand):
    help = 'Generate fake data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count users, orders and product')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        units = Unit.objects.all()
        sub_categories = SubCategory.objects.all()
        statuses = Status.objects.all()
        date = datetime.datetime.now().strftime('%d.%m.%Y')
        time = datetime.datetime.now().strftime('%H:%M')

        # Generate fake products
        for j in range(1, count + 1):
            product = Product(name=f'product_{j}',
                              description=f'description_{j}',
                              price=random.randint(1, 100),
                              unit=random.choice(units),
                              sub_category=random.choice(sub_categories))
            product.save()
        
        # Generate fake users
        for i in range(1, count + 1):
            user = User(name=f'user{i}',
                        email=f'user{i}@mail.com',
                        phone_number=f'8{random.randint(9000000000,10000000000)}')
            user.save()

        # Generate fake orders
        for i in range(1, count + 1):
            user = User.objects.filter(pk=i).first()
            for _ in range(1, random.randint(1, count)):
                total_price = 0
                order = Order(
                    order_number=''.join(random.choices(SIMBOLS, k=6)),
                    user=user,
                    date=date,
                    time=time,
                    status=random.choice(statuses)
                )
                for _ in range(1, random.randint(1, count)):
                    product = Product.objects.filter(pk=random.randint(1, count)).first()
                    total_price += product.price
                    order.total_price = total_price
                    order.save()
                    order.products.add(product)
