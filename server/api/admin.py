from server import *


class Admin:
    def is_user_banned(self):
        """
        Checks if a user is banned.
        Returns
        -------
        bool
            True if the user is banned, False otherwise.
        """
        response = requests.get(
            f"{BASE_URL}/admin/ban",
            json={
                "banUID": self.user_id,
            },
        ).json()
        return response["response"][1]

    def ban_user(self, uid, banUID):
        """
        Bans a user.
        Parameters
        ----------
        uid : str
            The user ID of the admin.
        banUID : str
            The user ID of the user to be banned.
        Returns
        -------
        str
            Response after banning a user.
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
        Parameters
        ----------
        uid : str
            The user ID of the admin.
        banUID : str
            The user ID of the user to be unbanned.
        Returns
        -------
        str
            Response after unbanning a user.
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
        Parameters
        ----------
        uid : str
            The user ID of the admin.
        Returns
        -------
        list
            A list of all users.
        """
        response = requests.get(f"{BASE_URL}/admin/ban", headers={"uid": uid})
        response = response.json()
        return response["response"]

    def get_membership_requests(self, uid, getAll=False):
        """
        Gets membership requests.
        Parameters
        ----------
        uid : str
            The user ID of the admin.
        getAll : bool, optional
            If True, gets all membership requests. If False, gets only pending requests. Default is False.
        Returns
        -------
        dict
            The response of the GET request.
        """
        response = requests.get(
            f"{BASE_URL}/admin/membership/requests",
            headers={"uid": uid},
            json={"orgID": getAll, "all": getAll},
        ).json()
        return response

    def approve(self, uid, org_id):
        """
        Approves a membership request.
        Parameters
        ----------
        uid : str
            The user ID of the admin.
        org_id : str
            The organization ID of the membership request to be approved.
        Returns
        -------
        str
            Response after approving the membership request.
        """
        response = requests.post(
            f"{BASE_URL}/admin/membership/requests",
            headers={"uid": uid},
            json={
                "orgID": org_id,
            },
        ).json()
        return response["response"][1]

    def decline(self, uid, org_id):
        """
        Declines a membership request.
        Parameters
        ----------
        uid : str
            The user ID of the admin.
        org_id : str
            The organization ID of the membership request to be declined.
        Returns
        -------
        dict
            Response after declining the membership request.
        """
        response = requests.put(
            f"{BASE_URL}/admin/membership/requests",
            headers={"uid": uid},
            json={"orgID": org_id},
        ).json()
        return response["response"]
