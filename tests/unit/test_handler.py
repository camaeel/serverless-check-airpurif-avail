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
    # assert ret["body"] == "Ok"


def test_check_skus_avilability_1():
    availability_data = {'material': ['883405950010', '883421550010', '883421750010', '883425610020', '883465910020', '883472951010', '883482910020', '883488910020'], 'unrestr': [0, 1, 12, 0, 0, 39, 1, 0]}
    skus = [('883405950010', 'name1')]

    ret = app.check_skus_avilability(skus, availability_data)
    
    assert len(ret) == 0

def test_check_skus_avilability_2():
    availability_data = {'material': ['883405950010', '883421550010', '883421750010', '883425610020', '883465910020', '883472951010', '883482910020', '883488910020'], 'unrestr': [0, 1, 12, 0, 0, 39, 1, 0]}
    skus = [('883421750010','name1')]

    ret = app.check_skus_avilability(skus, availability_data)

    assert len(ret) == 1
    assert ret[0] == ('883421750010','name1')

def test_check_skus_avilability_3():
    availability_data = {'material': ['883405950010', '883421550010', '883421750010', '883425610020', '883465910020', '883472951010', '883482910020', '883488910020'], 'unrestr': [0, 1, 12, 0, 0, 39, 1, 0]}
    skus = [('883421750010','name1'), ('883405950010','name2')]

    ret = app.check_skus_avilability(skus, availability_data)

    assert len(ret) == 1
    assert ret[0] == ('883421750010','name1')

def test_check_skus_avilability_4():
    availability_data = {'material': ['883405950010', '883421550010', '883421750010', '883425610020', '883465910020', '883472951010', '883482910020', '883488910020'], 'unrestr': [0, 1, 12, 0, 0, 39, 1, 0]}
    skus = [('883421750010','name1'), ('883421550010','name2')]

    ret = app.check_skus_avilability(skus, availability_data)

    assert len(ret) == 2
    assert ret[0] == ('883421750010','name1')
    assert ret[1] == ('883421550010','name2')
