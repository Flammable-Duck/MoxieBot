from enum import Enum
from typing import Any

# Python enums kinda dumb ngl.. like why not just be normal and have like
# ```
# enum Whatever:
#     value
#     value
#     UwU
# ```

class ConfigType(Enum):
    BOOL = 0
    STR = 1

class ConfigValue:
    name: str
    desc: str
    value: Any
    config_type: ConfigType

    def __init__(self, name: str, desc: str, default_val):
        self.name = name
        self.desc = desc
        self.value = default_val
        if isinstance(default_val, bool):
            self.config_type = ConfigType.BOOL
        elif isinstance(default_val, str):
            self.config_type = ConfigType.STR

    def set(self, val) -> bool:
        if isinstance(val, bool) and self.config_type == ConfigType.BOOL:
            self.value = val
        elif isinstance(val, str) and self.config_type == ConfigType.STR:
            self.value = val
        else:
            return False
        return True

configs = []

# Add configs here for later reference or something idk
def init():
    configs.append(ConfigValue("Test", "A test value", False))
    configs.append(ConfigValue("UwU", "OwO", "monke"))

async def list_configs(ctx):
    final = ""
    for config in configs:
        final += f"{config.name}: {config.desc}\n"
        final += f"\tValue: {config.value}\n"
    await ctx.send(final)

async def set_value(ctx, name: str, value):
    # Is there index method..?
    for config in configs:
        if config.name == name:
            if config.set(value):
                await ctx.send(f"Changed {name} to {value}!")
            else:
                await ctx.send("Failed to change config!")
