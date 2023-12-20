|ID|Area Tested|Sub-area|Description|Test Performed|Result|Mark|Re-Test|Corrective action|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|1|Navbar|Navbar|Page load with all elements properly displayed in desktop|Load all pages in the project in desktop|Navbar remains in it`s intended shape and form|Pass|No| |
|2|Navbar|Navbar|Page load with all elements properly displayed in mobile|Load all pages in the project in mobile|Navbar remains in it`s intended shape and form|Pass|No| |
|3|Navbar|Logo|Logo displayed correctly|Load page in desktop and various mobile screen sizes|Logo is displayed visible and clear, in correct position|Pass|No| |
|4|Navbar|Logo|Links redirect to all relavant pages and subsections|Click on logo|User is redirected to index page|Pass|No| |
|5|Navbar|Account|Account section displayed correctly|Load page in desktop and various mobile screen sizes|Account section is displayed visible and clear|Pass|No| |
|6|Navbar|Account|Account section displayed correctly|Section displayes logged in user name visible and clear whenever user is logged in|On login username is displayed visible and clear and on logout it dissapears. Issue with background not showing the same uniform color code as the overall header|Faill| | |
|7|Navbar|Account|Account section displayed correctly - Re-Test|Section displayes logged in user name visible and clear whenever user is logged in|On login username is displayed visible and clear and on logout it dissapears. Color discrepancy gone|Pass|Yes|Corrected CSS to dissplay same background color as the header when user is logged in, surrounding the user name.|
|8|Navbar|Account|Links redirect to all relavant pages and subsections|Click on icon and drop down arow on account section.|User logged out: expands section with Login and Register visible|Pass|No| |
|9|Navbar|Account|Links redirect to all relavant pages and subsections|Click on icon and drop down arow on account section.|User logged in: expands section with Profile and Logout section visible|Pass|No| |
|10|Navbar|Account|Links redirect to all relavant pages and subsections|Click on icon and drop down arow on account section.|Admin logged in: expands section with Profile and Logout section visible|Pass|No| |
|11|Navbar|Account|Links redirect to all relavant pages and subsections|Click on Login|Opens the Login Modal|Pass|No| |
|12|Navbar|Account|Links redirect to all relavant pages and subsections|Click on Logout|Logs user out|Pass|No| |
|13|Navbar|Account|Links redirect to all relavant pages and subsections|Click on Profile|Redirects user to their profile page|Pass|No| |
|14|Navbar|Account|Links redirect to all relavant pages and subsections|Click on Admin Panel|Takes admin to the admin page|Pass|No| |
|15|Navbar|Menu|Menu displayed correctly|Load page in desktop and various mobile screen sizes|Menu is displayed visible and clear in correct position.|Pass|No| |
|16|Navbar|Menu|Menu displayed correctly|Expands correctly with all elements visible.|Click Menu and Menu Toggle icon to display menu elements|Pass|No| |
|17|Navbar|Menu|Menu displayed correctly|Contracts correcly with all elements vsible|Click on expanded Menu and Menu Toggle icon to hide elements|Pass|No| |
|18|Navbar|Menu|Menu links redirect to all relavant pages|Click on "About me section"|Redirect to about-me.html|Pass|No| |
|19|Navbar|Menu|Menu links redirect to all relavant pages|Click on "What are essential oils"|Redirect to about-oils.html|Pass|No| |
|20|Navbar|Menu|Menu links redirect to all relavant pages|Click on "What is the best Essential Oil for me"|Redirect to recommended.html|Pass|No| |
|21|Navbar|Menu|Menu links redirect to all relavant pages|Click on "Promotions"|Redirect to promotions.html|Pass|No| |
|22|Navbar|Menu|Menu links redirect to all relavant pages|Cllick on "Contact"|Redirect to contact.html|Pass|No| |
|23|Modal-login|Modal-login|Modal displayed correctly|Click on Login in Account section to open Modal|Opens Modal and all information is visible and displyed as intended in both mobile and desktop|Pass|No| |
|24|Modal-login|Modal-login|Input sections can receive data|Click in each input section and add different data formats|Input fields accept data and store it.|Pass|No| |
|25|Modal-login|Modal-login|Buttons and links redirect to relevant sections|Click on Login button|If data is correct refreshes page and connects it to the registered users account|Pass|No| |
|26|Modal-login|Modal-login|Buttons and links redirect to relevant sections|Click on Login button|If data is not correct, takes the user to an allauth page with an error stating data is incorect where user can try again/recover password or sign-up.|Pass|No| |
|27|Modal-login|Modal-login|Buttons and links redirect to relevant sections|Click on Register button|Takes the user to the register.html page|Pass|No| |
|28|Modal-login|Modal-login|Buttons and links redirect to relevant sections|Click Forgot Password link|Takes the user to the recover password standard allauth form.|Pass|No| |
|29|Allauth form|Forgot Password|Page displays correctly|Open page in various screen sizes mobile/desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|30|Allauth form|Forgot Password|Form accepts user email input and validates entered data|Click in input and add correct and incorrect email format|If incorrect email format user is prompted that the data is incorrect and if data is correct, the input section accepts it.|Pass| | |
|31|Allauth form|Forgot Password|Reset button redirects user to reset confirmation page.|Click on reset my password button|User is taken to the page which confirms reset success(email sent to user to reset).|Pass| | |
|32|Allauth form|Forgot Password|Reset button triggers message of reset to be printed in django terminal as website is set not to send to an email address the reset link, but print it in the django terminal.|Click on reset my password button|Terminal prints relevant message|Pass| | |
|33|Allauth form|Wrong username and password|Page displays correctly|After triggering from modal wrong credentials, open wrong password page in various screen sizes mobile/desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|34|Allauth form|Wrong username and password|Form accepts all types of user data input|Click in input filed and add various styled of data|Input accepts and stores data|Pass| | |
|35|Allauth form|Wrong username and password|Reset page is retriggered if user data is not correct|Simulate wrong username or password|Page reloads with the error message stating the user or password are wrong|Pass| | |
|36|Allauth form|Wrong username and password|Normal result is obtained if user data is correct|Add correct user input data|Homepage reloads with logged in user|Pass| | |
|37|Allauth form|Wrong username and password|Sign Up redirects to register.html|Click on sign up|User redirected to register.html page|Pass| | |
|38|Allauth form|Wrong username and password|Forgot Password redirects to password recovery page|Click on Forgott password|User is redirected to the allauth customized recovery password page.|Pass| | |
|39|Allauth form|Change password form|Form accepts all types of user data input|Click in input filed and add various styled of data|Input accepts and stores data|Pass| | |
|40|Allauth form|Change password form|Page displays correctly|Open page in various screen sizes mobile/desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|41|Allauth form|Change password form|Page gives user info on accepted data and does not move beyond this if current password is wrong.|Type various scenarios including wrong data|Page will not confirm data change unless the data is adequate, but does not prompt the user if he uses the wrong data for current password. As well, there isn`t a confirmation message of successful change.|Partial Pass| | |
|42|Floating Wsapp element|Floating Wsapp element|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|43|Floating Wsapp element|Floating Wsapp element|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|44|Floating Wsapp element|Floating Wsapp element|Redirect to relevant link|Click on wsapp icon|Opens wsapp app/link|Pass| | |
|45|Footer|Footer|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|46|Footer|Footer|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|47|Footer|Join My Team|Redirect to relevant link |Click on Join Team Link|Opens the contact.html page|Pass| | |
|48|Footer|GDPR|Redirect to relevant link |Click on GDPR link|Loads data-protection.html page|Pass| | |
|49|Footer|Social Links|Redirect to relevant link |Click on each social link|Loads Each social link in a separate tab|Pass| | |
|50|Homepage|Homepage|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|51|Homepage|Homepage|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|52|Homepage|Homepage|Page load with all elements properly|Load page with user logged out and logged in|Logged out, the section redirecting user to login modal. Logged in, button displays Use our tool redirected them to the recommended tool page.|Pass| | |
|53|Homepage|Homepage|Redirect to relevant link |Click on Register/Login link in section redirecting to recommended.html page.|Redirects user to login modal.|Pass| | |
|54|Homepage|Homepage|Redirect to relevant link |Click on I want to join team|Redirects user to contact.html page|Pass| | |
|55|Homepage|Homepage|Redirect to relevant link |Click on Learn More in Promotions section|Redirects user to promotions.html page|Pass| | |
|56|Homepage|Homepage|Redirect to relevant link |Click on Learn more in hero section |Redirects user to about-oils.html page|Pass| | |
|57|About Me|About Me|Page loads with all elements properly displayed in desktop|Load website page in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|58|About Me|About Me|Page loads with all elements properly displayed in mobile|Load website page in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|59|What are essential oils|What are essential oils|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|60|What are essential oils|What are essential oils|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|61|What is the best Essential Oil for me|What is the best Essential Oil for me|Trying to access the page without being logged in|Click on the What is the best Essential Oil for me link from both homepage and navbar.|Page displayed requests user to register or login(clicking on the 2 buttons will either display the login modal or the register.html page.|pass| | |
|62|What is the best Essential Oil for me -Admin view|What is the best Essential Oil for me|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|63|What is the best Essential Oil for me -Admin view|What is the best Essential Oil for me|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|64|What is the best Essential Oil for me -Admin view|What is the best Essential Oil for me|Quick access menu is displayed allowing the admin to access the relevant product to edit.|Load page in both mobile and desktop|Quick access area is present on top of the page.|Pass| | |
|65|What is the best Essential Oil for me -Admin view|Filter section|Clear filter selection - Re-Test|Click on Clear all|Filters are removed and all products are displayed| | | |
|66|What is the best Essential Oil for me -Admin view|Description input section|Input field can take various type of data|Click in input area and type data and add various type of data|Alert comes up on the screen asking if you are sure that you want to update the data which shouldn`t happen.|Faill| |Changed onclick event listener to onsubmit.|
|67|What is the best Essential Oil for me -Admin view|Description input section|Input field can take various type of data Re-Test|Click in input area and type data and add various type of data|Field allows user to input various types of data|Pass| | |
|68|What is the best Essential Oil for me -Admin view|Save description button|Button to save changes made to description|Click button|Message prompts the admin x 2 to confirm description change and upon confirmation, description updates. Should prompt only once.|Faill| | |
|69|What is the best Essential Oil for me -Admin view|Save description button|Button to save changes made to description|Click button|Message prompts the admin to confirm description change and upon confirmation, description updates in products list and in the database. |Pass| | |
|70|What is the best Essential Oil for me -Admin view|Delete product button|Button to delete product|Click button|Message prompts the admin to confirm product deletion, and once confirmed, it deletes from the products screen and from the database|Pass| | |
|71|What is the best Essential Oil for me -Admin view|Add to favorites button|Mark a product as favorite|Click button|Marks the product as favorite but then refreshes and removes it.|Faill| |Added condition to check if user is admin and don`t display in this scenario the toggle button.|
|72|What is the best Essential Oil for me -Admin view|Add to favorites button|Mark a product as favorite - Re-Test|Reload page|Don`t display for admin|Pass| | |
|73|What is the best Essential Oil for me -Admin view|Add to favorites button|Remove product as a favorite|Click button|Marks the product as favorite but then refreshes and removes it.|Faill| |Added condition to check if user is admin and don`t display in this scenario the toggle button.|
|74|What is the best Essential Oil for me -Admin view|Add to favorites button|Remove product as a favorite - Re-Test|Click button|Don`t display for admin|Pass| | |
|75|What is the best Essential Oil for me -User view|Contact section links|Redirect to relevant link |Click on each social link|Loads Each social link in a separate tab|Pass| | |
|76|What is the best Essential Oil for me -Admin view|Add Product button|Add a new product straight from the recommended page|Click button|Opens the modal to add a new product|Pass| | |
|77|What is the best Essential Oil for me -Admin view|Add Product modal|Display modal in mobile and desktop|Open page in various screen sizes mobile/desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|78|What is the best Essential Oil for me -Admin view|Add Product modal|Input fields take various type of data|Click inside the input area and try various type of data|Modal will take all forms of data.|Pass| | |
|79|What is the best Essential Oil for me -Admin view|Add Product modal|If mandatory fields are not selected, data can`t be saved|Leave a mandatory field without data and click on save|Admin is asked to confirm the save and then prompted on mandatory data.|Pass| | |
|80|What is the best Essential Oil for me -Admin view|Add Product modal|Checkbox can be selected multiple at the same time|Select multiple checkboxes|Multiple checkboxes can be selected at the same time|Pass| | |
|81|What is the best Essential Oil for me -Admin view|Add Product modal|Save product will save the created product with all relevant details in the page|Fill in all data and click on Save Product|Alert comes up to confirm creation and then product is populated in the product list page.|Pass| | |
|82|What is the best Essential Oil for me -Admin view|Add Product modal|Clear form will clear all data inputed in the form.|Fill in all data and click on Clear form|Alert comes up to confirm clearing the form, and after confirmation clears the form data.|Pass| | |
|83|What is the best Essential Oil for me -User view|Non Approved user|Trying to access the tool without being approved by the admin|Click on the What is the best Essential Oil for me link from both homepage and navbar.|User receives notification they are not approved and need to wait approval to use it|Pass| | |
|84|What is the best Essential Oil for me -User view|Approved user|Trying to access the tool approved by the admin|Click on the What is the best Essential Oil for me link from both homepage and navbar.|User can access and use the tool as normal.|Pass| | |
|85|What is the best Essential Oil for me -User view|Approved user|Add to favorites|Click the button add to favorites|Favorites button changes to remove from favorites and remains checked. Product is populated in favorites section in profile.|Pass| | |
|86|What is the best Essential Oil for me -User view|Approved user|Remove from favorites|Click the button remove from favorites|Favorites button changes to add to favorites. Product is removed from favorites section in profile.|Pass| | |
|87|What is the best Essential Oil for me -User view|What is the best Essential Oil for me|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|88|What is the best Essential Oil for me -User view|What is the best Essential Oil for me|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|89|What is the best Essential Oil for me  -User view|What is the best Essential Oil for me|Filter section expanded in desktop and mobile|Load page in both mobile and desktop|Filter section is expanded.|Pass| | |
|90|What is the best Essential Oil for me  -User view|Search Ailment section|User can search for an ailment from the list|Type existent and non existent ailment name|As you start typing the filter section starts filtering through the ailments displaying only the ones containing the letters or combination of letters|Pass| | |
|91|What is the best Essential Oil for me  -User view|Filter section|User can select multiple filters|Click on single or multiple check boxes|Boxes can be clicked and multiple selected into one session|Pass| | |
|92|What is the best Essential Oil for me  -User view|Filter section|Apply filter selection - Re-Test|Click on Apply selection|Only products containing at least one of the selected ailments is displayed|Pass| | |
|93|What is the best Essential Oil for me  -User view|Filter section|Clear filter selection - Re-Test|Click on Clear all|Filters are removed and all products are displayed|Pass| | |
|94|What is the best Essential Oil for me -Admin view|Add to favorites button|Mark a product as favorite|Click button|Marks the product as favorite but then refreshes and removes it.|Pass| | |
|95|User Profile page|User Profile page|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|96|User Profile page|User Profile page|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|97|User Profile page|Change password form|User is able to access the change password form using the link profile.html|Click on link to change password|User is directed to change password allauth form|Pass| | |
|98|User Profile page|Update user details|User can change the content of their profile details|Change input data.|User data is changed|Pass| | |
|99|User Profile page|Save changes|Click on save changes will update the data in the users profile page|Change name and click on save changes|User is prompted to confirm the change. Once confirmed, page updates with the new user details.|Pass| | |
|100|User Profile page|Delete account|Clicking on delete account will remove users access privilages|While logged in, click on Delete account|User is prompted on the action of deletion and to confirm it, but the actual delete doesn`t happen, just a refresh is done on the page.|Faill| |Separated forms for delete and save changes and update delete_account view to add a logout action when delete is triggered.|
|101|User Profile page|Delete account|Clicking on delete account will remove users access privilages - Re-Test|While logged in, click on Delete account|User is prompted on the action of deletion, account is deleted and user redirected to homepage.|Pass| | |
|102|User Profile page|Favorites section|Clicking on remove from favorites removes the product from Favorite products section|Select a product to add to favorites, go to profile and click on remove favorites|Product is removed from favorites section in profile.|Pass| | |
|103|Promotions-Admin view|Promotions|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|104|Promotions-Admin view|Promotions|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|105|Promotions-Admin view|Save description button|Button to save changes made to description|Click button|Message prompts the admin to confirm description change and upon confirmation, description updates in promotions list and in the database. |Pass| | |
|106|Promotions-Admin view|Delete product button|Button to delete promotion|Click button|Message prompts the admin to confirm promotion deletion, and once confirmed, it deletes it from the promotion screen and from the database|Pass| | |
|107|Promotions-Admin view|Description input section|Input field can take various type of data|Click in input area and type data and add various type of data|Alert comes up on the screen asking if you are sure that you want to update the data which shouldn`t happen.|Faill| |Changed onclick event listener to onsubmit.|
|108|Promotions-Admin view|Description input section|Input field can take various type of data Re-Test|Click in input area and type data and add various type of data|Field allows user to input various types of data|Pass| | |
|109|Promotions-User view|Contact section links|Redirect to relevant link |Click on each social link|Loads Each social link in a separate tab|Pass| | |
|110|Promotions-User view|Promotions|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|111|Promotions-User view|Promotions|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|112|Contact page|Contact page|Page load with all elements properly displayed in desktop|Load website pages in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|113|Contact page|Contact page|Page load with all elements properly displayed in mobile|Load website pages in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|114|Contact page|Contact section links|Redirect to relevant link |Click on each social link|Loads Each social link in a separate tab|Pass| | |
|115|403 page|403 page|Page load with all elements properly displayed in desktop|Simulate error in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|116|403 page|403 page|Page load with all elements properly displayed in mobile|Simulate error in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|117|404 page|404 page|Page load with all elements properly displayed in desktop|Simulate error in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|118|404 page|404 page|Page load with all elements properly displayed in mobile|Simulate error in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|119|500 page|500 page|Page load with all elements properly displayed in desktop|Simulate error in desktop|Page displays as intended with clear and unaltered data.|Pass| | |
|120|500 page|500 page|Page load with all elements properly displayed in mobile|Simulate error in mobile|Page displays as intended with clear and unaltered data.|Pass| | |
|121|Admin section|Admin section|Displayed user details are visible for logged in users.|Created a user and accessed it from backend.|User details are rendered correctly.|Pass| | |
|122|Admin section|Admin section|Change user by admin in backend results in change in front end.|Changed last name resulting in a change also to the user view in front end.|User details are rendered correctly.|Pass| | |
|123|Admin section|Admin section|Admin can delete a user|Tried to delete a user|Admin is prompted that it has no acess.|Faill| |Add admin rights to be able to delete from user|
|124|Admin section|Admin section|Admin can delete a user|Tried to delete a user|Admin can delete users from admin section and automatically removes them also from AppUser.|Pass|Yes| |
|125|Admin section|Add Products Section|Display products|Access a product from backend.|Details displayed correctly.|Pass| | |
|126|Admin section|Add Products Section|Change products|Change product description from backend|New details display correctly in front end.|Pass| | |
|127|Admin section|Add Products Section|Delete products|Delete a product from backend.|Product deleted has been removed from product list.|Pass| | |
|128|Admin section|Add Products Section|Add a product.|Add product using the add backend functionality.|Product is added to front with no issues.|Pass| | |
|129|Admin section|Add Products Section|Import/Export products|Export file, add a product and import again.|Product was added to the database and front-end|Pass| | |
|130|Admin section|Add Promotions|Display promotions|Acces a promotion from backend.|Promotion content is displayed correctly.|Pass| | |
|131|Admin section|Add Promotions|Change promotions|Change promotion details from backend|Changing promotion details in backend results in a change also on front.|Pass| | |
|132|Admin section|Add Promotions|Delete promotions|Deleting a promotion in backend.|Promotion deleted also front-end.|Pass| | |
|133|Admin section|Add Promotions|Add promotions|Add a promotion in backend.|Promotion is also added to front-end.|Pass| | |
|134|Admin section|Add Promotions|Import/Export promotions|Export file, add a promotion and import again.|Promotion was added to the database and front-end|Pass| | |
|135|Admin section|Ailments|Display ailment|Access an ailment in admin panel.|Ailment details are displayed correctly.|Pass| | |
|136|Admin section|Ailments|Change ailment|In admin section change an ailment name|Ailment name is changed backend, also front end, and in the description of the product.|Pass| | |
|137|Admin section|Ailments|Add ailment|Adding an ailment and allocating it/not allocating it to a product|If allocated to a product it displays front end in the ailment list, if not allocated it displays only backend.|Pass| | |
|138|Admin section|Ailments|Delete ailment|Delete an ailment.|Ailment is no longer present in the database, front end, or in the product description.|Pass| | |
|139|Admin section|Ailments|Import/Export ailment|Export import/export file, add an ailment and import again.|Ailment is added to the database.|Pass| | |
|140|Admin section|App users|Approve App Users|Create a new user and approve backend|User is created with approval status not confirmed. Once approved by admin, user can access the tool in recommended.html section.|Pass| | |
|141|Admin section|Favourite selections|View user favourites|Access favorite section in admin, with posibility to remove them(not a functionality to be used now).|See users favorite: active, history.|Pass| | |
