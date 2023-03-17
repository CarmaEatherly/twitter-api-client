MAX_IMAGE_SIZE = 5_242_880  # ~5 MB
MAX_GIF_SIZE = 15_728_640  # ~15 MB
MAX_VIDEO_SIZE = 536_870_912  # ~530 MB
CHUNK_SIZE = 8192

BOLD = '\u001b[1m'
SUCCESS = '\u001b[32m'
WARN = '\u001b[31m'
RESET = '\u001b[0m'

account_settings = {
    "address_book_live_sync_enabled": False,
    "allow_ads_personalization": False,
    "allow_authenticated_periscope_requests": True,
    "allow_dm_groups_from": "following",
    "allow_dms_from": "following",  # all
    "allow_location_history_personalization": False,
    "allow_logged_out_device_personalization": False,
    "allow_media_tagging": "none",  # all, following
    "allow_sharing_data_for_third_party_personalization": False,
    "alt_text_compose_enabled": None,
    "always_use_https": True,
    "autoplay_disabled": False,
    "country_code": "us",
    "discoverable_by_email": False,
    "discoverable_by_mobile_phone": False,
    "display_sensitive_media": True,
    "dm_quality_filter": "enabled",  # disabled
    "dm_receipt_setting": "all_disabled",  # all_enabled
    "geo_enabled": False,
    "include_alt_text_compose": True,
    "include_mention_filter": True,
    "include_nsfw_admin_flag": True,
    "include_nsfw_user_flag": True,
    "include_ranked_timeline": True,
    "language": "en",
    "mention_filter": "unfiltered",
    "nsfw_admin": False,
    "nsfw_user": False,
    "personalized_trends": True,
    "protected": False,
    "ranked_timeline_eligible": None,
    "ranked_timeline_setting": None,
    "require_password_login": False,
    "requires_login_verification": False,
    "settings_metadata": {},
    "sleep_time": {
        "enabled": False,
        "end_time": None,
        "start_time": None
    },
    "translator_type": "none",
    "universal_quality_filtering_enabled": "enabled",
    "use_cookie_personalization": False,
    ## todo: not yet implemented - requires additional steps
    # "allow_contributor_request": "all",
    # "protect_password_reset": False,
}
notification_settings = {
    "cursor": "-1",
    "include_profile_interstitial_type": "1",
    "include_blocking": "1",
    "include_blocked_by": "1",
    "include_followed_by": "1",
    "include_want_retweets": "1",
    "include_mute_edge": "1",
    "include_can_dm": "1",
    "include_can_media_tag": "1",
    "include_ext_has_nft_avatar": "1",
    "include_ext_is_blue_verified": "1",
    "include_ext_verified_type": "1",
    "skip_status": "1",
}

follow_settings = {
    "include_profile_interstitial_type": "1",
    "include_blocking": "1",
    "include_blocked_by": "1",
    "include_followed_by": "1",
    "include_want_retweets": "1",
    "include_mute_edge": "1",
    "include_can_dm": "1",
    "include_can_media_tag": "1",
    "include_ext_has_nft_avatar": "1",
    "include_ext_is_blue_verified": "1",
    "include_ext_verified_type": "1",
    "skip_status": "1",
}

account_search_settings = {
    "optInFiltering": True,  # filter out nsfw content
    "optInBlocking": True,  # filter out blocked accounts
}

profile_settings = {
    "birthdate_day": int,
    "birthdate_month": int,
    "birthdate_year": int,  # 1985
    "birthdate_visibility": str,  # "self",
    "birthdate_year_visibility": str,  # "self",
    "displayNameMaxLength": int,  # "50",
    "url": str,  # "https://example.com",
    "name": str,  # "foo",
    "description": str,  # "bar",
    "location": str,  # "world",
}
