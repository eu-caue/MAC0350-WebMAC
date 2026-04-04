const defaultProblems = [
    {
        title: "Palindrome Queries",
        category: "Strings",
        difficulty: "Difícil",
        statement: "\
Dado uma string inicial s e q queries com valores l e r, determine para cada query se a substring entre l e r é um palíndromo. \n\
Restrições: |s| &lt= 10^5, q &lt= 10^5, 1 &lt= l, r &lt= |s|"
    },
    {
        title: "Knapsack",
        category: "Programação Dinâmica",
        difficulty: "Médio",
        statement: "\
Um ladrão invade um museu e deseja roubar N itens. No entanto, sua mochila é limitada e consegue suportar no máximo W de peso. \n\
Dado o valor v_i e o peso w_i de cada item, diga qual o maior valor que o ladrão consegue retirar em apenas uma viagem. \n\
Restrições: 1 <= N, W, v_i, w_i <= 1000."
    }
];

let problems = JSON.parse(localStorage.getItem("problems"));

console.log("LS:", localStorage.getItem("problems"));
console.log("Parsed:", problems);

if (!problems) {
    problems = defaultProblems;
    localStorage.setItem("problems", JSON.stringify(problems));
}

function renderProblems(ProblemList) {
    const container = document.getElementById("problem-list");
    container.innerHTML = "";

    if (ProblemList.length === 0) {
        container.innerHTML = "<p><strong>Nenhum problema encontrado.</strong></p>";
        return;
    }

    ProblemList.forEach(problem => {
        const div = document.createElement("div");

        div.innerHTML = `
            <h3>${problem.title}</h3>
            <p><strong>Categoria:</strong> ${problem.category}</p>
            <p><strong>Dificuldade:</strong> ${problem.difficulty}</p>

            <details>
                <summary>Enunciado</summary>
                <pre>${problem.statement}</pre>
            </details>

            <button>Editar</button>
            <button>Remover</button>
            <hr>
        `;

        container.appendChild(div);
    });
}

function getCategories() {
    const categories = problems.map(p => p.category);
    return [...new Set(categories)].sort();
}

function populateCategoryFilter() {
    const select = document.getElementById("category");
    select.innerHTML = '<option>Todas as categorias</option>';

    const categories = getCategories();

    categories.forEach(cat => {
        const option = document.createElement("option");
        option.value = cat;
        option.textContent = cat;
        select.appendChild(option);
    });
}

function applyFilters() {
    const search = document.getElementById("search").value.toLowerCase();
    const category = document.getElementById("category").value;
    const difficulty = document.getElementById("difficulty").value;

    const filtered = problems.filter(p => {
        const matchTitle = p.title.toLowerCase().includes(search);
        const matchCategory = (category === "Todas as categorias" || p.category === category);
        const matchDifficulty = (difficulty === "Todas as dificuldades" || p.difficulty === difficulty);

        return matchTitle && matchCategory && matchDifficulty;
    });

    renderProblems(filtered);
}

document.addEventListener("DOMContentLoaded", () => {
    populateCategoryFilter();
    renderProblems(problems);
});