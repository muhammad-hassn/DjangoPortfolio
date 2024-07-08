from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from myapp.models import Contact
from.models import Game
# from .forms import MatrixForm
# Create your views here.

def index(request):
    # return HttpResponse('hello HAssan')
    return render(request , 'home.html')
def about(request):
    # return HttpResponse('hello HAssan')
    return render(request , 'about.html')

def Project(request):
    # return HttpResponse('hello HAssan')
    return render(request , 'project.html')

def resume(request):
    # return HttpResponse('hello HAssan')
    return render(request , 'resume.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc= request.POST.get('desc')
        contact = Contact(name = name , email = email , number = number , desc = desc , date = datetime.today())
        contact.save()
    return render(request, 'contact.html')


@csrf_exempt
def calculator(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')
    
        result = None
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2

        return JsonResponse({'result': result})

    return render(request, 'calculator.html')

def Converter(request):
    if request.method == 'POST':
        def currency_converter(amount, from_currency, to_currency):
        # Fetch the latest exchange rates from an API
            exchange_rates = get_exchange_rates()
            # Convert the amount from the source currency to USD
            usd_amount = amount / exchange_rates[from_currency]
            # Convert the USD amount to the target currency
            result = usd_amount * exchange_rates[to_currency]
            return result
        def get_exchange_rates():
            # Fetch the latest exchange rates from an API
            # Replace this with the actual API call to get the exchange rates
            exchange_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.0,
            'CAD': 1.25,
            'RS' : 278,
            # Add more currencies and their exchange rates here
            }
            return exchange_rates
            # Example usage
        amount = float(request.POST.get('amuont'))
        from_currency = request.POST.get('convert').upper()
        to_currency = request.POST.get('to_currency').upper()
        converted_amount = currency_converter(amount, from_currency, to_currency)
        return JsonResponse({'result': converted_amount})
    

    return render(request ,'converter.html')

@csrf_exempt
def temp_Convert(request):
    if request.method == 'POST':
        temperature = float(request.POST.get('temperature'))
        unit = request.POST.get('unit')
        if unit.upper() == 'F':
            result = (temperature - 32) * 5/9
            # print(f"{temperature} degree is equal to {celsius} degree Celsius:")
            # return JsonResponse({'result': celsius})
        elif unit.upper() == 'C':
            result = (temperature * 9/5) + 32
            # print(f"{temperature} degree is equal to {fahrenhiet} degree Farenhiet:")
        else:
            print("Invalid unit.Please Enter F or C")
        # return JsonResponse({f'result {temperature} dgree is equal to {result} degree {unit}'})
        return JsonResponse({f'{temperature} dgree is equal to {unit}':result })
    return render(request ,'temCon.html')

def matrix_view(request):
    if request.method == 'POST':
        size_a = int(request.POST['size_a'])
        matrix_a = request.POST['matrix_a'].splitlines()
        matrix_a = [list(map(int, row.split())) for row in matrix_a]

        size_b = int(request.POST['size_b'])
        matrix_b = request.POST['matrix_b'].splitlines()
        matrix_b = [list(map(int, row.split())) for row in matrix_b]

        A = np.array(matrix_a)
        B = np.array(matrix_b)

        At = A.T
        ATA = np.dot(At, A)
        ATB = np.dot(At, B)
        ATA_inv = np.linalg.inv(ATA)
        X = np.dot(ATA_inv, ATB)

        return render(request, 'result.html', {'result': X})
    else:
        return render(request, 'run_code.html')

def Company(request):
    if request.method == 'POST':
        salarys = float(request.POST.get('salary'))
        years_of_service = int(request.POST.get('service'))
        if years_of_service > 5:
            bonus_percentage = 5
            net_bonus_amount = (bonus_percentage / 100) * salarys
            return JsonResponse({f'Congratulations! You qualify for a {bonus_percentage} % bonus. Your net bonus amount is: {net_bonus_amount}' : net_bonus_amount })
        else:
            return HttpResponse({'Sorry, you do not qualify for a bonus.'})

    return render(request , 'company.html')

import random
# from django.shortcuts import render

def guess_game(request):
    if request.method == 'POST':
        if 'guess' in request.POST:
            guess = request.POST.get('guess')
            if not guess:
                message = 'Please enter a number.'
            else:
                guess = int(guess)
                number = request.session.get('number')
                if guess < number:
                    message = 'Your guess is too low.'
                elif guess > number:
                    message = 'Your guess is too high.'
                else:
                    message = 'Congratulations, you guessed the number!'
        elif 'restart' in request.POST:
            del request.session['number']
            request.session['number'] = random.randint(1, 100)
            message = 'Game restarted! Guess a number between 1 and 10.'
        return render(request, 'Guess_Game.html', {'message': message})
    else:
        if 'number' not in request.session:
            request.session['number'] = random.randint(1, 100)
        return render(request, 'Guess_Game.html')