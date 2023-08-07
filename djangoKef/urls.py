from django.contrib import admin
from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),
    path("product/<int:product_id>/", views.product, name="product"),
    path("indexAdmin/", views.indexAdmin, name = "admin"),
    path("indexAdmin/<int:product_id>/", views.adminProduct, name="adminProduct"),
    path("indexAdmin/<int:product_id>/delete", views.deleteProduct, name="deleteProduct"),
    path("indexAdmin/createProduct", views.createProduct, name="createProduct"),
    path("indexAdmin/updateProduct/<int:product_id>", views.updateProduct, name ="updateProduct"),
    path("tienda/",views.tienda, name="tienda"),
    path("agregar/<int:producto_id>/", views.agregarProducto, name="add"),
    path("elimnar/<int:producto_id>/", views.eliminar, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar, name="restar"),
    path("limpiar/", views.limpiar, name="limpiar"),
    path("guardar/", views.guardar_carrito,name="guardar_carrito"),
    path("carrito/",views.vista_del_carrito, name="carrito"),
    path("eliminarCarrito/<int:producto_id>/", views.eliminarCarrito, name="eliminarCarrito"),
    path("agregarCarrito/<int:producto_id>/", views.agregarCarrito, name="addCarrito"),
    path("restarCarrito/<int:producto_id>/", views.restarCarrito, name="restarCarrito"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)