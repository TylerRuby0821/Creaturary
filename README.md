<h1>Creaturary</h1>

Creaturary is an interactive creature database allowing users to lookup and add any creature they could dream of and allowing 
other users to then access that creatures information.

Check it out here: <a href='https://creaturary.herokuapp.com/'>Creaturary</a>

<h2>Technical Details:</h2>

Creaturary allows users to sign up for an account, and log in to visit the main portion of the website.
Once logged in a user can search in a multitude of ways, allowing them to access the multitude of creatures stored in the database.
If a creature isnt in the database yet or they created it themselves, they can also add that creature and any relevent information into 
the database for storage and access.

<h1>Features - Current State </h1>
<h3>Landing Page</h3>
<p>
  <img src="/referenceimages/landing.PNG" width="500" height="300" />
</p>

<h3>Signup</h3>
  Users can sign up to create an account on the application.
<p>
  <img src="/referenceimages/signup.PNG" width="500" height="300" />
</p>  

<h3>Signup</h3>
  Users who already have an account can log in, or can log in as the Demo user.
<p>
  <img src="/referenceimages/login.PNG" width="500" height="300" />
</p>  

<h3>Main Page</h3>
  Once users have signed up/logged in, they will be redirected to the main page,
  allowing them a multitude of search options, as well as access to the users menu 
  to create a new creature or logout
<p>
  <img src="/referenceimages/main.PNG" width="500" height="300" />
</p> 

<h3>Search</h3>
  Wether a user types into the search field or clicks one of the fast links, it will dispay the results of that search,
  presenting any creature in the database that fitsthe criteria, as well as a brief description. The user can then click on 
  the creatures result to be taken to their individual page.
<p>
  <img src="/referenceimages/results.PNG" width="500" height="300" />
  <img src="/referenceimages/creaturepage" width="500" height="300" />
</p> 

<h3>Create Creature / User Menu</h3>
  If the creature is not currently in the database, the user can access the user-menu to give them the option of
  adding it to the database!
  The user menu also provides access to the logout functionality if a user has finished thier time in the app.
<p>
  <img src="/referenceimages/usersmenu" width="500" height="300" />
  <img src="/referenceimages/newcreature" width="500" height="300" />
</p> 

<h2>To Do:</h2>

- [ ] Better Error Handling when creating a creature fails.
- [ ] User-Favorites to allow users to favorite and view their favorite creatures
- [ ] AWS integration so creatures can have photos uploaded
- [ ] user authorization - Role based for editing/deleting creatures
