import requests
from bs4 import BeautifulSoup
import time
import sys

#print

print("@Author:Sauravtxt")




# Function to find all links on a webpage
def find_links(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object from the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the <a> tags in the HTML
    link_tags = soup.find_all("a")

    # Create a list to store the links
    links = []

    # Iterate over the <a> tags and get the href attribute
    for link in link_tags:
        href = link.get("href")
        if href:
            links.append(href)

    return links


# Function to get the page title
def get_page_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "Title not found"
    return title


# Function to get all images on a webpage
def get_images(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img")
    images = []
    for img in img_tags:
        src = img.get("src")
        if src:
            images.append(src)
    return images


# Function to search for a specific class in a webpage
def search_class_in_page(url, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all(class_=class_name)
    if elements:
        print(f"Found {len(elements)} elements with class '{class_name}':")
        for element in elements:
            print(element)
    else:
        print(f"No elements found with class '{class_name}'.")


# Function to prompt the user for the project options
def get_project_options():
    print("Select option:")
    print("1. Find all links on a webpage")
    print("2. Get the page title")
    print("3. Get all images on a webpage")
    print("4. Get paragraph text from a webpage")
    print("5. Search for a specific class in a webpage")
    print("6. Quit")

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice
        else:
            print("Invalid choice. Please try again.")


# Function to animate progress
def animate_progress():
    for i in range(101):
        sys.stdout.write('\r')
        sys.stdout.write(f"Progress: {i}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print()


# Main program
while True:
    option = get_project_options()

    if option == "1":
        url = input("Enter the URL of the webpage: ")
        animate_progress()
        links = find_links(url)
        print("Links found on the webpage:")
        for link in links:
            print(link)
        print()

    elif option == "2":
        url = input("Enter the URL of the webpage: ")
        animate_progress()
        title = get_page_title(url)
        print("Page title:", title)
        print()

    elif option == "3":
        url = input("Enter the URL of the webpage: ")
        animate_progress()
        images = get_images(url)
        print("Images found on the webpage:")
        for img in images:
            print(img)
        print()

    elif option == "4":
        url = input("Enter the URL of the webpage: ")
        animate_progress()
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        print("Paragraph text from the webpage:")
        for paragraph in paragraphs:
            print(paragraph.get_text())
        print()

    elif option == "5":
        url = input("Enter the URL of the webpage: ")
        class_name = input("Enter the class name to search for: ")
        animate_progress()
        search_class_in_page(url, class_name)
        print()

    elif option == "6":
        print("Exiting the program...")
        break
