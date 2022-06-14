import json
import time

import requests


def update_repo(workspace, auth_token, id, data):
    headers = get_header(auth_token)

    try:
        req = requests.patch(url=('https://%s.cloud.databricks.com/api/2.0/repos/%s' % (workspace, id)),
                             json=data, headers=headers)
        print(req.status_code)
        res = json.loads(req.content.decode('utf-8'))
        return res
    except Exception as e:
        print(e)
        message = 'Error getting Batch Job status'
        print(message)
        raise Exception(message)


def submit_job(workspace, auth_token, data):
    headers = get_header(auth_token)

    try:
        req = requests.post(url=('https://%s.cloud.databricks.com/api/2.0/jobs/runs/submit' % workspace),
                            json=data, headers=headers)
        print(req.status_code)
        res = json.loads(req.content.decode('utf-8'))
        return res['run_id']
    except Exception as e:
        print(e)
        message = 'Error getting Batch Job status'
        print(message)
        raise Exception(message)


def get_repos(workspace, path, auth_token):
    headers = get_header(auth_token)

    req = requests.get(url="https://%s.cloud.databricks.com/api/2.0/repos?path_prefix=%s" % (workspace, path),
                       headers=headers)
    res = json.loads(req.content.decode('utf-8'))
    return res


def get_job_status(run_id, workspace, auth_token):
    headers = get_header(auth_token)

    req = requests.get(url="https://%s.cloud.databricks.com/api/2.0/jobs/runs/get?run_id=%s" % (workspace, run_id),
                       headers=headers)
    res = json.loads(req.content.decode('utf-8'))
    return res['state']


def get_header(auth_token):
    return {
        'Content-Type': 'application/json',
        'Authorization': ('Bearer %s' % auth_token)
    }


def wait_job_completion(run_id, workspace, auth_token):
    for i in range(100):
        time.sleep(10)
        status = get_job_status(run_id, workspace, auth_token)
        print(status)
        if status['life_cycle_state'] in ['TERMINATED', 'INTERNAL_ERROR']:
            return status['result_state']

    return "TIMED OUT"  # SUCCESS FAILED


