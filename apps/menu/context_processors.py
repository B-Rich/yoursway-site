from apps.menu.models import Menu

def menu(request):
    return {'global_menu': Menu.objects.order_by('order')}