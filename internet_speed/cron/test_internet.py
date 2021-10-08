from internet_speed.speed_test.speed_test import get_speed
from internet_speed.utils.db_utils import add_speed_data_to_db


def test_internet():
    print("Testing internet...")
    speed_data = get_speed()
    add_speed_data_to_db(speed_data)



