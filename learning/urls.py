from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('typing',views.typing, name='typing'),
    path('typing/game',views.typing_game, name='typing_game'),
    path('shortcuts',views.shortcuts, name='shortcuts'),
    path('structure',views.structure, name='structure'),
    path('structure/game',views.structure_game, name='structure_game'),
    path('structure/extension',views.structure_extension, name='structure_extension'),

    path('Office',views.Office, name='Office'),
    path('Office/Excel',views.Excel, name='Excel'),
    path('Office/PowerPoint',views.PowerPoint, name='PowerPoint'),
    path('Office/Word',views.Word, name='Word'),
    path('Windows',views.Windows, name='Windows'),   

#Excel video
    path('Excel_video1',views.Excel_video1, name='Excel_video1'),
    path('Excel_video2',views.Excel_video2, name='Excel_video2'),
    path('Excel_video3',views.Excel_video3, name='Excel_video3'),
    path('Excel_video4',views.Excel_video4, name='Excel_video4'),
    path('Excel_video5',views.Excel_video5, name='Excel_video5'),
    path('Excel_video6',views.Excel_video6, name='Excel_video6'),

#Word video
    path('Word_video1',views.Word_video1, name='Word_video1'),
    path('Word_video2',views.Word_video2, name='Word_video2'),
    path('Word_video3',views.Word_video3, name='Word_video3'),
    path('Word_video4',views.Word_video4, name='Word_video4'),
    path('Word_video5',views.Word_video5, name='Word_video5'),
    path('Word_video6',views.Word_video6, name='Word_video6'),
    path('Word_video7',views.Word_video7, name='Word_video7'),

#PowerPoint video
    path('PowerPoint_video1',views.PowerPoint_video1, name='PowerPoint_video1'),
    path('PowerPoint_video2',views.PowerPoint_video2, name='PowerPoint_video2'),
    path('PowerPoint_video3',views.PowerPoint_video3, name='PowerPoint_video3'),
    path('PowerPoint_video4',views.PowerPoint_video4, name='PowerPoint_video4'),
    path('PowerPoint_video5',views.PowerPoint_video5, name='PowerPoint_video5'),
    path('PowerPoint_video6',views.PowerPoint_video6, name='PowerPoint_video6'),
    path('PowerPoint_video7',views.PowerPoint_video7, name='PowerPoint_video7'),

#Windows video
    path('Windows_video1',views.Windows_video1, name='Windows_video1'),
    path('Windows_video2',views.Windows_video2, name='Windows_video2'),
    path('Windows_video3',views.Windows_video3, name='Windows_video3'),
    path('Windows_video4',views.Windows_video4, name='Windows_video4'),
  

    path('demo',views.demo, name='demo'),
    path('demo/<int:article_id>', views.iddemo, name='iddemo'),
]
