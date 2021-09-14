from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from API_app.models import Utilisateurs, Phrase
from API_app.serializers import UtilisateursSerializer, PhraseSerializer


from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def utilisateursApi(request, id=0):
    if request.method == 'GET':
        utilisateurs = Utilisateurs.objects.all()
        utilisateurs_serializer = UtilisateursSerializer(utilisateurs, many=True)
        return JsonResponse(utilisateurs_serializer.data, safe=False)

    elif request.method == 'POST':
        utilisateur_data = JSONParser().parse(request)
        utilisateurs_serializer = UtilisateursSerializer(data=utilisateur_data)
        if utilisateurs_serializer.is_valid():
            utilisateurs_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        utilisateur_data = JSONParser().parse(request)
        utilisateur = Utilisateurs.objects.get(UtilisateurID=utilisateur_data['UtilisateurID'])
        utilisateur_serializer = UtilisateursSerializer(utilisateur, data=utilisateur_data)
        if utilisateur_serializer.is_valid():
            utilisateur_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        utilisateur = Utilisateurs.objects.get(UtilisateurID=id)
        utilisateur.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)