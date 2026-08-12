document.addEventListener("DOMContentLoaded", () => {
    const searchForm = document.querySelector(".search");
    const studentForm = document.querySelector(".student-form");

    // if (searchForm) {
    //     searchForm.addEventListener("submit", (event) => {
    //         event.preventDefault();
    //         alert("Qidiruv hozircha backendga ulanmagan.");
    //     });
    // }

    // if (studentForm) {
    //     studentForm.addEventListener("submit", (event) => {
    //         event.preventDefault();
    //         alert("Forma tayyor. Keyingi darslarda Django backendga ulanadi.");
    //     });
    // }
});


document.querySelector('.search').addEventListener('submit', function (e) {
    var input = document.getElementById('q');

    // Agar input bo'sh bo'lsa yoki faqat bo'shliqlardan iborat bo'lsa
    if (!input.value.trim()) {
        e.preventDefault(); // Formaning standart yuborilishini to'xtatamiz
        // Formaning action manziliga (? belgisiz) shunchaki o'tamiz
        window.location.href = this.action;
    }
});