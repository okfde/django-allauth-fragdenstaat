from allauth.socialaccount.tests import create_oauth2_tests
from allauth.tests import MockedResponse
from allauth.socialaccount.providers import registry

from .provider import FragdenstaatProvider


class FragdenstaatTests(create_oauth2_tests(registry.by_id(
      FragdenstaatProvider.id))):
    def get_mocked_response(self):
        return MockedResponse(200, """{
  "id": 1,
}""")
