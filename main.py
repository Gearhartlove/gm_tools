import getpass
import os

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langgraph.prebuilt import create_react_agent
from pydantic.main import BaseModel
from random import randint


class DiceRoll(BaseModel):
    total: int
    rolls: list[int]


# KGF TODO: get ai to roll dice
def roll_dice(number: int, dice_kind: int) -> DiceRoll:
    """Roll dice of the same kind. Example: roll 2d20 means roll a 'd20' twice and total their result."""
    DIE_MINIMUM = 1

    rolls = []
    total = 0
    for _ in range(number):
        roll = randint(DIE_MINIMUM, dice_kind)
        rolls.append(roll)
        total += roll

    return DiceRoll(total=total, rolls=rolls)


def main():
    if not os.environ.get("ANTHROPIC_API_KEY"):
        os.environ["ANTHROPIC_API_KEY"] = getpass.getpass(
            "Enter API key for anthropic: "
        )

    model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")

    messages = [
        SystemMessage("You are a pirate, talk like one!"),
        HumanMessage("Hello, world!"),
    ]

    result = model.invoke(messages)
    print(result)


if __name__ == "__main__":
    main()
