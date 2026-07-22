const loadBtn = document.getElementById("loadBtn");
const loading = document.getElementById("loading");
const notifications = document.getElementById("notifications");
const errorDiv = document.getElementById("error");
const retryBtn = document.getElementById("retryBtn");

// Task 1 - Promise with .then()

function fetchUser(id) {
    return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then(response => response.json())
        .then(user => {
            console.log("User:", user.name);
            return user;
        });
}

// Task 1 - async/await

async function fetchUserAsync(id) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);
        const user = await response.json();
        console.log("Async User:", user.name);
    } catch (error) {
        console.log(error);
    }
}

// Simulate loading local courses

function fetchAllCourses() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve([
                { name: "Data Structures" },
                { name: "Database Systems" },
                { name: "Web Development" }
            ]);
        }, 1000);
    });
}

async function loadCourses() {
    loading.textContent = "Loading courses...";

    const courses = await fetchAllCourses();

    loading.textContent = "";

    console.log(courses);
}

loadCourses();

// Promise.all()

Promise.all([
    fetchUser(1),
    fetchUser(2)
]).then(users => {
    console.log(users[0].name, users[1].name);
});

// Reusable Fetch Function

async function apiFetch(url) {

    try {

        loading.textContent = "Loading...";

        errorDiv.textContent = "";

        retryBtn.style.display = "none";

        notifications.innerHTML = "";

        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Unable to load data.");
        }

        const data = await response.json();

        loading.textContent = "";

        return data;

    } catch (error) {

        loading.textContent = "";

        errorDiv.textContent = error.message;

        retryBtn.style.display = "inline-block";

        return [];

    }

}

// Render Notifications

async function loadNotifications() {

    const posts = await apiFetch(
        "https://jsonplaceholder.typicode.com/posts?_limit=5"
    );

    posts.forEach(post => {

        const card = document.createElement("div");

        card.className = "notification-card";

        card.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.body}</p>
        `;

        notifications.appendChild(card);

    });

}

// Retry

retryBtn.addEventListener("click", loadNotifications);

loadBtn.addEventListener("click", loadNotifications);

// Axios Interceptor

axios.interceptors.request.use(config => {

    console.log("API call started:", config.url);

    return config;

});

// Axios Example

async function axiosExample() {

    try {

        const response = await axios.get(
            "https://jsonplaceholder.typicode.com/posts",
            {
                params: {
                    userId: 1
                }
            }
        );

        console.log(response.data);

    } catch (error) {

        console.log(error);

    }

}

axiosExample();

/*
Fetch vs Axios

1. Fetch is built into browsers; Axios is an external library.
2. Fetch requires response.json(); Axios parses JSON automatically.
3. Fetch does not throw errors for HTTP errors automatically; Axios does.
*/
