import xml.etree.ElementTree as ET
import datetime
from typing import *


def get_last_update_time() -> datetime.datetime:
    return datetime.datetime.now()


def parse_feed(err: str, msg: str) -> Tuple[object, bool]:
    if err:
        return msg, True
    else:
        root = ET.fromstring(msg)
        channel = root.find("channel")  # First find the <channel> element
        if channel is None:
            return "No <channel> found in RSS feed", True

        result_array = []
        for item in channel.findall("item"):
            cur = {}
            cur["title"] = item.find("title").text
            cur["description"] = item.find("description").text
            cur["link"] = item.find("link").text
            result_array.append(cur)
        return result_array, False
