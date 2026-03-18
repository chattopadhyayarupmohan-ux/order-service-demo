import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Orders")

def lambda_handler(event, context):
    order_id = event.get("order_id")
    if not order_id:
        return {"status": "error", "message": "order_id is missing"}

    # Update order status to SHIPPED
    table.update_item(
        Key={"order_id": order_id},
        UpdateExpression="SET #s = :val",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":val": "SHIPPED"}
    )

    return {"status": "success", "message": f"Order {order_id} marked as shipped"}
