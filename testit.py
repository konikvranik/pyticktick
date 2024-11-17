import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = "yO0CWLTsSt779hE2z8",
    password = "yAW40M1Ta+^4lPwV9#)5wB)1JyKw_th1",
    access_token = "d2538515-39cd-4074-adc6-0c78690cec1f"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    #oauth_token_post_request = openapi_client.OauthTokenPostRequest() # OauthTokenPostRequest |  (optional)

    try:
        # Get token
        api_response = api_instance.open_v1_project_get()
        #api_response = api_instance.oauth_token_post(oauth_token_post_request=oauth_token_post_request)
        print("The response of DefaultApi->oauth_token_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->oauth_token_post: %s\n" % e)
