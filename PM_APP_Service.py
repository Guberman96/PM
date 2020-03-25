from PM_APP_Models import RequirementsModel

class ReqServ:
    def __init__(self):
        self.model = RequirementsModel()

    def create(self, params):
        return self.model.create(params)