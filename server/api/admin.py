class Admin:
    def is_user_banned(self):
        response = requests.get(
            self.url,
            headers=self.headers,
            json={
                "banUID": self.user_id,
            },
        ).json()
        print(response)
        return response["response"][1]

    def ban_user(self):
        """
        Bans a user.

        Returns
        -------
        str
            response after banning a user
        """
        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "banUID": self.user_id,
            },
        ).json()
        return response["response"][1]

    def un_ban_user(self):
        """
        Unbans a user.

        Returns
        -------
        str
            response after unbanning a user
        """
        response = requests.put(
            self.url,
            headers=self.headers,
            json={
                "banUID": self.user_id,
            },
        ).json()
        return response["response"][1]

    def get_all_users(self):
        """
        Gets all users.

        Returns
        -------
        list
            a list of all users
        """
        response = requests.get(BASE_URL + "/api/auth/all", headers=self.headers)
        response = response.json()
        return response["response"][1]

    def get_membership_requests(self, getAll=False):
        response = requests.get(
            self.url,
            headers=self.headers,
            json={"all": getAll},
        ).json()
        return response["response"][1]

    def approve(self):
        """
        Sends a POST request and returns the response.

        Returns
        -------
            dict
                response of the POST request
        """

        response = requests.post(
            self.url,
            headers=self.headers,
            json={
                "registrationCertificateUrl": registrationCertificateUrl,
                "annualReportUrl": annualReportUrl,
                "legalDocumentsUrl": legalDocumentsUrl,
                "name": name,
                "email": email,
                "password": password,
                "description": description,
                "requestID": self.requestID,
            },
        ).json()
        print(response)
        return response["response"][1]

    def decline(self):
        """
        Sends a PUT request and returns the response.

        Returns
        -------
            dict
                response of the PUT request
        """

        response = requests.put(
            self.url,
            headers=self.headers,
            json={
                "registrationCertificateUrl": registrationCertificateUrl,
                "annualReportUrl": annualReportUrl,
                "legalDocumentsUrl": legalDocumentsUrl,
                "name": name,
                "email": email,
                "password": password,
                "description": description,
                "requestID": self.requestID,
            },
        ).json()
        print(response)
        return response["response"][1]
