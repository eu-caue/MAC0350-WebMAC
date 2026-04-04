function addProblem() {
    const title = document.getElementById("title").value;
    const category = document.getElementById("category").value;
    const difficulty = document.getElementById("difficulty").value;
    const statement = document.getElementById("statement").value;

    const newProblem = {
        title,
        category,
        difficulty,
        statement
    };

    const problems = JSON.parse(localStorage.getItem("problems")) || [];
    problems.push(newProblem);
    localStorage.setItem("problems", JSON.stringify(problems));
    window.location.href = "index.html";
}