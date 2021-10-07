import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from internet_speed.utils.db_utils import get_data_from_db


def generate_report():
    print("Generating Reports...")
    now = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
    last_week = now - datetime.timedelta(days=7)

    data = get_data_from_db(now, last_week)
    data = pd.DataFrame.from_records(data)

    create_speed_image(data, title=f"Speed Test Analysis for {last_week.day}/{last_week.month}-{now.day}/{now.month}",
                       name="internet_speed/local_data/Speed_Test_Data")

    avr_download = np.average(data["download_speed"])
    avr_upload = np.average(data["upload_speed"])

    return {"avr_download": avr_download, "avr_upload": avr_upload, "las_week": last_week, "now": now}


def create_speed_image(data, title="", name=""):

    plt.figure(figsize=[15, 10])
    plt.plot(data["created_at"], data["download_speed"], "-o", label="Download Speed")
    plt.plot(data["created_at"], data["upload_speed"], "-o", label="Upload Speed")
    plt.plot(data["created_at"], data["ping"], "-o", label="Ping")
    plt.legend()
    plt.title(title)
    plt.savefig(name+".pdf")
