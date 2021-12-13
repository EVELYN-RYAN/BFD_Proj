from django.shortcuts import render
from django.http import HttpResponse
# HERE, I need to import the HTML page that I want and then i can return it LATER
from createOrder.models import Create_Order, Employee, job_order, ticket


################# Create your views here. ################

##### This pulls up the createOrder page ##########
def orderPageView(request):
    return render(request, 'createOrder/createOrder.html')


################### THIS is not displayed to the customer, it will MAKE an order ################
def storeOrderPageView(request):
    # Create a new ticket object from the model (like a new record)
    if request.method == 'POST':
        new_order = Create_Order()

        new_order.cust_first_name = request.POST.get('fname')
        new_order.cust_last_name = request.POST.get('lname')
        new_order.cust_email = request.POST.get('email')
        new_order.cust_phone = request.POST.get('phone')
        new_order.product_name = request.POST.get('pName')
        new_order.product_type = request.POST.get('pCategory')
        new_order.quantity = request.POST.get('amount')
        new_order.order_description = request.POST.get('description')

    # Save the ticket information record which will generate the autoincremented id
    new_order.save()
    data = Create_Order.objects.all()

    # Assign the list of employee records to the dictionary key "our_emps"
    context = {
        "new_orders": data
    }
    return render(request, 'trackOrders/displayOrders.html', context)

def deleteOrder(request, custID):
    delete_order = Create_Order.objects.filter(id=custID)

    delete_order.delete()
    data = Create_Order.objects.all()
    context = {
        'new_orders': data,
    }
    return render(request, "trackOrders/displayOrders.html", context)


############## this is a display of the FINAL orders created by customers ##############
def OrdersSummaryView(request):
    new_orders = Create_Order.objects.all()

    context = {
        "new_orders": new_orders
    }
    return render(request, "trackOrders/displayOrders.html", context)


############## this is a display of the FINAL tickets created by manager ##############
def TicketsSummaryView(request):
    all_tickets = ticket.objects.all()

    context = {
        "all_tickets": all_tickets
    }
    return render(request, "trackOrders/ticketsSummary.html", context)


###### trying to edit and delete a single order ########
def editOrderPageView(request, custID):
    order = Create_Order.objects.get(id=custID)

    context = {
        "order": order
    }
    return render(request, 'trackOrders/editOrder.html', context)


def confirmOrderPageView(request, custId):
    # order = Create_Order.objects.get(id=custId)
    confirm_order = Create_Order.objects.filter(id=custId)
    context = {
        'confirm_order': confirm_order,
    }
    return render(request, "trackOrders/confirmOrder.html", context)


#### THIS IS redirecting to the create ticket page #####
## still needs works###
def confirmOrder_CreateTicket(request, custID):
    confirm_order = Create_Order.objects.filter(id=custID)
    context = {
        'confirm_order': confirm_order,
    }
    return render(request, "trackOrders/createTicket.html", context)


#### THIS IS CREATING THE TICKET #####
def storeTicketPageView(request, orderID):
    if request.method == 'POST':
        icustID = request.POST['custID']

        # Create a new ticket
        new_ticket = ticket()

        # Modify the employee last name with a new value from the form
        new_ticket.order_id = icustID
        new_ticket.cust_first_name = request.POST['']
        new_ticket.cust_last_name = request.POST['lname']
        new_ticket.cust_email = request.POST['email']
        new_ticket.cust_phone = request.POST['phone']
        new_ticket.product_name = request.POST['pName']
        new_ticket.product_type = request.POST['pCategory']
        new_ticket.quantity = request.POST['amount']
        new_ticket.order_description = request.POST['description']

        # Save the changes
        new_ticket.save()

    return OrdersSummaryView(request)


def updateOrder(request):
    if request.method == 'POST':
        icustID = request.POST['custID']

        # Find the employee record
        order = Create_Order.objects.get(id=icustID)

        # Modify the employee last name with a new value from the form
        order.id = icustID
        order.cust_first_name = request.POST['fname']
        order.cust_last_name = request.POST['lname']
        order.cust_email = request.POST['email']
        order.cust_phone = request.POST['phone']
        order.product_name = request.POST['pName']
        order.product_type = request.POST['pCategory']
        order.quantity = request.POST['amount']
        order.order_description = request.POST['description']

        # Save the changes
        order.save()

    return OrdersSummaryView(request)
