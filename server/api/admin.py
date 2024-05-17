from server import *


class Admin:
    def is_user_banned(self):
        response = requests.get(
            f"{BASE_URL}/admin/ban",
            json={
                "banUID": self.user_id,
            },
        ).json()
        print(response)
        return response["response"][1]

    def ban_user(self, uid, banUID):
        """
        Bans a user.

        Returns
        -------
        str
            response after banning a user
        """
        response = requests.post(
            f"{BASE_URL}/admin/ban",
            headers={"uid": uid},
            json={
                "banUID": banUID,
            },
        ).json()
        return response["response"][1]

    def un_ban_user(self, uid, banUID):
        """
        Unbans a user.

        Returns
        -------
        str
            response after unbanning a user
        """
        response = requests.put(
            f"{BASE_URL}/admin/ban",
            headers={"uid": uid},
            json={
                "banUID": banUID,
            },
        ).json()
        return response["response"][1]

    def get_all_users(self, uid):
        """
        Gets all users.

        Returns
        -------
        list
            a list of all users
        """
        response = requests.get(f"{BASE_URL}/admin/ban", headers={"uid": uid})
        response = response.json()
        return response["response"]

    def get_membership_requests(self, uid, getAll=False):
        response = requests.get(
            f"{BASE_URL}/admin/membership/requests",
            headers={"uid": uid},
            json={"orgID": getAll, "all": getAll},
        ).json()
        return response

    def approve(self, uid, org_id):
        """
        Sends a POST request and returns the response.

        Returns
        -------
            dict
                response of the POST request
        """

        response = requests.post(
            f"{BASE_URL}/admin/membership/requests",
            headers={"uid": uid},
            json={
                "orgID": org_id,
            },
        ).json()
        print(response)
        return response["response"][1]

    def decline(self, uid, org_id):
        """
        Sends a PUT request and returns the response.

        Returns
        -------
            dict
                response of the PUT request
        """

        response = requests.put(
            f"{BASE_URL}/admin/membership/requests",
            headers={"uid": uid},
            json={"orgID": org_id},
        ).json()
        print(response)
        return response["response"]
