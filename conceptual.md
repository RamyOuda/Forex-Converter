### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  > **Python** is used for _back-end_ development for things like servers and databases.  
  > **JavaScript** is used in _front-end_ development for things like web pages and DOM manipulation.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

  > - dict.get("c") will return None if key is not fount
  > - dict.get("c", "3") will set 3 as the default value to return

- What is a unit test?

  > A **unit test** tests a small part of your code, such as a single line or function.

- What is an integration test?

  > An **integration test** assures that different parts of your code are working together correctly.

- What is the role of web application framework, like Flask?

  > To make the development process easier and faster, while writing less code.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  > A route is fitting when the page is mainly about that topic, whereas a query is more fitting when the perameter is not the main focus of the page.

- How do you collect data from a URL placeholder parameter using Flask?

  > You pass it in as an argument in the view function.  
  > Example:  
  > @app.route("/episode/\<int:number>")  
  > def episode_page(number):

- How do you collect data from the query string using Flask?

  > request.args

- How do you collect data from the body of the request using Flask?

  > request.form

- What is a cookie and what kinds of things are they commonly used for?

  > Cookies are stored in the browser and communicate with a server/database. They are commonly used to keep track of a user's activity on a site, such as how long they've visited, what they've clicked on, etc.

- What is the session object in Flask?

  > Flask sessions are an easy way to handle cookies, and is handled similar to a Python dictionary.

- What does Flask's `jsonify()` do?
  > Converts HTML into JSON.
