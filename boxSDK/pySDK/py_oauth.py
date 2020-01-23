from boxsdk import OAuth2, Client

token = input("Provide Access Token:  ")

auth = OAuth2(
    client_id='zzpznrktqtckmc7luqj8wo56171bkft5',
    client_secret='izLk3hpBQA5Sa1J8iTvEbPOlpEWbsoeh',
    access_token=token,
)
client = Client(auth)

user = client.user().get()
print('The current user ID is {0}'.format(user.id))
