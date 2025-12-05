from django.shortcuts import render
from django.http import HttpResponse
import datetime 

def writers_view(request):
    
    content = """
    <h1>10 Великих Писателей:</h1>
    1. Чынгыз Айтматов<br>
    2. Федор Достоевский<br>
    3. Антон Чехов<br>
    4. Александр Пушкин<br>
    5. Уильям Шекспир<br>
    6. Эрнест Хемингуэй<br>
    7. Франц Кафка<br>
    8. Джордж Оруэлл<br>
    9. Марк Твен<br>
    10. Лев Толстой
    """
    if request.method == 'GET':
         return HttpResponse(content)
    

def quotes_view(request):
    content = """
    <h1>5 Цитат:</h1>
    1. "Краткость — сестра таланта." (Чехов)<br>
    2. "Все счастливые семьи похожи друг на друга..." (Толстой)<br>
    3. "Быть или не быть — вот в чем вопрос." (Шекспир)<br>
    4. "Красота спасет мир." (Достоевский)<br>
    5. "И дольше века длится день." (Айтматов)
    """
    if request.method == 'GET':
         return HttpResponse(content)


def current_time_view(request):
    now = datetime.datetime.now() 
    if request.method == 'GET':
         return HttpResponse(f"<h1>Текущее системное время:</h1> {now}")