from enum import Enum
from typing import Any

class ConfigType(Enum):
    BOOL = 0
    STR = 1

class ConfigValue:
    desc: str
    value: Any
    config_type: ConfigType

    def __init__(self, desc: str, default_val):
        self.desc = desc
        self.value = default_val
        if isinstance(default_val, bool):
            self.config_type = ConfigType.BOOL
        elif isinstance(default_val, str):
            self.config_type = ConfigType.STR

    def set(self, val):
        if val.lower() == "true":
            self.value = True
        elif val.lower() == "false":
            self.value = False
        else:
            self.value = val

configs = dict()

def init():
    configs["prefix"] = ConfigValue("The prefix Moxie will use", "$")

async def list_configs(ctx):
    final = ""
    for name,config in configs.items():
        final += f"{name}: {config.desc}\n\tValue: {config.value}\n"
    await ctx.send(final)

def get_value(name: str):
    return configs[name].value

def update_bot(bot):
    bot.command_prefix = get_value("prefix")
    pass

def load(bot):
    config_file = open("configs.txt", "r")
    contents = config_file.read()
    config_file.close()
    for line in contents.splitlines():
        name = line.split(":")[0]
        val = line.split(":")[1]
        configs[name].set(val)
    update_bot(bot)

def save():
    config_file = open("configs.txt", "w")
    contents = ""
    for name,config in configs.items():
        contents += f"{name}:{config.value}"
    config_file.write(contents)
    config_file.close()

def set_value(bot, name: str, value):
    configs[name].set(value)
    update_bot(bot)
    save()
