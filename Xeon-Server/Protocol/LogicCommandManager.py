from Protocol.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
from Protocol.Commands.Client.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from Protocol.Commands.Client.ChangeIconCommand import ChangeIconCommand

commands = {
    500: LogicGatchaCommand,
    505: ChangeIconCommand,
    519: LogicPurchaseOfferCommand,
}