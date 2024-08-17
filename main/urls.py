from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainMain, name='home'),
    path('index', views.index, name='first'),
    path('about', views.about, name='DOT'),
    path('about/form', views.dotform, name='DOTform'),
    path('about/form/create', views.dotform_create, name='DOTcreate'),
    path('<int:pk>/update', views.dotformUpdateView.as_view(), name='DOTupdate'),
    path('<int:pk>/delete', views.dotformDeleteView.as_view(), name='DOTdelete'),

    path('about/bydot', views.by_DOT, name='byDOT'),
    path('about/bydot/create', views.by_DOT_create, name='byDOTcreate'),
    path('about/bydot/<int:pk>/update', views.by_dotUpdateView.as_view(), name='byDOTupdate'),
    path('about/bydot/<int:pk>/delete', views.by_dotDeleteView.as_view(), name='byDOTdelete'),

    path('about/out-dot', views.out_dot, name='outDOT'),
    path('about/last-dot', views.last_dot, name='lastDOT'),
    path('check-svtk', views.check_svtk, name='SVTK'),
    path('check-svtk/form', views.svtkform, name='SVTKform'),
    path('check-svtk/programm', views.svtkprogcheck, name='SVTKprog'),
    path('stats', views.stat, name='stats')
]