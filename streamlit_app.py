import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Web Page Link Finder")

# Input for the URL
url_input = st.text_input("Enter the URL to find links:")

if st.button("Find Links"):
    if url_input:
        try:
            # Send a request to get the HTML content of the web page
            response = requests.get(url_input)
            response.raise_for_status()

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags (links) in the web page
            links = soup.find_all('a')

            # Extract and filter the href attribute (link) from each anchor tag
            urls = []
            for link in links:
                href = link.get('href')
                if href and not href.startswith('#'):  # Filter out internal page anchors
                    if href.startswith('https://'):
                        urls.append(href)

            st.subheader("Links Found:")
            for link in urls:
                st.write(link)

        except requests.exceptions.RequestException as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid URL.")
