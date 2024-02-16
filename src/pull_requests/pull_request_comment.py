import requests
import os
import logging

logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] - %(message)s", force=True
)


class Message:
    """Instance of a message."""

    def __init__(self):
        """Init message class."""
        SYSTEM_COLLECTIONURI = os.getenv("SYSTEM_COLLECTIONURI")
        SYSTEM_PULLREQUEST_PULLREQUESTID = os.getenv("SYSTEM_PULLREQUEST_PULLREQUESTID")
        SYSTEM_TEAMPROJECT = os.getenv("SYSTEM_TEAMPROJECT")
        BUILD_REPOSITORY_ID = os.getenv("BUILD_REPOSITORY_ID")
        self.url = (
            f"{SYSTEM_COLLECTIONURI}{SYSTEM_TEAMPROJECT}/_apis/git/repositories/"
            f"{BUILD_REPOSITORY_ID}/pullRequests/{SYSTEM_PULLREQUEST_PULLREQUESTID}"
            "/threads?api-version=7.0"
        )
        self.headers = {
            "content-type": "application/json",
            "Authorization": f"BEARER {os.getenv('SYSTEM_ACCESSTOKEN')}",
        }

    def add(self, comment: str) -> bool:
        """Add a message to Azure DevOps Pull Request."""
        data = {
            "comments": [{"parentCommentId": 1, "content": comment, "commentType": 1}],
            "status": 1,
        }
        logging.info(f"Sending PR comment to this url: {self.url}")
        r = requests.post(url=self.url, json=data, headers=self.headers)

        logging.info(r.status_code)
        logging.info(r.reason)

        if r.status_code == 200:
            return True
        else:
            return False
