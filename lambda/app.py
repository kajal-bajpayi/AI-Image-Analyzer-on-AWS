import json

def lambda_handler(event, context):
    try:
        image_name = event['queryStringParameters']['image_name']

        response = {
            "image_name": image_name,
            "status": "processed",
            "message": "Image analyzed successfully"
        }

        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
