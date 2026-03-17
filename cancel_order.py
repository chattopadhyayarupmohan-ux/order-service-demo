import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Orders")

def lambda_handler(event, context):
    table.update_item(
        Key={"order_id": event["order_id"]},
        UpdateExpression="SET #s = :val",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":val": "CANCELLED"}
    )

    return {"message": "Order cancelled"}
