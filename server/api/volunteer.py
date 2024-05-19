from server import *


class Volunteer:
    def get_volunteer_opportunities(self, uid):
        """
        Get volunteer opportunities for a given user ID.
        Args:
            uid (str): User ID.
        Returns:
            list: List of volunteer opportunities.
        """
        response = requests.get(
            f"{BASE_URL}/org/jobs",
            headers={"uid": uid},
        ).json()
        return response["response"][1]

    def get_trainings(self, uid):
        """
        Get trainings for a given user ID.
        Args:
            uid (str): User ID.
        Returns:
            list: List of trainings.
        """
        response = requests.get(
            f"{BASE_URL}/org/training",
            headers={"uid": uid},
        ).json()
        return response["response"]

    def apply_for_opportunity(self, uid, opportunity_id):
        """
        Apply for a volunteer opportunity.
        Args:
            uid (str): User ID.
            opportunity_id (str): Opportunity ID.
        Returns:
            dict: Response from the server.
        """
        response = requests.post(
            f"{BASE_URL}/volunteer/jobs/apply/{opportunity_id}",
            headers={"uid": uid},
            json={"opportunityID": opportunity_id},
        ).json()
        return response["response"]

    def apply_for_training(self, uid, training_id):
        """
        Apply for a training.
        Args:
            uid (str): User ID.
            training_id (str): Training ID.
        Returns:
            dict: Response from the server.
        """
        response = requests.post(
            f"{BASE_URL}/volunteer/training/apply",
            headers={"uid": uid},
            json={"trainingID": training_id},
        ).json()
        return response["response"]

    def get_profile(self, uid):
        """
        Get user profile.
        Args:
            uid (str): User ID.
        Returns:
            dict: User profile information.
        """
        response = requests.get(
            f"{BASE_URL}/auth/user",
            headers={"uid": uid},
        ).json()
        return response["response"]

    @staticmethod
    def cv(uid, cv_bye_array):
        """
        Upload CV for a user.
        Args:
            uid (str): User ID.
            cv_bye_array (list): CV byte array.
        Returns:
            Response from the server.
        """
        response = requests.post(
            f"{BASE_URL}/auth/signup",
            headers={"uid": uid},
            json={"CV": cv_bye_array},
        )
        return response
