from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('Category/<slug:slug>/', views.show_category, name='category'),
    path('Category/<slug:slug>/', views.show_category, name='show_category'),
    path('Product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('faq/', views.faq, name='faq'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('user/', views.user, name='user'),
    path('user/update_profile', views.update_profile, name='update_profile'),
    path('user/update_address', views.update_address, name='update_address'),
    path('user/update_profile_pic', views.update_profile_pic, name='update_profile_pic'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist_update/<int:product_id>', views.wishlist_update, name='wishlist_update'),
    path('cart/', views.cart, name='cart'),
    path('cart_update/<int:product_id>', views.cart_update, name='cart_update'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_history_update/', views.order_history_update, name='order_history_update'),
    path('track_order/<int:order_id>', views.track_order, name='track_order'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('admin_product_page/<int:order_id>', views.admin_product_page, name='admin_product_page'),
    path('admin_status_update/<int:order_id>/<str:status>', views.admin_status_update, name='admin_status_update'),
    path('user/notification', views.notification, name='notification'),
    path('user/notification_info/<int:notification_id>', views.notification_info, name='notification_info'),
    path('user/notification_close/<int:pk>', views.notification_close, name='notification_close'),
]
