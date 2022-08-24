from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    book_list = []
    for book_item in books:
        book_dict = {}
        book_dict['id'] = book_item.id
        book_dict['name'] = book_item.name
        book_dict['author'] = book_item.author
        book_dict['pub_date'] = str(book_item.pub_date)
        book_list.append(book_dict)
        # print(book_dict['pub_date'])
    context = {'books': book_list}
    # print(context)
    return render(request, template, context)


def dates_view(request, cur_date):
    template = 'books/date_page.html'
    books = Book.objects.filter(pub_date=cur_date)
    book_list = []
    for book_item in books:
        book_dict = {}
        book_dict['id'] = book_item.id
        book_dict['name'] = book_item.name
        book_dict['author'] = book_item.author
        book_dict['pub_date'] = str(book_item.pub_date)
        book_list.append(book_dict)
        # print(book_dict['pub_date'])
    if Book.objects.filter(pub_date__gt=cur_date).order_by('pub_date').first():
        next_date = Book.objects.filter(pub_date__gt=cur_date).order_by('pub_date').first().pub_date
    else:
        next_date = cur_date
    if Book.objects.filter(pub_date__lt=cur_date).order_by('-pub_date').first():
        previous_date = Book.objects.filter(pub_date__lt=cur_date).order_by('-pub_date').first().pub_date
    else:
        previous_date = cur_date
    print(next_date, previous_date)
    context = {'books': book_list,
               'current_page': str(cur_date),
               'next_page': str(next_date),
               'previous_page': str(previous_date)}
    return render(request, template, context)
