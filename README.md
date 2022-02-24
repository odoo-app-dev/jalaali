# jalaali
This addon module will help you to show odoo 15 date fields in jalaali format.

Thanks Mr. Mohammadi (https://github.com/parodoo/parOdoo) for his hard work to prepare javascript files.

This version of jalaali works on odoo 15 community edition. It shows most date fields in jalaali format. 

<strong>Note: </strong> All dates are store in gregorian format in database. If your users preference language is English, all the dates are in gregorian too.

<strong>Note: </strong> To show jalaali dates, you need to change Persian as preference language.

# Installation:
## 1- On odoo linux server:
:/#cd /usr/lib/python3/dist-packages/odoo/custom/addons/

:/usr/lib/python3/dist-packages/odoo/custom/addons#git clone https://github.com/odoo-app-dev/jalaali.git

<strong>Note: </strong> You might also need to install jdatetime </br>
  #pip install jdatetime</br>
  (https://pypi.org/project/jdatetime/)

## 2- On odoo web application

settings > Activate the developer mode (with assets)

apps > update apps list

apps > (search for jalaali) > install

settings > users > (select your user) > Preferences > Languages > (select Persian)


#

<strong> Fell free to send me email on homayounfar@msn.com if you have any question.  </strong>


