#!/bin/sh

DOMAIN='auslfe.formonline.tokenaccess'

i18ndude rebuild-pot --pot ${DOMAIN}.pot --create ${DOMAIN} ..
i18ndude sync --pot ${DOMAIN}.pot ./*/LC_MESSAGES/${DOMAIN}.po
