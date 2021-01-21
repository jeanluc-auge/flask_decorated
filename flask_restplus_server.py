import functools
from flask import Flask, request  # , redirect, render_temple
from flask_restplus import Resource, Api, reqparse, fields
from macros import LcdnContentdClient, LcdnSecretClient
from generate_endpoints import render_data_generator
import json
import sys

# ******* define Flask api *******
app = Flask(__name__)
api = Api(app)

# ********* contentd api *************
contentd = api.namespace("contentd", description="macros for Akamai LCDN contentd")
contentd_client = LcdnContentdClient()

# ********* secret api *************
secret = api.namespace("secret", description="macros for Akamai LCDN secret")
secret_client = LcdnSecretClient()


# def get_rest_method(client, func_name):
#     def wrapper(self, *args, **kwargs):
#         response = getattr(client, func_name)(*args, **kwargs)
#         status_code = 200 if response else 400
#         return (response, status_code)
#
#     return wrapper
#
#
# reduce_attr = lambda base_object, attr_list: functools.reduce(
#     getattr, attr_list, base_object
# )

# for data in render_data_generator():
#     # {"endpoints": endpoints, "namespace": namespace, "client": client}
#     # endpoints = {
#     #     endpoint_name: {
#     #         'class_name': class_name,
#     #         'methods': [{
#     #             'rest_method': func.rest_method,
#     #             'func_name': func.__name__,
#     #             'func_args': {'path_args': _, 'free_args': _}
#     #         }]
#     #     }
#     # }
#     module = sys.modules[__name__]
#     client = getattr(module, data.client)
#     namespace = getattr(module, data.namespace)
#     for endpoint_name, endpoint_data in data.endpoints.items():
#         endpoint_class = type(
#             endpoint_data.class_name,
#             (Resource,),
#             {
#                 method.rest_method: api.doc(description=reduce_attr(module, [data.client, method.func_name, '__doc__']))(
#                     get_rest_method(client,method.func_name)
#                 )
#                 for method in endpoint_data.methods
#             }
#         )
#         endpoint_class = getattr(namespace, 'route')(endpoint_name)(endpoint_class)

endpoint_class = type(
    "Provider_account",
    (Resource,),
    {
        "get": api.doc(description=contentd_client.get_content_provider.__doc__)(
            lambda self, account: contentd_client.get_content_provider(account)
        )
    },
)

endpoint_class = contentd.route("/provider/<string:account>")(endpoint_class)

# ********** endpoints declaration ****************
# @contentd.route('/provider/<string:account>')
# class Provider_account(Resource):
#     @api.doc(
#         description=contentd_client.get_content_provider.__doc__
#     )
#     def get(self, account):
#         base_path = request.args.get('base_path')
#         response = contentd_client.get_content_provider_id(
#              account=account, base_path=base_path,
#         )
#         status_code = 200 if response else 400
#         return (
#             response, status_code
#         )


if __name__ == "__main__":
    # ***** start app server *******
    app.run(debug=True, host="0.0.0.0", port=9999)
