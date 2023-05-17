from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout 
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models  import Question,  QuizSubmission



def base(request):
    """
    Renders the base template.

    Returns:
        HttpResponse: The rendered base template.
    """

    return render(request, 'base.html')

def home(request):
    """
    Renders the home template.

    Returns:
        HttpResponse: The rendered home template.
    """
    return render(request, 'home.html')


"""
    Renders the home template.

    Returns:
        HttpResponse: The rendered home template.
    """

def registration(request):

    """
    Renders the registration template and handles user registration.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered registration template, or a redirect to the home page if the form is valid.
    """


    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log in the user after registration
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):

    """
    Renders the login template and handles user authentication.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered login template, or a redirect to the about page if the user is authenticated.
    """

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #messages.success(request, 'You have been successfully logged in.')
            return redirect('sugar:about')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'user_login.html')

def user_logout(request):

    """
    Logs out the user and redirects to the home page.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponseRedirect: A redirect to the home page.
    """
    logout(request)
    return redirect('home')


def about(request):

    """
    Renders the about template.

    Returns:
        HttpResponse: The rendered about template.
    """
    return render(request, 'about.html')


@login_required
def quiz(request):

    """
    Renders the quiz template and handles quiz submission.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered quiz template, or a redirect to the quiz page if the form is valid.
    """
    if request.method == 'POST':
        # handle form submission
        question1 = request.POST.get('question1', '')
        question2a = request.POST.get('question2a', '')
        question2b = request.POST.get('question2b', '')
        question2c = request.POST.get('question2c', '')
        question3a = request.POST.get('question3a', '')
        question3b = request.POST.get('question3b', '')
        question3c = request.POST.get('question3c', '')

        # check answers
        score = 0
        if question1 == 'a':
            score += 1
        if question2a == 'obesity' and question2b == 'diabetes' and question2c == 'heart disease':
            score += 1
        if question3a == 'water' and question3b == 'tea' and question3c == 'coffee':
            score += 1

      
        # show score to user
        messages.success(request, f'Your score is {score} out of 3!')

        return redirect('quiz')

    # render quiz template
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'quiz.html', context)

def login_view(request):
    """
    Renders the login template.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: The rendered login template.
    """

    return render(request, 'user_login.html')