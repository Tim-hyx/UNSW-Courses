# Tute 08

## 1. Code Review

Take a look at the ReactJS app in `review/`. It is the ReactJS component from lab04.

What would you do to improve this source code? Discuss as a class.
 * What is wrong with the style of the source code for this page?
 * Make appropriate changes to clean up these DOM elements.

> * Overall pretty good
> * Inline CSS in Card.jsx
> * Incosistent use of JSX and JS file extensions
> * Inconsistent use of semi colons and non semi colons to terminal statements
> * App.js has a redundant wrapper element around the input
> * Many lines are very long and should be moved onto next line

## 2. Types of dependencies

For each of the following dependencies, would you install them as `dependencies` or `devDependencies`?
 * `"jest"` >> devDependency
 * `"async-lock"` >> dependency
 * `"express"` >> dependency
 * `"passport"` >> dependency
 * `"lint-staged"` >> devDependency
 * `"request"` >> dependency
 * `"typeorm"` >> dependency

## 3. ReactJS example

Create a folder `exercise3` with `create-react-app` and build a basic react app that uses the server provided for assignment 3 and:
 * Allows a user to register for an account on a route `/register`
 * Once registered, shows them a 'Welcome' screen on route `/dashboard`.

> See `solutions/exercise3`