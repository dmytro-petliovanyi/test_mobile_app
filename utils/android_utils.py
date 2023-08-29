from typing import Any

from utils.dynamic_udid import get_phone_udid


def android_get_desired_capabilities() -> dict[str, Any]:
    udid = get_phone_udid()
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '12',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': udid,
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
