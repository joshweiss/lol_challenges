from lcu_driver import Connector


class LCU(object):
    connector = Connector()
    summoner_info = {}

    def __init__(self):
        self.connector.start()

    @staticmethod
    @connector.ready
    async def connect(connection):
        summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
        print('Got new summoner:', await summoner.json())
        LCU.summoner_info = await summoner.json()

    @staticmethod
    @connector.close
    async def disconnect(connection):
        print('Finished task')

    # # subscribe to '/lol-summoner/v1/current-summoner' endpoint for the UPDATE event
    # # when an update to the user happen (e.g. name change, profile icon change, level, ...) the function will be called
    # @connector.ws.register('/lol-summoner/v1/current-summoner', event_types=('UPDATE',))
    # async def icon_changed(connection, event):
    #     print(f'The summoner {event.data["displayName"]} was updated.')
