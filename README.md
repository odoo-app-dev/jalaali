# jalaali
This addon module will help you to show odoo 15 date fields in jalaali format.

Thanks Mr. Mohammadi (https://github.com/parodoo/parOdoo) for his hard work to prepare javascript files.

This version of jalaali works on odoo 15 community edition. It shows most date fields in jalaali format. 

Note: All dates are store in gregorian format in database. If your users preference language is English, all the dates are in gregorian too.

Note: To show jalaali dates, you need to change Persian as preference language.

# Installation:
## 1- On odoo linux server:
1.0. Make sure you installed npm and actvated rtlcss. If not, your odoo web will not work correctly while your user's prefrences language is Persian. So you need to run the folowing commands first.

      #sudo apt-get install npm
      
      #sudo npm install -g rtlcss
      
https://www.odoo.com/documentation/15.0/administration/install/install.html#id10
      
      
1.1. :/#cd /usr/lib/python3/dist-packages/odoo/custom/addons/
      
1.2. :/usr/lib/python3/dist-packages/odoo/custom/addons#git clone https://github.com/odoo-app-dev/jalaali.git

    Note: You might also need to install jdatetime </br>
      #pip install jdatetime</br>
      (https://pypi.org/project/jdatetime/)
  
1.3. edit /etc/odoo/odoo.conf file and add your custom file on 

      Original odoo.conf file:
      [options]
      addons_path = /usr/lib/python3/dist-packages/odoo/addons

      Edited odoo.conf file:
      [options]
      addons_path = /usr/lib/python3/dist-packages/odoo/addons , /usr/lib/python3/dist-packages/odoo/custom/addons

1.4. #systemctl restart odoo

## 2- On odoo web application

  2.1. settings > Activate the developer mode (with assets)

  2.2. apps > update apps list

  2.3. apps > (search for jalaali) > install

  2.4. settings > users > (select your user) > Preferences > Languages > (select Persian)


#

 Feel free to send me email on homayounfar@msn.com if you have any question. 


