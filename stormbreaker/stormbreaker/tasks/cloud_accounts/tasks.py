"""Cloud Accounts Task Code."""

import logging
from urllib.parse import urljoin

import pymongo
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from stormbreaker.celery import app
from stormbreaker.config import (
    CISCO_AMP_CONSOLE_URL, SELENIUM_COMMAND_EXECUTOR_URL,
)
from stormbreaker.mongo import db


logger = logging.getLogger(__name__)


# Cloud Account Cleaning Functions
def clean_amp_account(login, password):
    logger.info("Beginning cleanup of AMP login `{}`".format(login))

    success = False

    wd = webdriver.Remote(
        command_executor=SELENIUM_COMMAND_EXECUTOR_URL,
        desired_capabilities=DesiredCapabilities.CHROME)

    try:
        wd.get(CISCO_AMP_CONSOLE_URL)
        wd.find_element_by_id("user_email").click()
        wd.find_element_by_id("user_email").clear()
        wd.find_element_by_id("user_email").send_keys(login)
        wd.find_element_by_id("user_password").click()
        wd.find_element_by_id("user_password").clear()
        wd.find_element_by_id("user_password").send_keys(password)
        wd.find_element_by_name("button").click()
        wd.find_element_by_xpath(
            "//li[@class='management']//button[normalize-space("
            ".)='Management']").click()
        wd.find_element_by_link_text("Computers").click()

        try:
            wd.find_element_by_xpath(
                "//span[@id='selected-row-actions']/button[1]").click()
            wd.find_element_by_xpath(
                "//span[@id='selected-row-actions']/button[3]").click()
            wd.find_element_by_xpath(
                "//form[@id='delete-selected-form']//button["
                ".='Delete']").click()
        except:
            pass

        if "No computers" in wd.find_element_by_tag_name("html").text:
            logger.info(
                "No computers present in `{}` AMP account".format(login)
            )
            success = True

        else:
            logger.info(
                "Removing computers from `{}` AMP account".format(login)
            )
            # TODO: Add code to delete computers from AMP

        wd.get(urljoin(CISCO_AMP_CONSOLE_URL, "/logout"))

    finally:
        wd.quit()
        if success:
            logger.info(
                "Cleanup of `{}` AMP account was successful".format(login)
            )
        else:
            logger.warning(
                "Cleanup of `{}` AMP account failed".format(login)
            )
        return success


@app.task()
def clean_cloud_account(login):
    # Set status to `cleaning` and get Cloud Account details
    cloud_account = db.cloud_accounts.find_one_and_update(
        {"login": login},
        {"$set": {"status": "cleaning"}},
        projection={'_id': False},
        return_document=pymongo.ReturnDocument.AFTER,
    )

    password = cloud_account["password"]

    # Cleanup cloud accounts
    cleanup_successful = {
        "AMP": clean_amp_account(login, password)
    }

    if all(cleanup_successful.values()):
        logger.info(
            "Cleanup of cloud account `{}` was successful".format(login)
        )
        # Set status to `available`
        cloud_account = db.cloud_accounts.find_one_and_update(
            {"login": login},
            {"$set": {"status": "available"}},
            projection={'_id': False},
            return_document=pymongo.ReturnDocument.AFTER,
        )
    else:
        # Set status to `cleanup-failed`
        cloud_account = db.cloud_accounts.find_one_and_update(
            {"login": login},
            {"$set": {"status": "cleanup-failed"}},
            projection={'_id': False},
            return_document=pymongo.ReturnDocument.AFTER,
        )

    return cloud_account
