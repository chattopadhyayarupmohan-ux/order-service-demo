import boto3, uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Orders")

def lambda_handler(event, context):
    order_id = str(uuid.uuid4())

    table.put_item(Item={
        "order_id": order_id,
        "customer": event["customer"],
        "product": event["product"],
        "status": "CREATED"
    })

    return {"message": f"Order {order_id} created"}
