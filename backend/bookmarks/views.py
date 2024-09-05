# import newrelic.agent
from newrelic import agent
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

logger = logging.getLogger("app")


# logger.setLevel(logging.DEBUG)


# Create your views here.
class GetBookmarksAPI(APIView):
    @staticmethod
    def get(request: Request, *args, **kwargs):
        db = request.query_params.get("db", "default")

        data = {'key': 'value updated mkjfkjfkjfkkj'}

        logger.info("hello another")
        # logger.info(f"{repr(data)}", extra={'request': 'some req', "user_id": "xyz-userzmccc"})
        # logger.warn("warning msg u")
        # logger.error("error isssue up")
        # logger.critical("some crititcal updated")
        # newrelic.agent.add_custom_attribute("user", "som-xbhc")
        # newrelic.agent.add_custom_parameter("uxer", "bdo")

        # transaction = agent.current_transaction()
        # print("t", transaction)
        # if transaction:
        #     transaction.add_custom_attribute('custom_key', 'custom_value')

        return Response(data)


class CreateBookmarksAPI(APIView):
    @staticmethod
    def post(request: Request, *args, **kwargs):
        db = request.query_params.get("db", "default")
        data = request.data

        return Response({"message": "success", "db": db})