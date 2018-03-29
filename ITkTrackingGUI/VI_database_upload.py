#!/usr/bin/python
import json
import httplib2 as httplib2
import httplib2
import sys
import os
import getpass
from pathlib import Path
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

UU_OIDC_GATEWAY = "https://oidc.plus4u.net"
UU_OIDC_TOKEN_URI = "/uu-oidcg01-main/0-0/grantToken"

CMD_GATEWAY = "https://uuos9.plus4u.net"
TID = "98234766872260181"
AWID = "dcb3f6d1f130482581ba1e7bbe34413c"
CMD_UPLOAD_TESTRUN_RESULTS = '/cern-itkpd-test/' + TID + '-' + AWID + '/uploadTestRunResults'
CMD_CREATE_TESTRUN_ATTACHMENT = '/cern-itkpd-test/' + TID + '-' + AWID + '/createTestRunAttachment'

INPUT_FLD = "./input_TestResults"
PROCESSED_FLD = "./processed"

http = httplib2.Http()

class CommandError(Exception):
    """Error thrown when some problem occures in communication with uuOIDC server. """
    def __init__(self, status, code, message):
        super(CommandError, self).__init__(message)
        self.status = status
        self.code = code
        self.message = message

    def __str__(self):
        return str(self.status) + "," + self.code + "," + self.message

def oidc_grant_token(access_code_1, access_code_2):
    post_data = {"grant_type": "password",
                 "username": access_code_1,
                 "password": access_code_2
                }

    headers = {'Content-Type': 'application/json'}

    url = UU_OIDC_GATEWAY + UU_OIDC_TOKEN_URI

    response, content = http.request(url, "POST", headers=headers, body=json.dumps(post_data))

    if response.status >= 200 and response.status < 300:
        token_json = str(content.decode())
        return token_json
    else:
        status = response.status
        error_json = json.loads(str(content.decode()))
        raise CommandError(status, error_json["code"], error_json["message"])

def process_commands(token, component, testType, institution, runNumber, flag, problem, properties, results, comments, uploadedfile):
    #input_dir = Path(INPUT_FLD)
  processed_dir = Path(PROCESSED_FLD)
  if not processed_dir.is_dir():
    os.makedir("processed")
  response_json = upload_results(token, component, testType, institution, runNumber, flag, problem, properties, results, comments)
  testRun_code = json.loads(response_json)["testRun"]["id"] #uuObject testType not yet included in the database
  create_testRun_attachment(token, testRun_code, uploadedfile)
  new_filename = file.split(".")[0] + "_processed.json"
  processed_file = open(PROCESSED_FLD + "/" + new_filename, "w")
  if response_json is not None:
    processed_file.write(response_json)
  processed_file.close()

  print("Visual inspection results registered successfully!")

def create_testRun_attachment(token, code, filename):
    headers = {'Authorization':'Bearer '+ token}

    url = CMD_GATEWAY + CMD_CREATE_TESTRUN_ATTACHMENT

    files = {'data': (filename, open(INPUT_FLD + "/" + filename, 'rb'))}
    data={
      "testRun": code,
      "title": "Visual Inspection",
      "description": "Results explained in comments.",
      "data": (filename, open(INPUT_FLD + "/" + filename, 'rb'))
    }

    response = requests.post(url, headers=headers, files=files, data=data)

def upload_results(token, component, testType, institution, runNumber, flag, problem, properties, results, comments):
  headers = {'Authorization':'Bearer '+ token,
             'Content-type':'application/json'}

  url = CMD_GATEWAY + CMD_UPLOAD_TESTRUN_RESULTS

  data = {
      "component": component,
      "testType" : testType,
      "institution" : institution,
      "runNumber" : runNumber,
      "passed" : flag,
      "problem" : problem,
      "properties" : properties,
      "results" : results,
      "comments" : comments
  }

  response, content = http.request(url, "POST", headers=headers, body=data)

  if response.status >= 200 and response.status < 300:
    response_json = str(content.decode())
    return response_json
  else:
    status = response.status
    error_json = json.loads(str(content))
    raise CommandError(status, error_json["code"], error_json["message"])

def Database_upload(component, testType, institution, runNumber, flag, problem, properties, results, comments, uploadedfile):
  try:
    print("*** ITk Production Database Bot ***")
    print("Please, sign in to the ITk Production Database")
    print("")
    access_code_1 = getpass.getpass("Access Code 1: ")
    access_code_2 = getpass.getpass("Access Code 2: ")
    token = oidc_grant_token(access_code_1, access_code_2)
    token_json = json.loads(token)
    print("Welcome to the ITk Production Database! Results of visual inspection are being uploaded ...")
    print("")
    process_commands(token_json["id_token"], component, testType, institution, runNumber, flag, problem, properties, results, comments, uploadedfile)
  except Exception as e:
    print('500,CLIENT_UNEXPECTED_ERROR,' + str(e))
    exit(1)
