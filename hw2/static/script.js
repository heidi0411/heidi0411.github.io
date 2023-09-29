// Replace 'http://yourserver' with the actual URL of your Flask app
const baseUrl = 'http://127.0.0.1:5000/';

// Replace 'search' with the actual route you defined in Flask
const route = '/search';

// Define the parameters you want to send in the request
const queryParams = {

    keywords: 'iphone',
    'paginationInput.entriesPerPage': 10,
    'itemFilter(0).value': 25,
    'SECURITY-APPNAME': 'ChiTingH-firstApp-PRD-672bbdc3d-c7a8127b',
};

// Construct the URL with query parameters
const url = new URL(route, baseUrl);
Object.keys(queryParams).forEach((key) => {
    url.searchParams.append(key, queryParams[key]);
});

// Make the GET request to your Flask API
fetch(url)
    .then((response) => response.json())
    .then((data) => {
        // Handle the response data here
        console.log(data);
    })
    .catch((error) => {
        // Handle any errors here
        console.error('Error:', error);
    });
