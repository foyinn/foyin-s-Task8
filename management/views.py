from django.shortcuts import render, redirect
from .models import HotelRecord

def record(request):
    hotel_record = HotelRecord.objects.all()
    context = {
        "hotel_record": hotel_record
    }

    return render(request, 'management/blog1.html', context)


def createpost(request):
    if request.method == "POST":
       Name = request.POST.get("Name")
       Email = request.POST.get("Email")
       Occupation = request.POST.get("Occupation")
       Room_Number = request.POST.get("Room Number")
       Amount_Paid = request.POST.get("Amount Paid")
       Number_Of_Nights = request.POST.get("Number Of Nights")
       Day_Of_Arrival = request.POST.get("Day Of Arrival")
       Day_Of_Departure = request.POST.get("Day Of Departure")


       new_post = HotelRecord(Name=Name,
                              Email=Email,
                              Occupation=Occupation,
                              Room_Number=Room_Number,
                              Amount_Paid=Amount_Paid,
                              Number_Of_Nights=Number_Of_Nights,
                              Day_Of_Arrival=Day_Of_Arrival,
                              Day_Of_Departure=Day_Of_Departure,
                              )
       new_post.save()
       return redirect("management:hotel-record")

    return render(request, "management/create-post.html")