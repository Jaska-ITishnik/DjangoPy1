document.addEventListener("DOMContentLoaded", () => {
    const searchForm = document.querySelector(".search");
    const studentForm = document.querySelector(".student-form");

    if (searchForm) {
        searchForm.addEventListener("submit", (event) => {
            event.preventDefault();
            alert("Qidiruv hozircha backendga ulanmagan.");
        });
    }

    if (studentForm) {
        studentForm.addEventListener("submit", (event) => {
            event.preventDefault();
            alert("Forma tayyor. Keyingi darslarda Django backendga ulanadi.");
        });
    }
});
