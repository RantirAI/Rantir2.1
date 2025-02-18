# 🔹 Imports (Keep at the top)
import uuid
import json
import paypalrestsdk
import stripe
from rest_framework.response import Response
from rest_framework.decorators import api_view
from baserow.contrib.database.models import Table, Row
from django.views.decorators.csrf import csrf_exempt

# ============================
# 📌 EXISTING ORDER & PAYMENT FUNCTIONS (KEEP)
# ============================

# Your existing order handling, Stripe/PayPal checkout, and webhook functions should remain.

# ============================
# 📌 NEW SUBSCRIPTION DASHBOARD API (ADD HERE)
# ============================

@api_view(['GET'])
def get_subscription_overview(request):
    """Fetches subscription dashboard data including user counts, revenue, and signups."""
    try:
        # Dummy data structure (Replace with actual Baserow queries)
        response_data = {
            "total_members": 2300,
            "signups_last_month": 24,
            "paid_members": 324,
            "monthly_revenue": 12450,
        }
        return Response(response_data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

# ============================
# 📌 NEW DATABASE & USER GROUP API (ADD HERE)
# ============================

@api_view(['GET'])
def get_databases_and_user_groups(request):
    """Fetches available databases and their associated user groups."""
    try:
        response_data = {
            "databases": [
                {"id": 1, "name": "Truck Users"},
                {"id": 2, "name": "Uncategorized"},
            ],
            "user_groups": [
                {"id": 101, "name": "Truck Drivers"},
                {"id": 102, "name": "Uncategorized"},
            ],
        }
        return Response(response_data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET'])
def get_subscription_plans(request):
    """Fetches available subscription plans."""
    try:
        response_data = {
            "plans": [
                {"id": 1, "name": "Example Plan"},
                {"id": 2, "name": "Example 2 Plan"},
                {"id": 3, "name": "Exmaple 3 Plan"},
            ]
        }
        return Response(response_data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

# ============================
# 📌 NEW USER GROUP CREATION API (ADD HERE)
# ============================

@api_view(['POST'])
def create_user_group(request):
    """Creates a new user group and assigns it to a database & plan."""
    try:
        data = request.data
        user_group_id = str(uuid.uuid4())  # Generate unique ID
        new_user_group = {
            "id": user_group_id,
            "name": data.get("name"),
            "database_id": data.get("database_id"),
            "plan_id": data.get("plan_id"),
        }
        # Simulating database insert (Replace with actual Baserow logic)
        return Response({"message": "User group created successfully", "data": new_user_group}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

# Stripe API Key
stripe.api_key = "sk_test_XXXX"

# PayPal API Configuration
paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": "YOUR_PAYPAL_CLIENT_ID",
    "client_secret": "YOUR_PAYPAL_CLIENT_SECRET"
})

@api_view(['POST'])
def create_order_or_subscription(request):
    """Handles both product orders and subscription purchases with Stripe or PayPal."""
    try:
        table_id = request.data.get("table_id")
        user_id = request.data.get("user_id")
        order_type = request.data.get("order_type")  # "subscription" or "product"
        payment_method = request.data.get("payment_method")  # "stripe" or "paypal"
        total_price = request.data.get("total_price")

        order_id = str(uuid.uuid4())

        # Define shared order/subscription fields
        order_data = {
            "order_id": order_id,
            "user_id": user_id,
            "total_price": total_price,
            "status": "pending",
            "payment_status": "unpaid",
            "payment_provider": payment_method
        }

        if order_type == "subscription":
            order_data["subscription_status"] = "active"
            order_data["start_date"] = request.data.get("start_date")
            order_data["end_date"] = request.data.get("end_date")

        elif order_type == "product":
            order_data["products"] = request.data.get("products")  # JSON format
            order_data["shipping_address"] = request.data.get("shipping_address")

        # Save order to Baserow
        new_order = Row.objects.create(table_id=table_id, values=order_data)

        # Generate Payment Link for Stripe or PayPal
        if payment_method == "stripe":
            payment_link = generate_stripe_payment_link(order_id, total_price, order_type)
        elif payment_method == "paypal":
            payment_link = generate_paypal_payment_link(order_id, total_price)

        return Response({"order_id": order_id, "payment_link": payment_link}, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=500)

def generate_stripe_payment_link(order_id, amount, order_type):
    """Creates a Stripe Checkout session."""
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": f"{order_type.capitalize()} Order {order_id}"},
                "unit_amount": int(amount * 100),
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url=f"https://your-site.com/success?order_id={order_id}",
        cancel_url=f"https://your-site.com/cancel?order_id={order_id}",
    )
    return session.url

def generate_paypal_payment_link(order_id, amount):
    """Creates a PayPal payment link."""
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": f"https://your-site.com/success?order_id={order_id}",
            "cancel_url": f"https://your-site.com/cancel?order_id={order_id}"
        },
        "transactions": [{
            "amount": {
                "total": f"{amount:.2f}",
                "currency": "USD"
            },
            "description": f"Order {order_id}"
        }]
    })

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                return link.href  # PayPal checkout link

    return None  # If something went wrong

@csrf_exempt
@api_view(['POST'])
def stripe_webhook(request):
    """Handles Stripe payment updates for orders and subscriptions."""
    payload = request.body
    event = None

    try:
        event = json.loads(payload)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        order_id = session["metadata"]["order_id"]

        # Find order in Baserow
        order = Row.objects.get(values__order_id=order_id)

        # Update payment status
        order.values["payment_status"] = "paid"
        order.values["status"] = "completed"

        # If it's a subscription, mark as "active"
        if "subscription_status" in order.values:
            order.values["subscription_status"] = "active"

        order.save()

    return Response({"message": "Success"}, status=200)

@csrf_exempt
@api_view(['POST'])
def paypal_webhook(request):
    """Handles PayPal payment updates."""
    try:
        data = json.loads(request.body)
        event_type = data.get("event_type")

        if event_type == "PAYMENT.SALE.COMPLETED":
            order_id = data["resource"]["invoice_id"]  # PayPal sends the order ID as invoice_id

            # Find order in Baserow
            order = Row.objects.get(values__order_id=order_id)

            # Update payment status
            order.values["payment_status"] = "paid"
            order.values["status"] = "completed"

            # If it's a subscription, mark as "active"
            if "subscription_status" in order.values:
                order.values["subscription_status"] = "active"

            order.save()

        return Response({"message": "PayPal webhook processed"}, status=200)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
