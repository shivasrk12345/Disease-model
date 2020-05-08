import pytest
from app import Base_code
import flask
import urllib
from flask import request, jsonify

import json
app =flask.Flask(__name__)
import sys



def test_checkdatacalculate_display():
    data=Base_code.calculate_display();
    assert data is not None;

"""
def test_datatypeofcalculate_display():
    data=Base_code.calculate_display();
    assert type(data) == str

def test_dictionaryresults_calculate_display():
    data=Base_code.calculate_display();
    dic= json.loads(data);
    assert len(dic) == 4


def test_dicinteral1results_calculate_display():
    data=Base_code.calculate_display();
    dic= json.loads(data);
    assert type(dic['matrix']) == list ;

def test_dicinteral2results_calculate_display():
    data=Base_code.calculate_display();
    dic= json.loads(data);
    assert type(dic['startpatientcount']) == int ;

def test_dicinteral3results_calculate_display():
    data=Base_code.calculate_display();
    dic= json.loads(data);
    assert type(dic['infected_patients']) == int ;




def test_upload():
    #client =  flask.Flask.test_client()
    app.testing = True
    client = app.test_client()
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
	"rows":"10",
	"cols":"10",
	"start":"1",
	"end":"2",
	"points":"[(0,0);(0,1)]"

}
    url = '/post/values'

    response = client.post(url, data=data, headers=headers)

    assert response.content_type == 'text/html'
    #assert response.status_code == 200
    #assert response.json['rows'] == 10


"""













