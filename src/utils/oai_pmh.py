import requests, datetime, os
from utils.xml import extract_from_xml
from utils.logger import log


def get_records(url, params):
    log(f"GET request to: {url} with {params}")
    try:
        # Send a GET request to the URL
        response = requests.get(url, timeout=60 * 5, params=params)
        # Check if the request was successful otherwise raise an exception
        response.raise_for_status()
        # Set the encoding of the response to utf-8
        response.encoding = 'utf-8'
        # Return the response
        return response.text
    except Exception as e:
        log(f"Error sending request: {e}", "error")


def write_records_to_file(records, directory_path, suffix=""):
    # Save the response to a file named records-<timestamp>-<suffix>.xml
    file_path = os.path.join(
        directory_path,
        f"records-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}-{suffix}.xml"
    )
    # Write the response to a file
    log(f"Writing response to file: {file_path}")
    try:
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(records)
    except Exception as e:
        log(f"Error writing to file: {e}", "error")


def download_oai_pmh_records(url, directory_path):
    # Initialize the suffix for the file name
    suffix = 1
    # Define the parameters for the request
    params = {"verb": "ListRecords", "metadataPrefix": "oai_dc"}
    # Send the first request
    first_page = get_records(url, params)
    write_records_to_file(first_page, directory_path, suffix)
    # Extract the resumption token from the first page
    resumptionToken = extract_from_xml(
        first_page, ".//{http://www.openarchives.org/OAI/2.0/}resumptionToken")
    # If the resumption token is not None, then there are more pages to download
    while resumptionToken is not None:
        # Send the next request with the resumption token
        params = {"verb": "ListRecords", "resumptionToken": resumptionToken}
        next_page = get_records(url, params)
        if next_page:
            # Increment the suffix for the file name
            suffix += 1
            write_records_to_file(next_page, directory_path, suffix)
            # Extract the resumption token from the next page
            resumptionToken = extract_from_xml(
                next_page,
                ".//{http://www.openarchives.org/OAI/2.0/}resumptionToken")
        else:
            resumptionToken = None
