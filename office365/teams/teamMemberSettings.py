from office365.runtime.client_value_object import ClientValueObject


class TeamMemberSettings(ClientValueObject):
    """Settings to configure whether members can perform certain actions, for example, create channels and add bots,
    in the team. """

    def __init__(self):
        self.allowCreateUpdateChannels = True
        self.allowDeleteChannels = True
        self.allowAddRemoveApps = True
        self.allowCreateUpdateRemoveTabs = True
        self.allowCreateUpdateRemoveConnectors = True






