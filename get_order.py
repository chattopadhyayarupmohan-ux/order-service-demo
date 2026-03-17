import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Orders")

def lambda_handler(event, context):
    res = table.get_item(Key={"order_id": event["order_id"]})
    return res.get("Item", {"message": "Not found"})
