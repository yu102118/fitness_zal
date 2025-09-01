from django.shortcuts import render

def home(request):
    data = {
        'title': 'Main Page',
        'values': ['Цены', 'Персонал'],
        'obj': {
            'Удобство': '',
            'Атмосфера': 17,
            'хз не придумали': ''
        }
    }
    return render(request, 'main/home.html', data)

def services(request):
    # Для примера — список услуг фитнес-клуба
    services_list = [
        {'name': 'Персональные тренировки', 'description': 'Индивидуальные занятия с тренером', 'price': '50 AZN/час'},
        {'name': 'Групповые занятия', 'description': 'Занятия в группе до 10 человек', 'price': '20 AZN/занятие'},
        {'name': 'Кардиотренировки', 'description': 'Тренажёры и кардио зона', 'price': 'входит в абонемент'},
        {'name': 'Йога и растяжка', 'description': 'Занятия йогой для всех уровней', 'price': '30 AZN/занятие'},
    ]
    context = {
        'title': 'Xidmətlər',
        'services': services_list,
    }
    return render(request, 'main/services.html', context)

def hall(request):
    return render(request, 'main/hall.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def reviews_home(request):
    return render(request, 'reviews/reviews_home.html')
