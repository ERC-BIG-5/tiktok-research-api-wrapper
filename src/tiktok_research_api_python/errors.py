# Copyright 2024 TikTok Pte. Ltd.
#
# This source code is licensed under the MIT license found in
# the LICENSE file in the root directory of this source tree.

__all__ = ["APIErrorResponse", "ServerError"]


class APIErrorResponse:
    OK = "ok"
    INVALID_PARAM = "invalid_param"
    INVALID_REQUEST = "invalid_request"
    ACCESS_TOKEN_INVALID = "access_token_invalid"
    TIMEOUT = "timeout"

    def __str__(self):
        return self.value


class ServerError(Exception):
    """The API kept failing a request with a server error (HTTP 5xx or an unparsable body)."""

    def __init__(self, status_code, error_code=None, error_msg=None, log_id=None):
        self.status_code = status_code
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        super().__init__(f"{status_code=}; {error_code=}; {error_msg=}; {log_id=}")
