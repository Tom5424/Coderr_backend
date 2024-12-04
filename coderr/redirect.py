from django.shortcuts import redirect


def redirect_to_admin_page(request):
    return redirect("admin/")