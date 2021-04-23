from configparser import ConfigParser
from segno import helpers


try:
    with open('python_QR_generator/conf.ini') as fp:
        config = ConfigParser()
        config.read_file(fp)

        jobtitle = config.get('Personal_Info','title')
        firstname = config.get('Personal_Info','name')
        surname = config.get('Personal_Info','family')
        birthday = config.get('Personal_Info','birthday')

        phonenumber = config.get('Contact_Info','phone')
        email_address = config.get('Contact_Info','email')
        website = config.get('Contact_Info','url')

        eye_color = config.get('Pattern_Features','eye_color')

except Exception as e:
    print('Failed to load config file', repr(e))
    quit()

qr = helpers.make_vcard(title=jobtitle, name='{};{}'.format(surname, firstname), displayname='{} {}'.format(firstname, surname), birthday=birthday, phone=phonenumber, email=email_address, url=website)
qr.save(out='vcard.png', scale=3, finder_dark=eye_color, border=0, dark='black', light=None)