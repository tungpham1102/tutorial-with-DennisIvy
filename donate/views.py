from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
import stripe

stripe.api_key = "sk_test_y9j3fW1S2J4PlDidYgPT4wQQ00FTZ6quhm"



def donate(request):
    return render(request, 'donate/donate.html')


def charge(request):

    if request.method == 'POST':
        print('Data: ', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['nickname'],
            source = request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer = customer,
            amount = amount*100,
            currency = 'usd',
            description = 'Donation',
        )

    return redirect(reverse('success', args = [amount]))


def success(request, args):
    amount = args
    return render(request, 'donate/success.html', {'amount': amount})
