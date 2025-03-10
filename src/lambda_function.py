import json
import numpy as np
import talib as ta

def lambda_handler(event, context):

    close = np.random.random(100)
    print("****** Random values x 100 ******")
    print(close)

    output = ta.SMA(close)
    print("****** SMA ******")
    print(output)

    # list of functions
    print("****** Functions ******")
    for name in ta.get_functions():
        print(name)

    # dict of functions by group
    print("****** Functions by group ******")
    for group, names in ta.get_function_groups().items():
        print(group)
        for name in names:
            print(f"  {name}")

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! v3')
    }

if __name__ == "__main__":
    print(lambda_handler({}, {}))