import praw
import pandas as pd
import datetime as dt
import access_api

ACCESS_TOKEN = 'FC0tkuO4MU0Wjg'
ACCESS_TOKEN_SECRET = 'n4II27rRz_M_fqbl242zmcyayvY'



def get_memes():
    reddit = praw.Reddit(client_id=ACCESS_TOKEN, client_secret=ACCESS_TOKEN_SECRET, user_agent='DankMemeBot',
                         username=access_api.USERNAME, password=access_api.PASSWORD)