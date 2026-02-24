from django.urls import path
from . import views

app_name = 'volonteri'  

urlpatterns = [
   path('aktivnosti/', views.ActivityListView.as_view(), name='aktivnost_list'),
   path("aktivnosti/<int:pk>/", views.AktivnostDetailView.as_view(), name="aktivnost_detalji"),

    path("kategorije/", views.KategorijaListView.as_view(), name="kategorije"),
    path("kategorije/<int:pk>/", views.KategorijaDetailView.as_view(), name="kategorija_detalji"),

    path("prijave/", views.PrijavaListView.as_view(), name="prijave"),
    path("prijave/<int:pk>/", views.PrijavaDetailView.as_view(), name="prijava_detalji"),

    path('', views.index, name='index'),

    path("register/", views.register, name="register"),

    path("aktivnosti/novo/", views.AktivnostCreateView.as_view(), name="aktivnost_nova"),
    path("aktivnosti/<int:pk>/uredi/", views.AktivnostUpdateView.as_view(), name="aktivnost_uredi"),
    path("aktivnosti/<int:pk>/obrisi/", views.AktivnostDeleteView.as_view(), name="aktivnost_obrisi"),

]