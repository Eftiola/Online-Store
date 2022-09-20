from django.urls import path

from . import views


# app_name = "products"

urlpatterns = [
    path("", views.get_products, name="product_list"),
    path("<int:pk>/", views.get_product_details, name="product_details"),
    path("add/", views.product_add, name="product_add"),
    path("product/<int:pk>/", views.edit_product, name="product-edit"),
    #path("add-to-cart/<slug>/", views.add_to_cart, name="add-to-cart"),
    path("search_product", views.search_product, name="search_product"),



    path("cart/add/<int:id>/", views.cart_add, name="cart_add"),
    path("cart/item_clear/<int:id>/", views.item_clear, name="item_clear"),
    path("cart/item_increment/<int:id>/", views.item_increment, name="item_increment"),
    path("cart/item_decrement/<int:id>/", views.item_decrement, name="item_decrement"),
    path("cart/cart_clear/", views.cart_clear, name="cart_clear"),
    path("cart/cart-detail/", views.cart_detail, name="cart_detail"),
    # path("payments/pubkey/", views.get_stripe_pubkey, name="payments_pubkey"),
    # path(
    #     "payments/checkout-session/",
    #     views.create_checkout_session,
    #     name="payments_checkout_session",
    # ),
    # path("payments/success/", views.payment_success, name="payment_success"),
    # path("payments/cancelled/", views.payment_cancel, name="payment_cancel"),

]
