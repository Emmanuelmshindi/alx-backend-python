#!/usr/bin/env python3
"""A test suite for client.py
"""
import client
import unittest
from unittest.mock import patch
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, mock_get_json):
        mock_get_json.return_value = expected

        result = self.org()

        mock_get_json.assert_called_once_with(org)

        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        known_payload = {
            "repos_url": "https://api.github.com/orgs/example_org/repos"
        }
        mock_org.return_value = known_payload

        github_org_client = GithubOrgClient("example_org")

        result = github_org_client._public_repos_url

        mock_org.assert_called_once()

        expected_url = known_payload["repos_url"]

        self.assertEqual(result, expected_url)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos(self, mock_repos_url, mock_get_json):
        known_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = known_payload

        mock_repos_url.return_value = "https://api.github.com/orgs/example_org/repos"
        github_org_client = GithubOrgClient("example_org")

        result = github_org_client.public_repos()

        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/example_org/repos"    
        )
        expected_repos = ["repo1", "repo2"]
        self.assertEqual(result, expected_repos)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", True),
    ])
    def test_has_license(self, repo, license_key, expected):
        github_org_client = GithubOrgClient("example_org")

        result = github_org_client.has_license(repo, license_key)

        self.assertEqual(result, expected)

@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(org_payload, repos_payload, expected_repos, apache2_repos)])

class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls, org_payload, repos_payload,
        expected_repos, apache2_repos):
        cls.get_patcher = patch('client.requests.get')

        cls.mock_get = cls.patcher.start()

        cls.mock_get.side_effect = [
            MockResponse(org_payload),
            MockResponse(repos_payload)
        ]

        cls.org_payload = org_payload
        cls.repos_payload = repos_payload
        cls.expected_repos = expected_repos
        cls.apache2_repos = apache2_repos

    @classmethod
    def tearDownClass():
        cls.get_patcher.stop()

    def test_public_repos(self):
        github_org_client = GithubOrgClient("example_org")

        result = github_org_client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        github_org_client = GithubOrgClient("example_org")

        result = github_org_client.public_repos(license="apache-2.0")

        self.assertEqual(result, self.apache2_repos)

if __name__ == "__main__":
    unittest.main()
