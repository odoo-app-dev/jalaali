# jalaali (beta)
This addon module will help you to show odoo 16 date fields in jalaali format.

Thanks Mr. Mohammadi (https://github.com/parodoo/parOdoo) for his hard work to prepare javascript files.

This version of jalaali works on odoo 15 community edition. It shows most date fields in jalaali format. 

Note: All dates are store in gregorian format in database. If your users preference language is English, all the dates are in gregorian too.

Note: To show jalaali dates, you need to change Persian as preference language.

# Installation:
## 1- On odoo linux server:
1.0. Make sure you installed npm and actvated rtlcss. If not, your odoo web will not work correctly while your user's prefrences language is Persian. So you need to run the folowing commands first.

      sudo apt-get install npm
      
      sudo npm install -g rtlcss
      
      npm install jalali-moment -S
      
      pip install jdatetime
      
https://www.odoo.com/documentation/15.0/administration/install/install.html#id10
      
      
1.1. Go to custom folder of your odoo server

      cd /usr/lib/python3/dist-packages/odoo/custom/addons/
      
1.2. Run git clone to recive a copy of jalaali filels on your server

      git clone https://github.com/odoo-app-dev/jalaali.git
      
1.3. Edit the odoo.conf file on the /etc/odoo/odoo.conf path and then add your custom file on 
      
      vi /etc/odoo/odoo.conf
      (hit i or insert key to start edit)
            Original odoo.conf file:
            [options]
            addons_path = /usr/lib/python3/dist-packages/odoo/addons

      Edited odoo.conf file:
      [options]
            addons_path = /usr/lib/python3/dist-packages/odoo/addons , /usr/lib/python3/dist-packages/odoo/custom/addons
      
      (when finished the editing, firest hit ESC, then enter semicolon, ":", and after that enter "wq" and finaly hit Enter key)
      
1.4. After all changes, the odoo service must be restarted
      
      systemctl restart odoo

## 2- On odoo web application

  2.1. settings > Activate the developer mode (with assets)

  2.2. apps > update apps list

  2.3. apps > (search for jalaali) > install

  2.4. settings > users > (select your user) > Preferences > Languages > (select Persian)


#

 Feel free to send me email on homayounfar@msn.com if you have any question. 


