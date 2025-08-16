from django.contrib import admin
from django.urls import path
from accounts.views import register_view, login_view, logout_view
from customer.views import (
    customer_dashboard,
    cart_add, cart_read, cart_update, cart_delete,
    order_create, order_read, order_update, order_delete
)
from restaurant.views import restaurant_dashboard, add_dish, update_dish, delete_dish, list_dish
from django.shortcuts import redirect

# def redirect_to_login(request):
#     return redirect('register')

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", redirect_to_login),


    # Auth
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

    # Dashboards
    path("customer_dashboard/", customer_dashboard, name="customer_dashboard"),
    path("restaurant_dashboard/", restaurant_dashboard, name="restaurant_dashboard"),

    # Restaurant CRUD
    path("restaurant_add/", add_dish, name="restaurant_add"),
    path("restaurant_list/", list_dish, name="restaurant_list"),
    path("restaurant_update/<int:dish_id>/", update_dish, name="restaurant_update"),
    path("restaurant_delete/<int:dish_id>/", delete_dish, name="restaurant_delete"),

    # Cart
    path("cart/add/", cart_add, name="cart_add"),
    path("cart/", cart_read, name="cart_read"),
    path("cart/update/<int:cart_id>/", cart_update, name="cart_update"),
    path("cart/delete/<int:cart_id>/", cart_delete, name="cart_delete"),

    # Orders
    path("order/create/", order_create, name="order_create"),
    path("order/", order_read, name="order_read"),
    path("order/update/<int:order_id>/", order_update, name="order_update"),
    path("order/delete/<int:order_id>/", order_delete, name="order_delete"),

    path("customer/browse/", cart_add, name="customer_browse"),

]
