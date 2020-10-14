# A guide to the front-end developers 
"This guide mainly includes what is an API and how a front-end developer or a user can use it."

## What is an API?
API is the acronym for **Application Programming** Interface, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook and send an instant message, or check the weather on your phone, you're using an API.

## Why to use an API?
Computers make a lot of things easier, especially tasks that involve collecting and sorting through tons of data.
Benifits of using a web API is they are built around the HTTP protocol, nearly any programming language can be used to access them. Python, R, Java, JavaScript, Ruby, and every other general purpose programming language has at least one HTTP library to make this process easier. However, more specialist languages like SQL do not have HTTP libraries.

## What is an API key?

Some APIs are open to all. When you find an API as shown below, you can just take an API URL, add some parameters, put it into your browser, and youâ€™ll get back a useful response. An example of this is the old Twitter API. You can just put a URL into your browser and get results:
```
https://search.twitter.com/search.json?q=burritos
```

But most of the APIs are not quite that freewheeling. Instead, most of them require some sort of authentication. In the form of an API key, a long string of letters and numbers that functions like a password. But inorder to use these API's you have to fill a form to request access first.This process is usually quite quick, and plenty of APIs are still free even though they require an API key.

For better insight, click [here](https://schoolofdata.org/2013/11/18/web-apis-for-non-programmers/?__cf_chl_jschl_tk__=7bd9c1655390183d7bb02cc201bc980b54f38e22-1602518516-0-AdHsrAe32jCNKyIqmgWm0c5xuBPkk1v3TZLclqXJvR-3fJJtYYv-7q9IYF4G_pUJ39JdWovIB2BlC9ABx9xto4zFMaXuy9lHcRFjjeVLp1zHOkPIs1titSorWsPwZrtqcPzQ2LfEJ_1bnz1BhX12OnGXC0_kvhdrQzPpP_CogmVgPWi6vrkOtoSBHppJ3w7LY5h3rmri8IVpCYNK-2tP6VXuOXu8Na-wBD4uehYi_fif97D5X7ET07-OY6sgzLe4JOf35iUL9gByITJkvQqOrROeYpFYGuVs5Fpj6bZPw-FqqFxZ6bWv54WSiY_SPhZ4mB_3wTjEJGItsglE4a1rSYg).

## Types of API:
**There are four main types of APIs:**


1. **Open APIs:** Also known as Public APIs, there are no restrictions to access these types of APIs because they are publicly available.

2. **Partner APIs:** One needs specific rights or licenses in order to access this type of APIs because they are not available to the public.

3. **Internal APIs:** Also known as Private APIs, only internal systems expose this type of API, which is, therefore, less known and often meant to be used inside the company. The company uses this type of API among the different internal teams to be able to improve its products and services.

4. **Composite APIs:** This type of API combines different data and service APIs. It is a sequence of tasks that run synchronously as a result of the execution and not at the request of a task. Its main uses are to speed up the process of execution and improve the performance of the listeners in the web interfaces.

## Components of an API:
**APIs consist of three parts:**

- **User:** the person who makes a request.
- **Client:** the computer that sends the request to the server.
- **Server:** the computer that responds to the request.

#### Make a URL request in a browser for that information:
 This uses your internet browser as the client, and you will get back a text document in coding language to sort through.

 #### Use a program that requests the information and translates it into usable form:
  You can code your own program or use a ready-made HTTP client. This requires more coding fluency, but is great for programmers who want to use the database of another program to enhance their own apps.
  Many companies use the open APIs from larger companies like Google and Facebook to access data that might not otherwise be available.
  ## Actions can be taken through an API:
   **There are four types of actions an API can perform:**

  - **GET:** requests data from a server can be status or specifics (like last_name).
  - **POST:** sends changes from the client to the server; think of this as adding information to the server, like making a new entry.
  - **PUT:** revises or adds to existing information.
  - **DELETE:** deletes existing information.

  #### Ways to make a request on a server:

  - **HTTP:** hypertext transfer protocol. This is how you got to our site in the first place by typing a URL in the search bar in your browser. This is a really easy way to access data, but it won't come back to you in a pretty format if you request a lot of information. We'll go into this further in just a second.

  - **Text formats:** XML, JSON. These are the main languages for accessing data over an API. When you receive your data, you will need to wade through the XML or JSON code to understand what the server gave you.

  ## How to start using an API?

  - Most APIs require an API key. Once you find an API you want to play with, look in the documentation for access requirements. Most APIs will ask you to complete an identity verification, like signing in with your Google account. Youâ€™ll get a unique string of letters and numbers to use when accessing the API, instead of just adding your email and password every time.

  - The easiest way to start using an API is by finding an HTTP client online, like REST-Client, [Postman](https://www.postman.com/downloads/), or [Paw](https://paw.cloud/). These ready-made tools helps to structure the requests to access existing APIs with the API key one received. One will still need to know some of the syntax from the documentation, but there is very little coding knowledge required.
  
  - The next best way to pull data from an API is by building a URL from existing API documentation.
   
 > ***"An API request doesn't look that much different from a normal browser URL, but the returned data will be in a form that's easy for computers to read."***

For more information and example, check [here](https://gigaom.com/2010/10/29/using-apis-not-quite-as-hard-as-it-looks/).

## An example for explaining the workflow of an API for non- programmer:

1. If a user want some data from service X.Check out does service X has an API or not. If yes, ten proceed.
2. Look at the API documentation. Figure out if there is a URL that retrieves the kind of data you're looking for.
3. Sign up for an API key if one is required.
4. Figure out what parameters you need to include in the URL in order to get the exact data you want.
5. Load the URL, parameters included into your browser. If you are getting an error , go back to the 4th point.
6. Take that data and unpack it. For more information, read [here](https://schoolofdata.org/2013/11/21/xml-and-json/).


## For further readings:

- [API-google-sheets](https://rapidapi.com/blog/api-google-sheets/).
- [API-tutorial-for-node.js](https://rapidapi.com/blog/nodejs-express-rest-api-example/).
- [create_API](https://rapidapi.com/api-providers)

## References from:

- Technology-Advice
- School of Data
- Rapidapi




