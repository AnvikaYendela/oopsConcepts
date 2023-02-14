import abc


class createCampaign():
    @abc.abstractmethod
    def fillCampaignData(self):
        pass

    @abc.abstractmethod
    def fillAdDetails(self):
        pass

    @abc.abstractmethod
    def addCreatives(self):
        pass


class Engagements(createCampaign):
    def fillCampaignData(self):
        print("Perform operation to fill campaign data")

    def fillAdDetails(self):
        print("Perform operation to fill ad details data")


myapp = Engagements()
myapp.fillAdDetails()
