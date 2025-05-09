import os
import instaloader
from instaloader import Profile
import time
import requests
import sys

# Clear the screen based on the operating system
os.system('cls' if os.name == 'nt' else 'clear')

# Function to print text with a slow typewriter effect
def slow_print(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Function to display the banner with custom text
def banner():
    banner_text = """
\033[32m                   .___                 __                        ____.__ 
                   |   | ____   _______/  |______                |    |__|
                   |   |/    \\ /  ___/\\   __\\__  \\    ______     |    |  |
                   |   |   |  \\\\___ \\  |  |  / __ \\_ /_____/ /\\__|    |  |
                   |___|___|  /____  > |__| (____  /         \\________|__|
                             \\/     \\/            \\/                        

\033[41m  Coded by Krishna Dogra | Credit: Achik-Ahmed | github.com/krishnadogra1 \033[0m
"""
    slow_print(banner_text)  # Display the banner with the typewriter effect

# Function to handle user data saving (for profile picture and text data)
def save_user_data(username, profile_pic_path):
    user_data = {
        'username': username,
        'profile_pic': profile_pic_path
    }
    
    # Save data in a .txt file
    with open("user_data.txt", "a") as file:
        file.write(f"Username: {user_data['username']}\n")
        file.write(f"Profile Picture Path: {user_data['profile_pic']}\n\n")

    print("\033[32mUser data saved successfully!\033[0m")

# Function to simulate some tool functionality
def insta_tool():
    print("\033[34mWelcome to Insta-Ji tool!\033[0m")
    print("\033[33mHere you can manage your Instagram account features.\033[0m")
    print("\033[31mBe sure to use this tool responsibly!\033[0m")
    print("\n")

    # Ask the user for their username and profile picture path
    username = input("Enter your username: ")
    profile_pic_path = input("Enter the path to your profile picture: ")

    # Call the function to save the user data in a text file
    save_user_data(username, profile_pic_path)

    # Provide further instructions or options
    print("\033[32mYou can now use Instagram-like features in this tool.\033[0m")
    print("To follow, unfollow, post pictures, or send messages, use the respective options.")
    print("\nFor more advanced features, explore the premium options.")

# Function to save profile data into a directory
def save_profile_data(username, profile):
    directory = os.path.join("upload", username)
    os.makedirs(directory, exist_ok=True)

    with open(os.path.join(directory, "profile.txt"), "w", encoding="utf-8") as file:
        file.write(f"Username: {profile.username}\n")
        file.write(f"ID: {profile.userid}\n")
        file.write(f"Full Name: {profile.full_name}\n")
        file.write(f"Biography: {profile.biography}\n")
        file.write(f"Business Category: {profile.business_category_name}\n")
        file.write(f"External URL: {profile.external_url}\n")
        file.write(f"Followers: {profile.followers}\n")
        file.write(f"Followees: {profile.followees}\n")
        file.write(f"Is Private: {profile.is_private}\n")
        file.write(f"Is Verified: {profile.is_verified}\n")
        file.write(f"Media Count: {profile.mediacount}\n")
        file.write(f"Profile Pic URL: {profile.profile_pic_url}\n")

# Function to download the profile picture
def download_dp(username, profile):
    directory = os.path.join("upload", username)
    os.makedirs(directory, exist_ok=True)

    try:
        response = requests.get(profile.profile_pic_url)
        with open(os.path.join(directory, "dp.jpg"), "wb") as f:
            f.write(response.content)
    except Exception as e:
        print(f"\033[31mError downloading profile picture:\033[0m {e}")

# Function to fetch and display Instagram profile information
def profile_information(username):
    try:
        print("\n\033[33mFetching Profile Information...\033[0m\n")
        L = instaloader.Instaloader()
        profile = Profile.from_username(L.context, username)

        print("\033[32mUsername\033[0m :", profile.username)
        print("\033[32mID\033[0m :", profile.userid)
        print("\033[32mFull Name\033[0m :", profile.full_name)
        print("\033[32mBiography\033[0m :", profile.biography)
        print("\033[32mBusiness Category\033[0m :", profile.business_category_name)
        print("\033[32mExternal URL\033[0m :", profile.external_url)
        print("\033[32mFollowers\033[0m :", profile.followers)
        print("\033[32mFollowees\033[0m :", profile.followees)
        print("\033[32mIs Private\033[0m :", profile.is_private)
        print("\033[32mIs Verified\033[0m :", profile.is_verified)
        print("\033[32mMedia Count\033[0m :", profile.mediacount)
        print("\033[32mProfile Picture URL\033[0m :", profile.profile_pic_url)

        # Save data and DP
        save_profile_data(username, profile)
        download_dp(username, profile)

        print(f"\n\033[32mSaved profile data and DP in 'upload/{username}/'\033[0m")

    except instaloader.exceptions.ProfileNotExistsException:
        print("\033[31mError: Profile does not exist.\033[0m")
    except Exception as e:
        print("\033[31mUnexpected Error:\033[0m", e)

# Main function that runs the entire tool
def main():
    banner()
    username = input("\033[34mEnter Instagram Username: \033[0m")
    profile_information(username)

if __name__ == "__main__":
    main()
