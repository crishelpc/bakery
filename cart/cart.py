class Cart():
    def __init__(self, request):
        self.session = request.session

        # get the current cart from the session
        cart = self.session.get('cart')

        # if the cart is not present in the session, initialize it
        if 'cart' not in request.session:
            cart = self.session['cart'] = {}

        # make sure cart is available on all pages
        self.cart = cart

def add(self, product, quantity=1):
    product_id = str(product.id)

    if product_id in self.cart:
        # Increment the quantity if the product is already in the cart
        self.cart[product_id]['quantity'] += quantity
    else:
        # Add a new item with the specified quantity
        self.cart[product_id] = {'price': str(product.price), 'quantity': quantity}

    self.session.modified = True

    def __len__(self):
        return len(self.cart)