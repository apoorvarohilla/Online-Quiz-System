from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Online Quiz System</h1>")

urlpatterns = [
    path('', home),  # ✅ Homepage
    path('admin/', admin.site.urls),
    path('api/', include('quiz.urls')),  # ✅ API Endpoints
]
