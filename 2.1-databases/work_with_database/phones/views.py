from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_phones = request.GET.get("sort")
    all_phones = Phone.objects.all()

    if sort_phones == 'max_price':
        phones = all_phones.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_phones == 'min_price':
        phones = all_phones.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_phones == 'name':
        phones = all_phones.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)
    context = {
        'phones': all_phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
