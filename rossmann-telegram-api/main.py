import json
import requests
import pandas as pd
from flask import Flask, request, Response

#constants
TOKEN="5471778368:AAGFUDx-zO7iKyh4dzChLGG1RQWYoavuCUA"

# #Info about the Bot
# https://api.telegram.org/bot5471778368:AAGFUDx-zO7iKyh4dzChLGG1RQWYoavuCUA/getMe


# #get updates
# https://api.telegram.org/bot5471778368:AAGFUDx-zO7iKyh4dzChLGG1RQWYoavuCUA/getUpdates

# #WebHook updates
# https://api.telegram.org/bot5471778368:AAGFUDx-zO7iKyh4dzChLGG1RQWYoavuCUA/setWebhook?url=

# #WebHook google cloud
# https://api.telegram.org/bot5471778368:AAGFUDx-zO7iKyh4dzChLGG1RQWYoavuCUA/setWebhook?url=https://botrossmann.rj.r.appspot.com\

# #send message
# https://api.telegram.org/bot5471778368:AAGFUDx-zO7iKyh4dzChLGG1RQWYoavuCUA/sendMessage?chat_id=5773423495text&text=Hi Kos, I am doing good, tks!

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/"
    url = url + f'sendMessage?chat_id={chat_id}'

    r=requests.post( url, json = {'text': text})
    print(f'Status Code {r.status_code}')
    return None

def load_dataset(store_id):
    #loading test to df
    df10=pd.read_csv("data/test.csv")
    store=pd.read_csv('data/store.csv')

    # merge test dataset +store
    df_test=df10.merge(store,how='left',on='Store')

    #choose store for prediction
    df_test = df_test[df_test['Store'] == store_id]

    if not df_test.empty:
        #remove closed days
        df_test=df_test[(df_test['Open']!=0) & (~df_test['Open'].isnull())]
        # convert Dataframe to json
        data = json.dumps(df_test.to_dict(orient='records'))

    else:
        data='error'

    return data

def predict (data):
    url="https://rossmann-361410.rj.r.appspot.com/rossmann/rossmann_predict"
    data=data

    header = {'Content-type':  'application/json','debug':'True'}

    r=requests.post(url, data, headers=header)
    print( f'Status Code {r.status_code}')

    d1 = pd.DataFrame( r.json(), columns=r.json()[0].keys())

    return d1


def parse_message(message):
    chat_id = message['message']['chat']['id']
    store_id = message['message']['text']
    store_id=store_id.replace("/","")

    try:
        store_id = int(store_id)
    except ValueError:
        store_id = 'error'


    return chat_id, store_id

#API initialize
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        message = request.get_json()
        chat_id, store_id = parse_message(message)



        if store_id != 'error':
            #loading data
            data = load_dataset(store_id)

            if data != 'error':
                d1 = predict(data)

                #prediction
                d1 = predict(data)
                #calculation
                d2 = d1[['Store', 'prediction']].groupby( 'Store' ).sum().reset_index()

                
                msg =  'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( 
                            d2['Store'].values[0], 
                            d2['prediction'].values[0] ) 

                send_message(chat_id, msg)
                return Response('Ok', status=200)


            #send message

            else:
                send_message(chat_id, "Store Not Available")
                return Response( "Ok", status=200)


        else:
            send_message(chat_id,' Store ID is Wrong')
            return Response("Ok",status=200)


    else:
        return "<h1> Rossmann Telegram BOT </h1>"


if __name__ == '__name__':
    app.run(debug=True)




# d2 = d1[['Store', 'prediction']].groupby( 'Store' ).sum().reset_index()

# for i in range( len( d2 ) ):
#     print( 'Store Number {} will sell R${:,.2f} in the next 6 weeks'.format( 
#             d2.loc[i, 'Store'], 
#             d2.loc[i, 'prediction'] ) )