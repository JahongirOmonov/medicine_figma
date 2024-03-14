
class Cart:

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = dict()

        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity,
                                     'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += 1

        self.get_total_price(product_id)
        self.save()

    def get_total_price(self, item):
        quantity = self.cart[item]['quantity']
        price = self.cart[item]['price']
        total = quantity * float(price)
        self.cart[item]['total_price'] = str(total)

    def save(self):
        self.session.modified = True
        # del self.session['cart']

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def save_clear(self):
        del self.session['cart']
        self.session.modified = True

    def calculate_total_sum(self):
        total_sum = 0
        for item in self.cart.values():
            total_sum += float(item['total_price'])
        return total_sum
