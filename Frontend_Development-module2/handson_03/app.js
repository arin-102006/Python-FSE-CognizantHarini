import { courses } from "./data.js";

let displayedCourses = [...courses];

const courseGrid = document.querySelector(".course-grid");
const totalCredits = document.getElementById("total-credits");
const searchInput = document.getElementById("search-courses");
const sortButton = document.getElementById("sort-btn");
const selectedCourse = document.getElementById("selected-course");

// ES6 Features

displayedCourses.forEach(({ name, credits }) => {
    console.log(`${name} - ${credits} credits`);
});

const formattedCourses = displayedCourses.map(
    course => `${course.code} - ${course.name} (${course.credits} credits)`
);
console.log(formattedCourses);

const filteredCourses = displayedCourses.filter(
    course => course.credits >= 4
);
console.log("Courses with 4 or more credits:", filteredCourses.length);

const creditTotal = displayedCourses.reduce(
    (sum, course) => sum + course.credits,
    0
);
console.log("Total Credits:", creditTotal);

// Render Function

function renderCourses(courseList) {

    courseGrid.innerHTML = "";

    courseList.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p><strong>Code:</strong> ${course.code}</p>
            <p><strong>Credits:</strong> ${course.credits}</p>
            <p><strong>Grade:</strong> ${course.grade}</p>
        `;

        courseGrid.appendChild(article);

    });

    const total = courseList.reduce(
        (sum, course) => sum + course.credits,
        0
    );

    totalCredits.textContent = `Total Credits: ${total}`;

}

renderCourses(displayedCourses);

// Search

searchInput.addEventListener("input", () => {

    const keyword = searchInput.value.toLowerCase();

    const result = displayedCourses.filter(course =>
        course.name.toLowerCase().includes(keyword)
    );

    renderCourses(result);

});

// Sort

sortButton.addEventListener("click", () => {

    displayedCourses.sort((a, b) => b.credits - a.credits);

    renderCourses(displayedCourses);

});

// Event Delegation

courseGrid.addEventListener("click", (event) => {

    const card = event.target.closest(".course-card");

    if (!card) return;

    const id = Number(card.dataset.id);

    const course = displayedCourses.find(c => c.id === id);

    selectedCourse.textContent =
        `Selected Course: ${course.name} | Grade: ${course.grade}`;

});
