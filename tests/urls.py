from django.conf.urls import url


def dummy_view(request):
    from django.http import HttpResponse
    return HttpResponse()


urlpatterns = [
    url(r'^$', dummy_view, name='modeldict-home'),
]
