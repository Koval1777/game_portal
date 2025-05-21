from django.shortcuts import render, Http404

# Create your views here.
news_items = [
                 {
                     "id":1,
                     "title": "KK",
                     "image": "https://young-teacher.site/wp-content/uploads/2020/12/krestiki-noliki.jpg",
                     "description": "W trakcie wydarzenia zdobywasz unikalne samoloty.",
                     "date": "10 kwietnia 2025",
                     "label": None,
                     "iframe": 'kk/index.html'
                 },
                 {
                    "id":2,
                     "title": "Snake",
                     "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0sp1HTz_bluONTRsl7L27gvXSr9kVqrKUi6JBQP4jp4TrSrFN5toK4EeYXUmT3xmy42E&usqp=CAU",
                     "description": "",
                     "date": "23 kwietnia 2025",
                     "label": "Akcja",
                     "iframe": 'snake/index.html'
                 },
                 {
                    "id":3,
                     "title": "Tetris",
                     "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Tetris_logo.png/960px-Tetris_logo.png",
                     "description": "",
                     "date": "23 kwietnia 2025",
                     "label": None,
                      "iframe": 'tetris/index.html'
                 },
             ]

def index(request):
    context = {"news_items": news_items}

    return render(request, 'index.html', context)


def details(request, id):
    try:
        item = news_items[id - 1]
    except IndexError:
        raise Http404("Nie znaleziono wpisu.")

    context = {"item": item}
    return render(request, 'details.html', context)