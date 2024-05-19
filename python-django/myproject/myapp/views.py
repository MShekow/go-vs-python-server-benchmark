from django.http import JsonResponse
from django.views import View

from .models import Products, ProductsSerializer


class ProductsView(View):
    async def get(self, request):
        products = [p async for p in Products.objects.all()]
        serializer = ProductsSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


class CreateProductsView(View):
    def get(self, request):
        count = Products.objects.count()
        if count == 0:
            Products(Name='Widget A', Description='A useful widget', Price=19.99, StockQuantity=100,
                     Category='Widgets').save()
            Products(Name='Widget B', Description='Another useful widget', Price=25.99,
                     StockQuantity=150,
                     Category='Widgets').save()
            Products(Name='Gadget A', Description='A nifty gadget', Price=29.99, StockQuantity=200,
                     Category='Gadgets').save()
            Products(Name='Gadget B', Description='Another nifty gadget', Price=35.99, StockQuantity=90,
                     Category='Gadgets').save()
            Products(Name='Tool A', Description='An indispensable tool', Price=9.99, StockQuantity=80,
                     Category='Tools').save()
            Products(Name='Tool B', Description='Another indispensable tool', Price=14.99,
                     StockQuantity=120, Category='Tools').save()
            Products(Name='Device A', Description='A vital device', Price=199.99, StockQuantity=40,
                     Category='Devices').save()
            Products(Name='Device B', Description='Another vital device', Price=249.99, StockQuantity=50,
                     Category='Devices').save()
            Products(Name='Appliance A', Description='A necessary appliance', Price=79.99,
                     StockQuantity=75, Category='Appliances').save()
            Products(Name='Appliance B', Description='Another necessary appliance', Price=89.99,
                     StockQuantity=65, Category='Appliances').save()
            Products(Name='Gizmo A', Description='A handy gizmo', Price=4.99, StockQuantity=200,
                     Category='Gizmos').save()
            Products(Name='Gizmo B', Description='Another handy gizmo', Price=6.99, StockQuantity=300,
                     Category='Gizmos').save()
            Products(Name='Thingamajig A', Description='A useful thingamajig', Price=1.99,
                     StockQuantity=500, Category='Thingamajigs').save()
            Products(Name='Thingamajig B', Description='Another useful thingamajig', Price=2.99,
                     StockQuantity=600, Category='Thingamajigs').save()
            Products(Name='Doodad A', Description='A necessary doodad', Price=0.99, StockQuantity=700,
                     Category='Doodads').save()
            Products(Name='Doodad B', Description='Another necessary doodad', Price=1.49,
                     StockQuantity=800, Category='Doodads').save()
            Products(Name='Contraption A', Description='A complex contraption', Price=99.99,
                     StockQuantity=30, Category='Contraptions').save()
            Products(Name='Contraption B', Description='Another complex contraption', Price=109.99,
                     StockQuantity=20, Category='Contraptions').save()
            Products(Name='Gimmick A', Description='An interesting gimmick', Price=39.99,
                     StockQuantity=110, Category='Gimmicks').save()
            Products(Name='Gimmick B', Description='Another interesting gimmick', Price=44.99,
                     StockQuantity=120, Category='Gimmicks').save()
            return JsonResponse({'message': 'Products created'}, status=201)
        return JsonResponse({'message': 'Products already exist'}, status=200)
