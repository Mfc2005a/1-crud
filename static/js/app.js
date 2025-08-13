alert("Qualquer coisa");

let index = 0; 
        const titles = [ 
            "Mateus Ferrari Costa",
            "Desenvolvedor Full stack",
        ]; 
        function changeTitle(index, delay) {
            
            setInterval(() => {
                document.querySelector("h1").textContent = titles[index];
                index = (index + 1) % titles.length; // Retorna ao início
            }, delay);
        }
        changeTitle(index, 3000); //  
    
        document.querySelector(".stack").addEventListener("click", () => {

            const p = document.querySelector(".stack");
            p.style.color = "#00ff00"; // texto verde 
            p.style.backgroundColor = "#000;" // fundo preto
            p.style.padding = "10px" 
        });
        
        const topBtn = document.getElementById("topBtn")

        window.onscroll = () => {
            if (window.scrollY > 100) {
                topBtn.style.display = "block" ;
}           else {
                topBtn.style.display = "none" ; 
            }
        };

        topBtn.onclick = () => {
            window.scrollTo({top: 0, behavior: "smooth"});
        
        };

        const stack = document.querySelector(".stack")
        stack.classList.add("fade-in")
        setTimeout(() => {
            stack.classList.add("visible");

        }, 100);
        
        const titulo = [
            
        ]

        let indice = 0 
        const h1 = document.getElementById("titulo");

        setInterval(() => {
            indice = (indice + 1 ) % titulos.length; // Retorna ao inicio 
            h1.textContent = titulo[indice];

        }, 4000);