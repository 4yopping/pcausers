"""This module make the PCA analisis over a sample of users"""
import boto3
import numpy as np
from sklearn.decomposition import PCA
LAMBDA = boto3.client('lambda', region_name='us-east-1')
def pca(params, ctx):
    """ this function take a sample from user DB and make PCA analisis"""
    print params
    sampling = LAMBDA.invoke(
        FunctionName='saveUser',
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=str({
            "action" : "findRandom",
            "conditions" : {},
            "fields" : {},
            "options" :{
                "limit":params['sample']
            }
        })
    )
    print sampling
    return sampling
