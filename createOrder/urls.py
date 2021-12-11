# THIS IS THE URL's that is for our specific app
from django.urls import path

# This is accessing the views/funcitons that we wrote on views.py!!
from .views import editOrderPageView, orderPageView, storeOrderPageView, OrdersSummaryView, updateOrder, TicketsSummaryView, confirmOrder_CreateTicket


# we create the path with this syntax
urlpatterns = [
    path("createorder/", orderPageView, name="orders"),
    path("storeorder/", storeOrderPageView, name='storeorder'),
    path('currentOrders/', OrdersSummaryView, name='currentOrders'),
    path('currentTickets/', TicketsSummaryView, name='currentTickets'),
    path("editOrder/<int:custID>/",
         editOrderPageView, name='editOrder'),
    path('createTicket/<int:custID>/',
         confirmOrder_CreateTicket, name='createTicket'),
    path("updateOrder/", updateOrder, name="updateOrder"),

    # path("order/", OrdersSummaryView, name="orders"),
    # path("orders/", OrdersSummaryView, name="orders"),

]
