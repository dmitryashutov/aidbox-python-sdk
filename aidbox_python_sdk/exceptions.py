import json
from aiohttp import web


class AidboxSDKException(web.HTTPError):
    status_code = 422

    def __init__(self, *, reason):
        web.HTTPError.__init__(
            self,
            text=json.dumps({
                'resourceType': 'OperationOutcome',
                'status': 422,
                'issue': [{
                    'severity': 'error',
                    'code': 'invalid',
                    'diagnostics': reason or 'Error',
                }]
            }),
            content_type='application/json',
        )


class AidboxDBException(AidboxSDKException):
    pass
