#!/usr/bin/python3
# recommendations.py

import requests
from bs4 import BeautifulSoup


def recommendations(keyword):
    link = "https://www.volusia.org/services/growth-and-resource-management/environmental-management/natural-resources/water-conservation/25-ways-to-save-water.stml"
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")

    tips = soup.find_all(style= "color:#006400;")

    tip_list = []
    for tip in tips:            # creates a list of all the tips extracted from the website
        tip_final = tip.get_text()
        beginning = tip_final.find(".") + 2
        tip_final = tip_final[beginning:]
        tip_list.append(tip_final)

    tip_list[0] = tip_list[0][:-2]  # first tip has a weird tag that must be removed

    toilet = []
    shower = []
    faucet = []
    hose = []

    for element in tip_list:
        if "toilet" in element:
            toilet.append(element)
        elif "shower" in element or "baths" in element:
            shower.append(element)
        elif "faucet" in element or "brushing" in element or "shaving" in element or "drinking" in element or "rinsing" in element:
            faucet.append(element)
        elif "hose" in element or "lawn" in element or "cool" in element or "gutter" in element or "plants" in element or "broom" in element:
            hose.append(element)

    if keyword.lower() == "faucet":
        return faucet
    if keyword.lower() == "toilet":
        return toilet
    if keyword.lower() == "shower":
        return shower
    if keyword.lower() == "hose":
        return hose
    return []
