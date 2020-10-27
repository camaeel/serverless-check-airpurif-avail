import json
import pytest

from check_airpurif_avail import app


@pytest.fixture()
def cloud_watch_schedule_event():
    """ Generates schedule Event"""

    return {
            "version": "0",
            "id": "123123-123",
            "detail-type": "Scheduled Event",
            "source": "aws.events",
            "account": "433854569226",
            "time": "2020-10-27T22:05:19Z",
            "region": "eu-west-1",
            "resources": [
                "arn:aws:events:eu-west-1:433854569226:rule/CheckPurifAvailSchedule"
            ],
            "detail": {}
        }



def test_lambda_handler(cloud_watch_schedule_event):

    ret = app.lambda_handler(cloud_watch_schedule_event, "")

    assert ret["statusCode"] == 200
    assert ret["body"] == "Ok"
    # assert "location" in data.dict_keys()
