from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Test


def index(request):
    return render(request, 'index.html')


#API data
def tests_data_api(request):
    data = Test.objects.all()
    dataList = []

    for i in data:
        dataList.append({'name': i.name, 'result': i.result, 'id': i.id})

    return JsonResponse(dataList, safe=False)


@csrf_exempt
def create_test(request):
    name = request.POST.get('name')
    result = request.POST.get('result')

    Test.objects.create(
        name=name,
        result=result,
    )
    return JsonResponse('Test Created !', safe=False)


@csrf_exempt
def update_test(request):
    objId = request.POST.get('id')
    result = request.POST.get('result')

    test = Test.objects.get(id=objId)
    test.result = result
    test.save()

    return JsonResponse('Test Updated !', safe=False)


@csrf_exempt
def delete_test(request):
    objId = request.POST.get('id')
    test = Test.objects.get(id=objId)
    test.delete()
    return JsonResponse('Test Deleted !', safe=False)