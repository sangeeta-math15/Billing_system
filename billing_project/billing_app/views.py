from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Bill, Item
from .serializers import ItemSerializers, BillSerializers
from rest_framework.decorators import action
#
#
# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializers
#
#     def create(self, request, *args, **kwargs):
#         serializers = self.get_serializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_objects()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_objects()
#         serializers = self.get_serializer(instance, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BillViewSet(viewsets.ModelViewSet):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializers
#
#     @action(detail=False, methods=['POST'])
#     def generate_bill(self, request):
#         selected_item_related = request.data.get('selected_realted', [])
#         selected_item = Item.objects.filter(id__in=selected_item_related)
#
#         total_cost = sum(item.price for item in selected_item)
#
#         bill_data = {
#             'items': selected_item,
#             'total_cost': total_cost
#         }
#         serializers = self.get_serializer(data=bill_data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.data, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Bill, Item
from .serializers import ItemSerializers,BillSerializers
from rest_framework.decorators import action


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializers

    @action(detail=False, methods=['POST'])
    def generate_bill(self, request):

        selected_item_ids = request.data.get('items', [])
        selected_items = Item.objects.filter(id__in=selected_item_ids)
        print(selected_items)

        total_cost = sum(item.price for item in selected_items)
        print(total_cost)

        bill_data = {
            'items': selected_items,
            'total_cost': total_cost
        }
        serializer = self.get_serializer(data=bill_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
