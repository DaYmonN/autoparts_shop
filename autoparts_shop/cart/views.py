from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from catalog.models import Part


def cart_view(request):
    """Корзина покупок"""
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for part_id, quantity in cart.items():
        part = get_object_or_404(Part, id=int(part_id))
        item_total = part.price * quantity
        total += item_total
        cart_items.append({
            'part': part,
            'quantity': quantity,
            'total': item_total
        })

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def add_to_cart(request, part_id):
    """Добавить в корзину"""
    cart = request.session.get('cart', {})
    part_id_str = str(part_id)

    if part_id_str in cart:
        cart[part_id_str] += 1
    else:
        cart[part_id_str] = 1

    request.session['cart'] = cart

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True, 'cart_count': sum(cart.values())})

    return redirect('cart:cart_view')


def remove_from_cart(request, part_id):
    """Удалить из корзины"""
    cart = request.session.get('cart', {})
    part_id_str = str(part_id)

    if part_id_str in cart:
        del cart[part_id_str]

    request.session['cart'] = cart
    return redirect('cart:cart_view')


def update_cart(request, part_id):
    """Обновить количество"""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})

        if quantity <= 0:
            cart.pop(str(part_id), None)
        else:
            cart[str(part_id)] = quantity

        request.session['cart'] = cart

    return redirect('cart:cart_view')


def cart_total(request):
    """Контекстный процессор для корзины"""
    cart = request.session.get('cart', {})
    total_items = sum(cart.values())
    return {'cart_total_items': total_items}