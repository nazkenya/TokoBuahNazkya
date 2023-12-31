from django.urls import path
from main.views import add_product_ajax, create_product_flutter, delete_item_ajax, edit_item_ajax, get_product_json, show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_item, delete_item, increase_amount, decrease_amount, clear_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit_item/<int:id>', edit_item, name='edit_item'),
    path('delete/<int:id>', delete_item, name='delete_item'),
    path('increase/<int:id>', increase_amount, name='increase_amount'),
    path('decrease/<int:id>', decrease_amount, name='decrease_amount'),
    path('clear/', clear_item, name='clear_item'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('edit-item-ajax/', edit_item_ajax, name='edit_item_ajax'),
    path('delete_item_ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]   