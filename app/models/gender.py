from enum import Enum

class Gender(str, Enum):
    male= "male"
    female= "female"
    prefer_not_to_say = "prefer_not_to_say"