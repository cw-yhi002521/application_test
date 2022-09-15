# -*- coding:utf-8 -*-
"""locust-test-module"""
from locust import TaskSet, task, LoadTestShape
from locust_plugins.users import RestUser


class MyTaskSet(TaskSet):
    """taskSet"""

    @task
    def get_dna_analyses(self, **kwargs):
        """get_dna_analyses"""
        return self.client.get("/phr-dna/apps/v1/dna-analyses", name="/dna-analyses", **kwargs)

    @task
    def post_dna_analyses(self, **kwargs):
        """get_user_dna"""
        return self.client.post("/phr-dna/apps/v1/dna-analyses", name="/dna-analyses", **kwargs)

    @task
    def post_dna_kits_users_uid(self, uid, **kwargs):
        """post_dna_kits_users_uid"""
        return self.client.post("/phr-dna/apps/v1/dna-kits/users/{0}".format(uid)
                                , name="/dna-kits/users/{uid}", **kwargs)

    @task
    def patch_dna_kits_users_uid(self, uid, **kwargs):
        """patch_dna_kits_users_uid"""
        return self.client.patch("/phr-dna/apps/v1/dna-kits/users/{0}".format(uid)
                                 , name="/dna-kits/users/{uid}", **kwargs)

    @task
    def post_messages_completed(self, **kwargs):
        """post_messages_completed"""
        return self.client.post("/phr-dna/apps/v1/messages/completed"
                                , name="/messages/completed", **kwargs)

    @task
    def get_trait(self, **kwargs):
        """get_trait"""
        return self.client.get("/phr-dna/apps/v1/trait"
                               , name="/trait", **kwargs)

    @task
    def post_trait_users_uid(self, uid, **kwargs):
        """post_trait_users_uid"""
        return self.client.post("/phr-dna/apps/v1/trait/users/{0}".format(uid)
                                , name="/trait/users/{uid}", **kwargs)


class MyLocust(RestUser):
    """locustClass"""
    tasks = [MyTaskSet]
    min_wait = 1000
    max_wait = 3000
    host = "https://boapi.hb.id-im.dev" 
