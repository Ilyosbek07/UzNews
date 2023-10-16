import datetime
import re

from googleapiclient.discovery import build

my_key = "AIzaSyDfSCdDWf4bdx8uxUizIX1juLa1oRJwuSA"


def get_youtube_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    if match:
        return match.group(1)
    else:
        return None


def parse(pt_format):
    days = hours = minutes = seconds = 0
    if "P" in pt_format:
        pt_format = pt_format.split("P")[1]
        if "D" in pt_format:
            days, pt_format = pt_format.split("D")
        if "T" in pt_format:
            pt_format = pt_format.split("T")[1]
        if "H" in pt_format:
            hours, pt_format = pt_format.split("H")
        if "M" in pt_format:
            minutes, pt_format = pt_format.split("M")
        if "S" in pt_format:
            seconds, pt_format = pt_format.split("S")
    return {"days": int(days), "hours": int(hours), "minutes": int(minutes), "seconds": int(seconds)}


def get_duration_from_url(url):
    api_key = my_key
    youtube = build("youtube", "v3", developerKey=api_key)
    video_id = get_youtube_video_id(url)
    response = youtube.videos().list(part="contentDetails", id=video_id).execute()
    if response["items"] != []:
        duration = response["items"][0]["contentDetails"]["duration"]
        return datetime.timedelta(**parse(duration))
