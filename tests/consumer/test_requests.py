# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import pytest
import mock
from distutils.version import StrictVersion
import requests_oauthlib
from flask_dance.consumer.requests import OAuth1Session, OAuth2Session

requires_requests_oauthlib_043 = pytest.mark.skipif(
    StrictVersion(requests_oauthlib.__version__) < StrictVersion('0.4.3'),
    reason="requires requests_oauthlib at version 0.4.3 or higher",
)


FAKE_OAUTH1_TOKEN = {
    "oauth_token": "abcdefg",
    "oauth_token_secret": "hijklmnop",
}
FAKE_OAUTH2_TOKEN = {
    "access_token": "deadbeef",
    "scope": ["custom"],
    "token_type": "bearer",
}


@requires_requests_oauthlib_043
def test_oauth1session_authorized():
    bp = mock.Mock(token=FAKE_OAUTH1_TOKEN)
    sess = OAuth1Session(client_key="ckey", client_secret="csec", blueprint=bp)
    assert sess.authorized == True


@requires_requests_oauthlib_043
def test_oauth1session_not_authorized():
    bp = mock.Mock(token=None)
    sess = OAuth1Session(client_key="ckey", client_secret="csec", blueprint=bp)
    assert sess.authorized == False


def test_oauth2session_authorized():
    bp = mock.Mock(token=FAKE_OAUTH2_TOKEN)
    sess = OAuth2Session(client_id="cid", blueprint=bp)
    assert sess.authorized == True


def test_oauth2session_not_authorized():
    bp = mock.Mock(token=None)
    sess = OAuth2Session(client_id="cid", blueprint=bp)
    assert sess.authorized == False
