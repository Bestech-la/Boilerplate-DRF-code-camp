import datetime

from django.core.cache import cache
from django.utils.deconstruct import deconstructible

import google.auth
import google.auth.compute_engine
import google.auth.transport.requests
# We'll take it on the chin if this moves
from google.cloud.storage.blob import _quote
from storages.backends.gcloud import GoogleCloudStorage
from storages.utils import clean_name


@deconstructible
class GoogleCloudStorageAccessToken(GoogleCloudStorage):
    CACHE_KEY = "GoogleCloudStorageAccessToken.signing_extras"

    def url(self, name):
        """
        Return public url or a signed url for the Blob.
        This DOES NOT check for existance of Blob - that makes codes too slow
        for many use cases.

        We override this to provide an extra information to url signing, so we don't need to have a private key
        available. This is a workaround for https://github.com/jschneier/django-storages/issues/941.
        """
        name = self._normalize_name(clean_name(name))
        blob = self.bucket.blob(name)
        no_signed_url = self.default_acl == "publicRead" or not self.querystring_auth

        if not self.custom_endpoint and no_signed_url:
            return blob.public_url
        elif no_signed_url:
            return "{storage_base_url}/{quoted_name}".format(
                storage_base_url=self.custom_endpoint,
                quoted_name=_quote(name, safe=b"/~"),
            )
        elif not self.custom_endpoint:
            return blob.generate_signed_url(self.expiration, **self.signed_url_extra())
        else:
            return blob.generate_signed_url(
                expiration=self.expiration,
                api_access_endpoint=self.custom_endpoint,
                **self.signed_url_extra()
            )

    def signed_url_extra(self):
        value = cache.get(self.CACHE_KEY)
        if value is not None:
            expiry, extra = value
            if expiry > datetime.datetime.utcnow():
                return extra

        credentials, project_id = google.auth.default()
        auth_req = google.auth.transport.requests.Request()
        credentials.refresh(auth_req)
        extra = {
            "service_account_email": credentials.service_account_email,
            "access_token": credentials.token,
            "credentials": credentials,
        }

        cache.set(self.CACHE_KEY, (credentials.expiry, extra))
        return extra