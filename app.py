import requests


# Some basic style :)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Get the website url
url = input('Enter the url : ')
print('')


# Generating the Path
wp_content_url = url + 'wp-content/'
wp_admin_url = url + 'wp-admin/'
wp_login_url = url + 'wp-login.php/'


#making the request and store the status code
has_wp_content = requests.get(wp_content_url).status_code
has_wp_admin = requests.get(wp_admin_url).status_code
has_wp_login = requests.get(wp_login_url).status_code


is_wordpress_counter = 0


# Conditions
if has_wp_content == 200:
	is_wordpress_counter += 1
	print(bcolors.ENDC + 'wp-content | ' + bcolors.OKGREEN + 'url available')
else:
	print(bcolors.ENDC + 'wp-content | ' + bcolors.FAIL + 'url not available')

if has_wp_admin == 200:
	is_wordpress_counter += 1
	print(bcolors.ENDC + 'wp-admin | ' + bcolors.OKGREEN + 'url available')
else:
	print(bcolors.ENDC + 'wp-admin | ' + bcolors.FAIL + 'url not available')


if has_wp_login == 200:
	is_wordpress_counter += 1
	print(bcolors.ENDC + 'wp-login | ' + bcolors.OKGREEN + 'url available')
else:
	print(bcolors.ENDC + 'wp-login | ' + bcolors.FAIL + 'url not available')

print('')

if is_wordpress_counter == 0:
	print(bcolors.FAIL + 'Is Not a Wordpress website')

elif is_wordpress_counter > 0:
	print(bcolors.OKGREEN + 'Is a Wordpress website!')

print(bcolors.ENDC + '')






