# from basketapp.models import Basket


def basket(request):
    basket = []

    if request.user.is_authenticated:
        # basket = Basket.objects.filter(user=request.user)
        basket = request.user.basket.select_related()

    return {
        "basket": basket,
    }
