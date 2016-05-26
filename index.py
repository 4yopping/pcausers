"""This module make the PCA analisis over a sample of users"""
import boto3
LAMBDA = boto3.client('lambda')
def pca(params):
    """ this function take a sample from user DB and make PCA analisis"""
    sampling = LAMBDA.invoke(
        FunctionName='saveUser',
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload={
            "action" : "findRandom",
            "conditions" : {},
            "fields" : {},
            "options" :{
                "limit":params.sample | 1
            }
        }
    )
    print sampling
