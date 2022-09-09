import pickle
import pandas as pd
from flask             import Flask, request, Response, jsonify, render_template, url_for
from rossmann import Rossmann
import inflection
import os






# initialize API
app = Flask( __name__ )

# loading model
model=pickle.load(open("parameters/model_xgb_rossmann_v0.pkl","rb"))


@app.route( '/rossmann/rossmann_predict', methods=['POST'] )
def rossmann_predict():

    test_json = request.get_json(force=True)
   
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple example
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            
        # Instantiate Rossmann class
        pipeline = Rossmann()
        
        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )
        
        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # data preparation
        df3 = pipeline.data_preparation( df2 )
        
        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
        
        
    else:
        return Response( '{}', status=200, mimetype='application/json' )

if __name__ == '__main__':
    app.run(debug=True)
