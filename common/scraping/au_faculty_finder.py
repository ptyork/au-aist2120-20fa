# Writing this for you to use as another example.
# This script takes a command line arguent that
# is the partial LAST name of a faculty member.
# It then scrapes:
#   https://www.augusta.edu/faculty/directory/search.php
# to get details.
# 
# Call using an argument. E.g.,
#   python au_faculty_finder.py yo
# Where the "yo" is the part of the last name to find.

import sys
import requests
import bs4

if len(sys.argv) != 2:
    print('USAGE: python au_faculty_finder.py [name]')
    exit()

# Get the faculty name as requested on the command line
fac_name = sys.argv[1].lower()
# Get the first letter of the name since we need it for the URL
fac_letter = fac_name[0]

print('=' * 80)
print(f'FACULTY MATCHING "{fac_name}"')

# Construct the URL that should contain the faculty member
url = f"https://www.augusta.edu/faculty/directory/search.php?alpha={fac_letter}"

# Get the page from the server
resp = requests.get(url)
resp.raise_for_status()

# Create the Soup object
soup = bs4.BeautifulSoup(resp.text, features="html.parser")

# each faculty member looks like this in the HTML
# <div class="collapse-card">
#   <div class="collapse-card__heading">
#     <div class="collapse-card__title">
#       <em class="fa fa-plus fa-fw" aria-hidden="true">&nbsp;</em>
#       <span class="name">York, Paul</span>
#     </div>
#   </div>
#   <div class="collapse-card__body">
#     <div class="row">
#       <div class="col-md-2 text-center">
#         <img class="img-polaroid img-responsive" src="images/faculty/pyork1.jpg" alt="York, Paul">
#       </div>
#       <div class="col-md-6">
#         <p class="admrank">Assistant Professor</p>
#         <span style="display:none;" class="col">School of Computer and Cyber Sciences</span>
#         <span style="display: none;" class="dept"></span>
#         <h3>Academic Appointment(s)</h3>
#         <div class="appts">
#           <div class="profession">
#             <p>School of Computer and Cyber Sciences</p>
#           </div>
#         </div>
#       </div>
#       <div class="col-md-4 cfooter">
#         <p></p>
#         <p>
#           <i class="fa fa-phone fa-fw text-muted" aria-hidden="true"></i> (706) 667-4538
#         </p>
#         <p class="text-muted">
#           <i class="fa fa-map-marker fa-fw" aria-hidden="true"></i> AH E137
#         </p>
#         <p>
#           <a href="view.php?id=pyork1" class="btn btn-primary">Full Profile</a>
#         </p>
#       </div>
#     </div>
#   </div>
# </div>

# So I'll start out by finding each "collapse-card" class using a class
# selector of ".collapse-card"

cards = soup.select('.collapse-card')

# iterate over each one to further filter and find the faculty I want
for card in cards:
    # the name of the faculty memeber is in an element with a class of "name"
    name_elem = card.select_one('.name')

    # some cards don't have names, so gotta make sure it exists...otherwise move
    # to the next one.
    if not name_elem:
        continue
    
    name = name_elem.text

    # if the name doesn't start with the value I want (i.e., fac_name...the
    # value passed in as an argument), skip to the next one
    if not name.lower().startswith(fac_name):
        continue

    print('=' * 80)

    print(f"NAME:           {name}")

    # Each card might have a title...in this case an element with a class of admrank
    rank_elem = card.select_one('.admrank')
    if rank_elem:
        print(f"TITLE:          {rank_elem.text}")

    # "appointments" are the places where the faculty member works. Apparently there
    # can be many. So lets iterate over all of them...in elements with class of profession:
    appt_elems = card.select('.profession')

    if len(appt_elems) > 0:
        print("APPOINTMENT(S):")
        for appt_elem in appt_elems:
            # BUT, each appointment MAY have a second (e.g., departemnt) level
            # Both are stored as paragraphs so get the first paragraph as
            # the school/college/etc. and the second as the department.
            appt = appt_elem.contents[0].text
            print(f"                * {appt}")

            if len(appt_elem) == 2:
                dept = appt_elem.contents[1].text
                print(f"                     {dept}")
    
    # The hard part is that the phone and office locations are AFTER
    # <i> elements, not INSIDE of them. So we use a slightly different
    # strategy here. We'll get the text "next" to the element.

    phone_elem = card.select_one('.fa-phone')
    if phone_elem:
        phone = str(phone_elem.next)
        phone = phone.strip()
        print(f"PHONE:          {phone}")

    office_elem = card.select_one('.fa-map-marker')
    if office_elem:
        office = str(office_elem.next)
        office = office.strip()
        print(f"OFFICE:         {office}")

print('=' * 80)
