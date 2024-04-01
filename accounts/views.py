from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def register_view(request):
    """
    Função de visualização para registro de usuário.
    """
    
    if request.method == "POST":
        # Se o método da requisição for POST, processa o formulário de registro
        user_form = UserCreationForm(request.POST)
       
        if user_form.is_valid():
             # Se o formulário for válido, salva o usuário e redireciona para a página de login
            user_form.save()
            return redirect('login')
    else:
        # Se o método da requisição for GET, exibe o formulário de registro
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})


def login_view(request):
    """
    Função de visualização para login de usuário.
    """
    
    if request.method == "POST":
        # Se o método da requisição for POST, processa o formulário de login
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Se o usuário for autenticado, realiza o login e redireciona para a página de lista de carros
            login(request, user)
            return redirect('cars_list')
        else:
            # Se a autenticação falhar, exibe o formulário de login com mensagem de erro
            login_form = AuthenticationForm()
    else:
       # Se o método da requisição for GET, exibe o formulário de login
       login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout_view(request):
    """
    Função de visualização para logout de usuário.
    """
    # Realiza o logout e redireciona para a página de lista de carros
    logout(request)
    return redirect('cars_list')