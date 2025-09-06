# accounts/views.py

import json
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

# --- KAYIT VIEW'İ (DEĞİŞİKLİK YOK) ---
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# --- YENİ LOGIN VIEW'İ ---
@ensure_csrf_cookie
def login_view(request):
    # Sadece POST metodunu kabul et
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

    print("------ YENİ GİRİŞ İSTEĞİ ------")
    
    # 1. Gelen ham veriyi görelim
    print(f"Request Body: {request.body}")

    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        # 2. JSON'dan ayrıştırılan kullanıcı adı ve şifreyi görelim
        print(f"Alınan Kullanıcı Adı: '{username}'")
        print(f"Alınan Şifre: '{password}'")

    except json.JSONDecodeError:
        print("HATA: Gelen veri JSON formatında değil.")
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    # 3. authenticate fonksiyonunu çağıralım ve sonucunu görelim
    user = authenticate(request, username=username, password=password)
    print(f"Authenticate Sonucu (user nesnesi): {user}")
    
    if user is not None:
        print("Kimlik doğrulama BAŞARILI. Session başlatılıyor.")
        login(request, user)
        return JsonResponse({'message': 'Login successful'})
    else:
        print("Kimlik doğrulama BAŞARISIZ.")
        return JsonResponse({'error': 'Invalid credentials'}, status=401)