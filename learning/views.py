from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'learning/home.html')

def typing(request):
    return render(request, 'learning/Typing/typing.html')

def typing_game(request):
    return render(request, 'learning/typing_game.html')

def shortcuts(request):
    return render(request, 'learning/shortcuts.html')

def structure(request):
    return render(request, 'learning/structure.html')
    
def structure_game(request):
    return render(request, 'learning/structure_game.html')
#拡張子　quiz
def structure_extension(request):
    return render(request, 'learning/structure_extension.html')

def Office(request):
    return render(request, 'learning/Office.html')
#Excel
def Excel(request):
    return render(request, 'learning/Excel.html')
    #Excel　video
def Excel_video1(request):
    return render(request, 'learning/Excel_video/Excel_video1.html')
def Excel_video2(request):
    return render(request, 'learning/Excel_video/Excel_video2.html')
def Excel_video3(request):
    return render(request, 'learning/Excel_video/Excel_video3.html')
def Excel_video4(request):
    return render(request, 'learning/Excel_video/Excel_video4.html')
def Excel_video5(request):
    return render(request, 'learning/Excel_video/Excel_video5.html')
def Excel_video6(request):
    return render(request, 'learning/Excel_video/Excel_video6.html')

#PowerPoint　video
def PowerPoint(request):
    return render(request, 'learning/PowerPoint.html')
    #Word　video
def PowerPoint_video1(request):
    return render(request, 'learning/PowerPoint_video/PowerPoint_video1.html')
def PowerPoint_video2(request):
    return render(request, 'learning/PowerPoint_video/PowerPoint_video2.html')
def PowerPoint_video3(request):
    return render(request, 'learning/PowerPoint_video/PowerPoint_video3.html')
def PowerPoint_video4(request):
    return render(request, 'learning/PowerPoint_video/PowerPoint_video4.html')
def PowerPoint_video5(request):
    return render(request, 'learning/PowerPoint_video/PowerPoint_video5.html')
def PowerPoint_video6(request):
    return render(request, 'learning/PowerPoint_video/PowerPoint_video6.html')
def PowerPoint_video7(request):
    return render(request, 'learning/PowerPoint_video/PowerPoint_video7.html')

#Word　video
def Word(request):
    return render(request, 'learning/Word.html')
    #Word　video
def Word_video1(request):
    return render(request, 'learning/Word_video/Word_video1.html')
def Word_video2(request):
    return render(request, 'learning/Word_video/Word_video2.html')
def Word_video3(request):
    return render(request, 'learning/Word_video/Word_video3.html')
def Word_video4(request):
    return render(request, 'learning/Word_video/Word_video4.html')
def Word_video5(request):
    return render(request, 'learning/Word_video/Word_video5.html')
def Word_video6(request):
    return render(request, 'learning/Word_video/Word_video6.html')
def Word_video7(request):
    return render(request, 'learning/Word_video/Word_video7.html')

#Windows　video
def Windows(request):
    return render(request, 'learning/Windows.html')
    #Windows　video
def Windows_video1(request):
    return render(request, 'learning/Windows_video/Windows_video1.html')
def Windows_video2(request):
    return render(request, 'learning/Windows_video/Windows_video2.html')
def Windows_video3(request):
    return render(request, 'learning/Windows_video/Windows_video3.html')
def Windows_video4(request):
    return render(request, 'learning/Windows_video/Windows_video4.html')



#復習に使った
def demo(request):
    return render(request, 'learning/demo.html')

def iddemo(request, article_id):
    return HttpResponse("article_id: {}".format(article_id))