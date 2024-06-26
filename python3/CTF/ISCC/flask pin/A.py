import base64
import json

# JWT token to decode
token = ""

# Split the token into its parts
header, payload, signature = token.split('.')

# Decode the payload
decoded_payload = base64.urlsafe_b64decode(payload + '==').decode('utf-8')
payload_data = json.loads(decoded_payload)

print(payload_data)
