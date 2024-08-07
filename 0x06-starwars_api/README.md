# 0x06. Star Wars API
> - Algorithm
> - API
> - JavaScript

The `0. Star Wars Characters` project requires you to interact with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with several key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

## Method
- `Request` was used to fetch data from the API `https://swapi-api.alx-tools.com/api/films/[id]`.
- `process.argv` was used to get the ID of the movie from the command line.

- After fetching the data, the characters of the film are obtained, and then another request is made to retrieve each character and print them on separate lines.