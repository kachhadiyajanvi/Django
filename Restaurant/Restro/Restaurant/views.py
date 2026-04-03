from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'name':"Janvi Kachhadiya", 'ProjectType': "Prectice Project"}
    return render(request, 'Restaurant/home.html', d)

def about(request):
    d = {'name':"Janvi Kachhadiya"}
    return render(request, 'Restaurant/about.html', d)

def services(request):
    d = {'name':"Janvi Kachhadiya"}
    return render(request, 'Restaurant/services.html', d)

def event(request):
    d = {'name':"Janvi Kachhadiya"}
    return render(request, 'Restaurant/event.html', d)

def menu(request):
    d = {'name':"Janvi Kachhadiya"}
    return render(request, 'Restaurant/menu.html', d)

def bill(request):
    bill_data = {
        "restaurant_name": "The Gourmet Diner",
        "name": "Janvi Kachhadiya",
        "address": "123 Tasty Lane, Foodville",
        "items": [
            {"name": "Burger", "price": 8.50, "quantity": 2},
            {"name": "Pizza", "price": 12.00, "quantity": 1},
            {"name": "Pasta", "price": 9.25, "quantity": 1},
            {"name": "Soda", "price": 2.50, "quantity": 3},
        ],
        "tax_percentage": 18,
        "discount_percentage": 10
    }

    for item in bill_data["items"]:
        item["total"] = item["price"] * item["quantity"]

    # Calculate totals
    subtotal = sum(item["price"] * item["quantity"] for item in bill_data["items"])
    discount_amount = (subtotal * bill_data["discount_percentage"]) / 100
    discounted_total = subtotal - discount_amount
    gst_amount = (discounted_total * bill_data["tax_percentage"]) / 100
    total_amount = discounted_total + gst_amount

    # Add calculations to the dictionary
    bill_data.update({
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "discounted_total": discounted_total,
        "gst_amount": gst_amount,
        "total_amount": total_amount
    })
    return render(request, 'Restaurant/bill.html', {'bill_data': bill_data})