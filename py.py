# ********** 👇 Remove https or http from url python 👇 ********** #




# -- 👇 Remove HTTPS Using replace()  👇 -- #

url = "https://pytutorial.com" # 👉️ URL

new_url = url.replace("https://", "") # 👉️ Remove "https" from URL

print(new_url) # 👉️ Print

# 👆 Output: pytutorial.com





# -- 👇 Remove HTTP Using replace()  👇 -- #

url = "http://pytutorial.com" # 👉️ URL

new_url = url.replace("http://", "") # 👉️ Remove "http" from URL

print(new_url) # 👉️ Print

# 👆 Output: pytutorial.com





# -- 👇 Remove HTTPS and HTTP Using replace() 👇 -- #

url = "https://pytutorial.com" # 👉️ URL

new_url = url.replace("https://", "").replace("http://", "") # 👉️ Remove "HTTPS" and "HTTP" from URL

print(new_url) # 👉️ Print

# 👆 Output: pytutorial.com





# -- 👇 Remove HTTPS and HTTP and WWW Using replace() 👇 -- #

url = "https://www.pytutorial.com" # 👉️ URL

new_url = url.replace("https://", "").replace("http://", "").replace("www.", "") # 👉️ Remove "HTTPS" and "HTTP" and "WWW"

print(new_url) # 👉️ Print

# 👆 Output: pytutorial.com





# -- 👇 Remove HTTPS and HTTP Using re.sub() 👇 -- #


import re # 👉️ Import re module

url = "https://www.pytutorial.com" # 👉️ URL

pattern = "https?://" # 👉️ pattern

new_url = re.sub(pattern, "", url) # 👉️ Remove HTTPS and HTTP from URL
 
print(new_url) # 👉️ Print

# 👆 Output: www.pytutorial.com





# -- 👇 Remove HTTPS and HTTP and WWW Using re.sub() 👇 -- #

import re # 👉️ Import re module

url = "https://www.pytutorial.com" # 👉️ URL

pattern = "https?://www.?" # 👉️ pattern

new_url = re.sub("https?://www.?", "", url) # 👉️ Remove HTTPS and HTTP and WWW from URL
 
print(new_url) # 👉️ Print

# 👆 Output: pytutorial.com

