from rest_framework import serializers
from .models import Product, Category
from .cart import Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title',
            'image',
            'category',
            'price'
        )


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'title',
            'products'
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 2)]
    quantity = serializers.ChoiceField(
        choices=QUANTITY_CHOICES,
        write_only=True
    )
    override = serializers.BooleanField(required=False,
                                        initial=False,
                                        read_only=True
                                        )
    title = serializers.CharField(read_only=True)
    price = serializers.DecimalField(decimal_places=2, max_digits=10, read_only=True)
    category = serializers.StringRelatedField(source="category.title", read_only=True)

    class Meta:
        model = Product
        fields = "title", "price", "category", "quantity", "override"

    def update(self, instance, validated_data):
        print('\n\n')
        print(instance)
        print(self.context['request'])
        print(validated_data)
        print('\n\n')
        request = self.context['request']
        quantity = validated_data['quantity']
        cart = Cart(request)
        cart.add(instance, quantity)
        return super().update(instance, validated_data)
