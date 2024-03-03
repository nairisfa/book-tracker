from django.urls import path
from main.views import show_main
from main.views import register
from main.views import logout_user
from main.views import show_main, create_book, show_xml, show_json, show_xml_by_id, show_json_by_id, login_user
from main.views import edit_book
from main.views import delete_book

app_name = 'main'

urlpatterns= [
    path('delete/<int:id>', delete_book, name='delete_book'),
    path('edit-book/<int:id>', edit_book, name='edit_book'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('create-book', create_book, name='create_book'),
    path('', show_main, name='show_main'),
]
