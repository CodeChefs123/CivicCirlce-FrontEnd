from server import BASE_URL, requests


class Volunteer:
    def get_volunteer_opportunities(self, uid):
        response = requests.get(
            f"{BASE_URL}/org/jobs",
            headers={"uid": uid},
        ).json()
        return response["response"][1]

    def get_trainings(self, uid):
        response = requests.get(
            f"{BASE_URL}/org/training",
            headers={"uid": uid},
        ).json()
        return response["response"]

    def apply_for_opportunity(self, uid, opportunity_id):
        response = requests.post(
            f"{BASE_URL}/volunteer/jobs/apply/{opportunity_id}",
            headers={"uid": uid},
            json={"opportunityID": opportunity_id},
        ).json()
        return response["response"]

    def apply_for_training(self, uid, training_id):
        response = requests.post(
            f"{BASE_URL}/volunteer/training/apply",
            headers={"uid": uid},
            json={"trainingID": training_id},
        ).json()
        return response["response"]

    def get_profile(self, uid):
        response = requests.get(
            f"{BASE_URL}/auth/user",
            headers={"uid": uid},
        ).json()
        return response["response"]

    @staticmethod
    def cv(uid, cv_bye_array):
        response = requests.post(
            f"{BASE_URL}/auth/signup",
            headers={"uid": uid},
            json={"CV": cv_bye_array},
        )
        return response
