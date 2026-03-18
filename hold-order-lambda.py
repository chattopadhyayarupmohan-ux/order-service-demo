import json

def lambda_handler(event, context):
    order_id = event.get("order_id")

    if not order_id:
        return {
            "status": "FAILED",
            "message": "Missing order_id"
        }

    # Simulate hold logic (replace with DB update)
    return {
        "status": "SUCCESS",
        "message": f"Order {order_id} is now on HOLD"
    }
