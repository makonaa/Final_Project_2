from string import Template

API_BASE_URL = 'https://qa-desk.education-services.ru/api/'
SIGN_UP_URL = API_BASE_URL + 'signup'
SIGN_IN_URL = API_BASE_URL + 'signin'
CREATE_LISTING_URL = API_BASE_URL + 'create-listing'
UPDATE_LISTING_URL = Template(API_BASE_URL + 'update-offer/$listing_id')
DELETE_LISTING_URL = Template(API_BASE_URL + 'listings/$listing_id')
