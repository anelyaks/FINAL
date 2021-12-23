from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Category, Product, buy


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'abonements/type_products/price.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'abonements/type_product/detail.html', {'product': product})

class AddProductView(CreateView):
    model = Product
    template_name = 'abonements/crud/create.html'
    fields = '__all__'
    success_url = reverse_lazy('abonements:product_list')

class DeleteProductView(DeleteView):
    model = Product
    template_name = 'abonements/crud/delete.html'
    success_url = reverse_lazy('abonements:product_list')

class UpdateProductView(UpdateView):
    model = Product
    template_name = 'abonements/crud/update.html'
    fields = '__all__'
    success_url = reverse_lazy('abonements:product_list')


def price(request):
    error = ''
    if request.method == 'POST':
        form = buy(request.POST)
        if form.is_valid():
            form.save()
            return redirect("{% url 'product_list' %}")
        else:
            error = 'ERROR'

    form = buy()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'abonements/product_list', data)
